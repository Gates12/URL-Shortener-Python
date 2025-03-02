from flask import Flask, request, jsonify, redirect
from flask_redis import FlaskRedis
from hashids import Hashids
from flask_swagger_ui import get_swaggerui_blueprint
import validators

app = Flask(__name__)
app.config['REDIS_URL'] = "redis://localhost:6379/0"
redis_client = FlaskRedis(app)
hashids = Hashids(min_length=6, salt="your-secret-salt")

# Swagger UI setup
SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={"app_name": "URL Shortener"})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

TTL_SECONDS = 86400  # 24 hours (adjustable)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    long_url = data.get("long_url")

    if not long_url or not validators.url(long_url):
        return jsonify({"error": "Invalid URL"}), 400

    # Check if the URL is already stored
    existing_key = redis_client.get(long_url)
    if existing_key:
        short_code = existing_key.decode('utf-8')
    else:
        short_code = hashids.encode(len(redis_client.keys('*')) + 1)
        redis_client.setex(short_code, TTL_SECONDS, long_url)  # Store with TTL
        redis_client.set(long_url, short_code)  # Store reverse mapping
        redis_client.set(f"count:{short_code}", 0)  # Initialize visit count

    short_url = f"http://127.0.0.1:5000/{short_code}"
    return jsonify({"short_url": short_url})

@app.route('/<short_code>')
def redirect_url(short_code):
    long_url = redis_client.get(short_code)
    if long_url:
        redis_client.incr(f"count:{short_code}")  # Increment visit count
        return redirect(long_url.decode('utf-8'))
    return jsonify({"error": "Short URL expired or not found"}), 404

@app.route('/access_count/<short_code>', methods=['GET'])
def get_access_count(short_code):
    access_count = redis_client.get(f"count:{short_code}") or 0
    return jsonify({"short_code": short_code, "access_count": int(access_count)}), 200

@app.route('/')
def home():
    return "Welcome to the URL Shortener! Visit /swagger to test."

if __name__ == '__main__':
    app.run(debug=True)

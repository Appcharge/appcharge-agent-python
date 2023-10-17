from app import app
from config.settings import get_settings


if __name__ == '__main__':
    app_port = get_settings().APP_PORT
    app.run(host="0.0.0.0", port=app_port, debug=True)

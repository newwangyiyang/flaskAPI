"""
    flask项目的入口app
"""
from app.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8089, debug=app.config['DEBUG'])
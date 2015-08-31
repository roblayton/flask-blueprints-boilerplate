#!/usr/bin/env python

import sys
from app import create_app
from config import config

app = create_app('DEVELOPMENT')
def start_with_flask_server(port=app.config['PORT']):
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    start_with_flask_server()

# THE MAIN ENTRY OF THE WEBSERVER
from logging import debug
from webserver import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

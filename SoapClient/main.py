from app import create_app
from flask import render_template
import logging
from app.models import db


logger = logging.getLogger(__name__)

app = create_app('flask.cfg')


@app.route("/", methods=["GET"])
def index():
    return render_template('home.html')




if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5005, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
from flask import Flask, url_for, make_response, render_template, request # request 는 GET 인지 POST 인지 DELETE 인지 등등 구별해준다.
import urllib.parse

app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
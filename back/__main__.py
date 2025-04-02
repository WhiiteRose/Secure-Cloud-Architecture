import os
import sys
import flask


app = flask.Flask('app')


@app.route('/', defaults={ 'path': None })
@app.route('/<path:path>')
def get_static(path: str | None) -> flask.Response:
    if path is None:
        return flask.redirect('/index.html')
    return flask.send_from_directory("static", path)


if __name__ == "__main__":
    app.run(debug=True)

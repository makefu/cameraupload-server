from flask import Flask, request, redirect, send_from_directory, jsonify
import os.path
from os.path import basename, abspath
from shutil import copyfileobj
from pathlib import Path

from glob import iglob
app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('CUSERVER_SETTINGS',silent=True)


@app.route('/',methods=['GET'])
def init():
    d = abspath(app.config['STOREDIR'])
    files = iglob(f"{d}/*.jpg")
    try:
        last = basename(max(files,key=os.path.getctime))
        return send_from_directory(d, last,
                mimetype='image/jpeg')
    except:
        return "no pics :("

@app.route('/',methods=['POST'])
def load():
    from datetime import datetime
    d = app.config['STOREDIR']
    Path( d ).mkdir(parents=True, exist_ok=True)

    now = datetime.now().replace(second=0, microsecond=0).isoformat('T')

    direction = request.args.get('direction')
    fname = f"{d}/{direction}-{now}.jpg"
    with open(fname,"wb") as fo:
        copyfileobj(request.stream, fo)
    return jsonify({"success":1})

if __name__ == '__main__':
    app.run()

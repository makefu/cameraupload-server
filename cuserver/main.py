from flask import Flask, request, redirect, send_file
import os.path

from glob import iglob
app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('CUSERVER_SETTINGS',silent=True)


@app.route('/',methods=['GET'])
def init():
    files = iglob("*.jpg")
    try:
        last = max(files,key=os.path.getctime)
        return send_file(last, mimetype='image/jpg')
    except:
        return "no latest image :("

@app.route('/',methods=['POST'])
def load():
    from datetime import datetime
    now = datetime.now().replace(second=0, microsecond=0).isoformat('T')
    direction = request.args.get('direction')
    fname = f"{direction}-{now}.jpg"
    # image = request.values
    image = request.stream.read()
    with open(fname,"wb") as fo:
        fo.write(image)
    return redirect(request.url)

if __name__ == '__main__':
    app.run()

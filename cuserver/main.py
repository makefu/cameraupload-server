from flask import Flask,render_template,jsonify,request, redirect
from os.path import join

app = Flask(__name__)

# default config
app.config.from_pyfile('default_config.py')
# bonus config
app.config.from_envvar('CUSERVER_SETTINGS',silent=True)


@app.route('/',methods=['GET'])
def hello():
    return "hello from cameraupload-server"

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

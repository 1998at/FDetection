from flask import Flask, request, Response,render_template,send_file
import time
from flask_cors import CORS

PATH_TO_TEST_IMAGES_DIR = './images'

app = Flask(__name__)
CORS(app)

"""@app.route('/')
def index():
    return render_template("getImage.html")
    #return Response(open('./static/getImage.html').read(), mimetype="text/html")
"""
# save the image as a picture
@app.route('/image', methods=['POST'])
def image():

    i = request.files['image']  # get the image
    f = ('%s.png' % time.strftime("%Y%m%d-%H%M%S"))
    i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
    return send_file(PATH_TO_TEST_IMAGES_DIR+"/"+f, mimetype='image/gif')
    #return render_template("results.html",image_name=f)

    #return Response("%s saved" % f)

if __name__ == '__main__':
    app.run()

import os
from flask import Flask, g, request, redirect, url_for, render_template
from flask import send_from_directory
from werkzeug import secure_filename
from PIL import Image
import color_bands

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = './static/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            global images
            images = [filename]
            images = color_bands.gen_bands(os.path.join(app.config['UPLOAD_FOLDER']), filename, images)
            g.images = images
            return redirect(url_for('base_image'))
    return render_template('index.html')

@app.route('/show')
def base_image():
    global images
    path = 'http://127.0.0.1:5000/uploads/'
    return render_template('stego.html', path=path, images=images)

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )

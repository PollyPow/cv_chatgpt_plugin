from werkzeug.utils import secure_filename
from flask import *
import os

ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file(request):
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    try :
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            foldername = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(foldername, filename)
            result = request.args.get("result")

        return filename, foldername, result

    except Exception as ex:
        print(ex)

        return -1


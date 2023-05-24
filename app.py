from fileloader import upload_file
from fileprocessor import pdf_to_text, remove_private
from flask import *
import os
import sys
import sending_prompt
import openai
from flask import Flask, redirect, render_template, request, url_for

ALLOWED_EXTENSIONS = {'pdf'}


app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def main():
    result = "No success"

    if request.method == 'POST':
        filename, foldername, result = upload_file(request)

    return render_template("index.html", result=result)


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        file = request.files['file']
        file.save(file.filename)
        text = pdf_to_text(file)

        private = request.form['private_info']
        text = remove_private(text, private)

        jd = request.form['job_description']

        # result = sending_prompt.openai_completion(text, jd)
        return render_template("Acknowledgement.html", name=file.filename, text=text)


if __name__ == '__main__':
    app.run(debug=True)

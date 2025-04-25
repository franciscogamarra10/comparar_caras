from flask import Flask, render_template, request, redirect
import face_recognition
import os
import numpy as np
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads'
UPLOAD_FOLDER2 = 'feedback'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_FOLDER2'] = UPLOAD_FOLDER2
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route("/")
def index():
    return render_template("index.html")
@app.route('/', methods=['GET', 'POST'])
def predi():
    result = None
    distance = None
    file1_url = file2_url = None

    if request.method == 'POST':
        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
            filename1 = secure_filename(file1.filename)
            filename2 = secure_filename(file2.filename)

            filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
            filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)

            file1.save(filepath1)
            file2.save(filepath2)

            image1 = face_recognition.load_image_file(filepath1)
            image2 = face_recognition.load_image_file(filepath2)

            encodings1 = face_recognition.face_encodings(image1)
            encodings2 = face_recognition.face_encodings(image2)

            if len(encodings1) > 0 and len(encodings2) > 0:
                face1 = encodings1[0]
                face2 = encodings2[0]

                distance = np.linalg.norm(face1 - face2)

                if distance < 0.5:
                    result = "Sos vos"
                elif distance < 0.7 and distance >0.5:
                    result = "Son parecidos"
                else:
                    result = "Son diferentes personas"
            else:
                result = "No se detecto cara en alguna o en las dos fotos"

            file1_url = '/' + filepath1
            file2_url = '/' + filepath2

    return render_template('index.html', result=result, distance=distance, file1_url=file1_url, file2_url=file2_url)

@app.route("/feedback", methods=["POST"])
def feedback():
    feedback_text = request.form.get("feedback", "")

    fname=os.path.join(app.config['UPLOAD_FOLDER2'], "feedback.txt")
    if feedback_text:
        with open(fname, "a+") as f:
            f.write(feedback_text + "\n---\n")
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) ## for docker
    #app.run(debug=True) ##local run



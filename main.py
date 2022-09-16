from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config['UPLOAD_FOLDER'] = 'files'


class UploadFileForm(FlaskForm):
    file = FileField('File', validators=[InputRequired()])
    submit = SubmitField('Upload File')

# defining methods
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/returnjson', methods=['GET'])

# defining a function for uploading a file through API
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # first grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))) # uploading the file
        return 'File has been uploaded'

    return render_template('index.html', form=form)

    # creating one empty dictionary to hold the jsonified data
    dict1 = {}

    with open('C:/Users/Ravi/OneDrive/Documents/RedHatFilePath.txt', 'r') as fh: # opening the file using 'open' function

        # reading the lines and trimming the extra spaces
        for line in fh:
            command, description = line.strip().split(None, 1)

            dict1[command] = description.strip()

    # creating a json file
    # the JSON file is named as 'output'
    out_file = open('output.json', 'w')
    json.dump(dict1, out_file, indent=4, sort_keys=False) # jsonifying the output
    out_file.close() # closing the file


if __name__ == '__main__':
    app.run()











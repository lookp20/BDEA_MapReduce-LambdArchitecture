from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename
import os
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import glob
import numpy as np
import subprocess

text_folder = '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection'
extensions = set(['txt', 'pdf', 'docx'])
text_path = '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection'

app = Flask(__name__)

Image_folder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = Image_folder

def allowed_extensions(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in extensions

def create_wordcloud_DIRECT(text_Path):
    for filename in glob.glob(os.path.join(text_path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as file:
            text = file.read()
    text = text.replace('\n', ' ')
    # save the name
    if filename.startswith(text_path+'/') and filename.endswith('.txt'):
        file_name = filename[len(text_path+'/'):-4]
    # Create stopword list:
    stopwords = set(STOPWORDS)
    stopwords.update(['der', 'die', 'das', 'und', 'dass', 'nicht'])

    # lower max_font_size, change the maximum number of word and lighten the background:
    wordcloud = WordCloud(stopwords=stopwords,width=1900, height=1000, max_font_size=100, max_words=200, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt.savefig('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/images/'+file_name+'.png')
    


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename =='':
            return redirect(request.url)
        if allowed_extensions(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(text_folder, filename))
            return redirect(request.url), create_wordcloud_DIRECT(text_path)
    return render_template('index.html')

@app.route('/create_WordCloud_direct', methods=['GET', 'POST'])
def create_WordCloud_direct():
    if request.method == 'POST':
        if not os.listdir(app.config['UPLOAD_FOLDER']):
            return redirect(url_for('index'))
        else:
            for filename in glob.glob(os.path.join(text_path, '*.txt')):   
                if filename.startswith(text_path+'/') and filename.endswith('.txt'):
                    file_name = filename[len(text_path+'/'):-4]
            img = os.path.join(app.config['UPLOAD_FOLDER'], file_name+'.png')
            #subprocess.call("./text_collection.sh", shell=True)
            #subprocess.call('./image_collection.sh', shell=True)
            return render_template('index.html', img=img)
    return render_template('index.html')

@app.route('/image')
def image_collection():
    return render_template('image_collection.html')


@app.route('/text')
def text_collection():
    return render_template('text_collection.html')

@app.route('/wordcount')
def wordcount():
    return render_template('wordcount.html')


@app.route('/document_frequency')
def document_frequency():
    return render_template('document_frequency.html')

if __name__ == '__main__':
    app.run(port=1337, debug=True)
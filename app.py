from flask import Flask, render_template, url_for, redirect, request
from werkzeug.utils import secure_filename
import os, sys, stat, operator
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import glob
import numpy as np
import subprocess
import shutil
import random
import json

text_folder = '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection'
extensions = set(['txt', 'pdf', 'docx'])
text_path = '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/text_collection'
text_path_BATCH = '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_for_wc_BATCH'


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
    wordcloud = WordCloud(stopwords=stopwords,width=400, height=300, max_font_size=100, max_words=500, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt.savefig('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/images/'+file_name+'.png')

def create_wordcloud_BATCH(text_path_BATCH):
    for filename in glob.glob(os.path.join(text_path_BATCH, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as file:
            text = file.read()
    # save the name
    if filename.startswith(text_path_BATCH+'/') and filename.endswith('.txt'):
        file_name = filename[len(text_path_BATCH+'/'):-4]
    # Create stopword list:
    stopwords = set(STOPWORDS)
    stopwords.update(['der', 'die', 'das', 'und', 'dass', 'nicht'])

    # lower max_font_size, change the maximum number of word and lighten the background:
    wordcloud = WordCloud(stopwords=stopwords,width=400, height=300, max_font_size=100, max_words=500, background_color="white").generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    return plt.savefig('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/img_for_BATCH/'+file_name+'.png')

def clean(word):
    word = word.replace('\xc3\x84', 'ae')
    word = word.replace('\xc3\x96', 'oe')
    word = word.replace('\xc3\x9c', 'ue')
    word = word.replace('\xc3\x9f', 'ss')
    word = word.replace('\xc3\xa4', 'ae')
    word = word.replace('\xc3\xb6', 'oe')
    word = word.replace('\xc3\xbc', 'ue')
    word = word.replace('\xc5\xbf', 's')
    word = word.replace('u\xcd\xa4', 'ue')
    word = word.replace('a\xcd\xa4', 'ae')
    word = word.replace('o\xcd\xa4', 'oe')
    word = word.replace('\xc5\xbf', 's')
    word = word.replace('U\xcd\xa4', 'ue')
    word = word.replace('A\xcd\xa4', 'ae')
    word = word.replace('O\xcd\xa4', 'oe')    
    return word
def clean_python3(word):
    word = word.replace('Ä', 'ae')
    word = word.replace('Ö', 'oe')
    word = word.replace('Ü', 'ue')
    word = word.replace('ß', 'ss')
    word = word.replace('ä', 'ae')
    word = word.replace('ö', 'oe')
    word = word.replace('ü', 'ue')
    word = word.replace('ſ', 's')
    word = word.replace('uͤ', 'ue')
    word = word.replace('aͤ', 'ae')
    word = word.replace('oͤ', 'oe')
    word = word.replace('ſ'.upper(), 's')
    word = word.replace('uͤ'.upper(), 'ue')
    word = word.replace('aͤ'.upper(), 'ae')
    word = word.replace('oͤ'.upper(), 'oe')    
    return word

def MR_OneDoc(Doc):
    cmd = Doc
    finalcmd = '#!/bin/bash\n'+'docker exec -t 4c0d173b1e74 hdfs dfs -rm -r /user/history/output1\n'+'docker exec -t 4c0d173b1e74 rm -r /src/output1\n'+'rm -r /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/output1\n'+'docker exec -t 4c0d173b1e74 hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.6.0-cdh5.7.0.jar -D mapreduce.job.ubertask.enable=true -file /src/mapper2.py -mapper "python mapper2.py" -file /src/reducer.py  -reducer "python reducer.py" -input /user/history/Flask_textcollection/'+cmd+' -output /user/history/output1\n'+'docker exec -t 4c0d173b1e74 hdfs dfs -get /user/history/output1 /src\n'+'docker cp 4c0d173b1e74:/src/output1 /Users/lookphanthavong/Documents/VisualStudioCode/BDEA\n'+'for file in /Users/lookphanthavong/Documents/VisualStudioCode/BDEA/output/output1/part*; do mv "$file" "${file%.exec}.txt"; done'
    bash_text = open('MapReduce_OneDoc_Job.sh', 'w')
    bash_text.write(finalcmd)
    bash_text.close()
    os.chmod("./MapReduce_OneDoc_Job.sh", stat.S_IXUSR)
    return bash_text

def normalize_doc():
    z = {}
    for i in os.listdir("/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/output1"):
        if i.startswith("part-"):
            with open("/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/output1/"+i,"r") as file:
                    output = file.read()
                    output = output.replace('\t', '":')
                    output = output.replace('\n', ',"')
                    output = '{"'+output+'}'
                    output = output.replace(',"}', '}')
                    output = json.loads(output)
                    sorted_dict = sorted(output.items(), key=operator.itemgetter(1))
    for a in os.listdir('./static/text_library'):
        with open("/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library/"+a,"r") as file:
            for_text = file.read()
            for_text = for_text.lower()
            for_text = clean_python3(for_text)
            for i in range(len(sorted_dict)):
                if sorted_dict[i][0] in for_text:
                    if sorted_dict[i][0] in z:
                        z[sorted_dict[i][0]] += 1
                    else:
                        z[sorted_dict[i][0]] = 1
    normcount = {}
    for key in output:
        normcount.update({key:output[key]/z[key]})
        sorted_dict_norm = sorted(normcount.items(), key=operator.itemgetter(1))
        sorted_dict_norm.reverse()
    text_list = ''
    for i in range(len(sorted_dict_norm)):
        text_list +=(sorted_dict_norm[i][0] + ' ')*sorted_dict_norm[i][1]
    a = open("/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_for_wc_batch/text.txt", "w")
    a.write(text_list)
    a.close()
    return a
  
    
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
            if not os.path.exists('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library/'+filename+'.txt'):
                shutil.copy(text_folder+'/'+filename, '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library')
            else:
                shutil.copy(text_folder+'/'+filename, '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library/'+filename+str(random.randint(0, 100))+'.txt') 
            return redirect(request.url), create_wordcloud_DIRECT(text_path)
    return render_template('index_alt.html')

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
            if not os.path.exists('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/Gallery/'+file_name+'.png'):
                shutil.copy(img, '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/Gallery')
            else:
                shutil.copy(img, '/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/Gallery/'+file_name+str(random.randint(0, 100))+'.png') 
            return render_template('index_alt.html', img=img)
    return render_template('index_alt.html')

@app.route('/upload_to_hdfs', methods=['GET', 'POST'])
def upload_to_hdfs():
    if request.method == 'POST':
        if os.listdir(text_folder) or os.listdir(app.config['UPLOAD_FOLDER']):
            subprocess.call("./text_collection.sh", shell=True)
            subprocess.call("./image_collection.sh", shell=True)
            return redirect(url_for('create_WordCloud_direct'))
        else:
            return render_template('index_alt.html')
    return render_template('index_alt.html')

@app.route('/image', methods=['GET', 'POST'])
def image_collection():
    if request.method == 'GET':
        img = os.listdir('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/Gallery')
        return render_template('image_collection.html', img=img)
    return render_template('image_collection.html')
   
@app.route('/text', methods=['GET', 'POST'])
def text_collection():
    if request.method == 'GET':
        txt = os.listdir('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/text_library')
        return render_template('text_collection.html', txt=txt)
    return render_template('text_collection.html')

@app.route('/Document_TagCloud', methods=['GET','POST'])
def Document_TagCloud():
    if request.method == 'POST':
        text = request.form["text"]
        MR_OneDoc(text)
        os.chmod('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/MapReduce_OneDoc_Job.sh', 0o775)
        subprocess.call('./MapReduce_OneDoc_Job.sh', shell=True)
        normalize_doc()
    return render_template('Dokumenten_TagCloud.html'), create_wordcloud_BATCH(text_path_BATCH)

@app.route('/Display_TagCloud', methods=['GET', 'POST'])
def Display_TagCloud():
    if request.method == 'POST':
        img_BATCH = os.listdir('/Users/lookphanthavong/Documents/VisualStudioCode/BDEA/flask/static/img_for_BATCH')
        return render_template('Dokumenten_TagCloud.html', img_BATCH=img_BATCH)
    return render_template('Dokumenten_TagCloud.html')


@app.route('/Korpus_TagCloud')
def Korpus_TagCloud():
    return render_template('Korpus_TagCloud.html')

if __name__ == '__main__':
    app.run(port=1337, debug=True)

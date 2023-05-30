import os 
from os import getcwd
from flask import Blueprint,jsonify, request, send_from_directory
from werkzeug.utils import secure_filename
import cv2 
image = Blueprint('img_upload',__name__)

PATH_FILE = getcwd() + '/src/img/'
ALLOWED_EXTENSION =set(['png','jpg','jpge'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSION


@image.route('/img/<string:name_img>',methods = ['POST'])
def upload_img(name_img):


    if 'file' not in request.files :
        return jsonify({'message':'no file part in the request'}) , 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No file selected for uploading'})
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        name = name_img + '.' + filename.rsplit('.',1)[1].lower()
        file.save(os.path.join(PATH_FILE, name))
        url = '/upload/img/'+ name
        imgs = cv2.imread( PATH_FILE+ name)
        imgs2 = cv2.resize(imgs, (400,200))
        print(imgs.shape)
        print(imgs2.shape)
        cv2.imwrite('src/img/r'+ name ,imgs2)
       
        return jsonify({'message':'File successfully uploaded', 'url': url})
    else:
        return jsonify({'message':'Allowed file type are png'}) , 400


@image.route('/img/<string:name_img>')
def get_file(name_img):
    return send_from_directory(PATH_FILE, path=name_img , as_attachment=False)




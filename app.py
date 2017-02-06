from flask import Flask
from flask import render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import models
from models import Base
from models import ImageMeta
from models import UserData
from werkzeug import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'imgFolders/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_FILE_EXTENSIONS = set(['tar', 'zip'])

#web services API
@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/upload-files", methods=['GET', 'POST'])
def uploadfile():
	if request.method == 'POST':
		imgFile = request.files['file']
		if imgFile and allowed_file_type(imgFile.filename):
			filename = secure_filename(imgFile.filename)
			imgFile.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return ''
	return 'not successfully upload'

#helper function
def allowed_file_type(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_FILE_EXTENSIONS

#testing postgresql with sqlalchemy
# db = SQLAlchemy(app)
# engine = create_engine('postgresql://localhost/cmpe295')
# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# image1 = ImageMeta(path='abc/ccc', preProcessed = True)
# image2 = ImageMeta(path='abc/bbb', preProcessed = False)
# session.add(image1)
# session.add(image2)

# employee1 = UserData(userName='Andrew', workType='admin')
# employee2 = UserData(userName='Eric', workType='operator')
# session.add(employee1)
# session.add(employee2)

# try:
# 	session.commit()
# except SQLAlchemyError as ex:
# 	session.rollback()
# 	print(str(ex))

# for image in session.query(ImageMeta).all():
# 	print("id", image.id)
# 	print("path", image.path)
# 	print("preprocessed", image.preProcessed)
# 	print("add date", image.createDate)
# 	print("preprcessed date", image.preprocessedDate)

# for employee in session.query(UserData).all():
# 	print("id", employee.id)
# 	print("name", employee.userName)
# 	print("preprocessed", employee.workType)
# 	print("add date", employee.createDate)	

# engine.dispose()

if __name__ == "__main__":
	app.run()
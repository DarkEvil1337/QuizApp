from inspect import Parameter
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

def loadAllPicture():
  filepath = 'picDB.txt'
  pictures=[]
  with open(filepath) as fp:
    line =readline()
    cnt=1
    while line:
      if line!='':
        fullPicInfo = line.strip().split(';')
        pictures.append(fullPicInfo[1])
      line=fp.readline()
      cnt+=1
    fp.close()
    return pictures

#Pirmā lapa, kas tiks ielādēta
@app.route('/',methods = ['POST', 'GET'])
def root():
    return render_template("index.html")
    
#Pārbaudes lapa, lai saprastu, ka kods vispār strādā
@app.route('/health')
def health():
  return "OK"

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/test', methods=['POST', 'GET'])
def test():
    parametri = ["IQ","Augums","Kājas izmērs"]
    images = ["https://www.rd.com/wp-content/uploads/2021/01/GettyImages-1175550351.jpg","https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-mediumSquareAt3X-v2.jpg","https://cdn.mos.cms.futurecdn.net/VSy6kJDNq2pSXsCzb6cvYF.jpg"] 
    return render_template("test.html",parametri=parametri, images=images)

if __name__ == '__main__':
  app.run(debug="true")
from flask import Flask, request, render_template
from flask import request
from flask import jsonify


from arun import summerization
app = Flask(__name__)
@app.route('/')
def home():
	return render_template("a.html")
@app.route('/out',methods=['GET','POST'])
def out():
	inpt=str(request.form.get("url"))
	
	m=int(request.form.get("nol"))
	print(type(m))
	b=summerization(inpt,m)
	a="-->"
	for i in b:
		a=a+i+"<br />"+"-->"
	return '<html><body bgcolor="black"><font color="white" size="5px">'+a+'</font></body></html>'
	
if __name__ == '__main__':
	app.run(debug=True)
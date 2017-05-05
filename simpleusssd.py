from flask import Flask,session,request
from flask_session import Session

app= Flask(__name__)

app.secret_key= 'A0Zr98jT'
@app.before_request
def session_management():
    # make the session last indefinitely until it is cleared
    session.permanent = True

@app.route("/",methods=["POST"])
def respond():
	#get request form data
	session.clear()
	info=[]
	info.append(request.form.get("sessionId"))
	info.append(request.form.get("serviceCode"))
	info.append(request.form.get("phoneNumber"))
	info.append(request.form.get("text"))
	session['sessionId']=info[0]
	if info[3]=="1" or info[3]=="3" :
		session.clear()
		response="END Goodbye to Sir i can help you"
		return response

	response="CON Welcome to Complab"+info[2]+ "\n"
	response+="1:Unashida hujui ni gani \n"
	response+="2:umepigwa na bibi \n"
	response+="3:Huna Pesa \n"
	response+="4:Yote yalio juu \n"
	return response

if __name__ == '__main__':
	app.run()
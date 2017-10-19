from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_home():
    return render_template('home.html')

@app.route("/responseM")
def render_responseM():
    mph = float(request.args['mph'])
    
    response = mph * 1.6
    return render_template('responseM.html', response = response)
    
if __name__=="__home__":
    app.run(debug=False, port=54321)

@app.route("/responseV")
def render_responseV():
    value = float(request.args['value'])
    
    response = value * .84
    return render_template('responseV.html', response = response)
    
if __name__=="__home__":
    app.run(debug=False, port=54321)
 
@app.route("/responseS")
def render_responseS():
    sandwich = float(request.args['sandwich'])
    
    response = sandwich / 5
    return render_template('responseS.html', response = response)
    
if __name__=="__home__":
    app.run(debug=False, port=54321)

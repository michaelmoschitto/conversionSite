from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_conversionPage():
    return render_template('conversionPage.html')

@app.route("/responseK")
def render_responseK():
    kilos = float(request.args['kilograms'])
    
    response = kilos / 1000
    return render_template('responseK.html', response = response)
    
if __name__=="__home__":
    app.run(debug=False, port=54321)

@app.route("/responseN")
def render_responseN():
    newtons = float(request.args['newtons'])
    
    response = newtons * 1000000
    return render_template('responseN.html', response = response)
    
if __name__=="__home__":
    app.run(debug=False, port=54321)
 
@app.route("/responseS")
def render_responseS():
    silly = float(request.args['silly'])
    
    response = silly * 6.6944754
    return render_template('responseS.html', response = response)
    
if __name__=="__home__":
    app.run(debug=False, port=54321)

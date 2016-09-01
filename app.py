from flask import Flask , render_template,request
import sent_mod as sm

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():

    return render_template('index.html',title = "SentAna")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def showContact():
    return render_template("contact.html")


@app.route("/getKeyword" ,  methods = ["POST"])
def get_keyword():
    topic = request.form['keyword']
    tweets = sm.get_tweet(topic)
    f = open("./twitter_out.txt").read()
    posCount = f.count("positive")
    negCount = f.count("negative")
    return render_template('chart.html', topic=topic,pos =posCount , neg = negCount , tweets = tweets )


@app.route("/contact" , methods = ["POST" , "GET"])
def contact():
    name = request.form["name"]
    email = request.form['email']
    text = request.form['text']
    if request.method == "POST":
        return render_template("response.html")





if __name__=='__main__':
    app.run(host="127.0.0.1" , port="33808")

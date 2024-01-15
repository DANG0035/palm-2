from flask import Flask, request, render_template
import google.generativeai as palm
palm.configure(api_key="AIzaSyDc9xO4tlqv9Ji6PimmfHnD0n_M3xg8UCY")
model = {"model":"models/chat-bison-001"}
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")
        print(q)
        r = palm.chat(
            **model,
            messages = q
        )
        return(render_template("index.html",result=r.last))
    else:
        return(render_template("index.html", result="waiting for question............."))
if __name__ == "__main__":
    app.run()

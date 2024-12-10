from flask import Flask,render_template

app=Flask(__name__)
print(app)
@app.route("/")
def Hello():
    name="sameer_Khan"
    return render_template("index.html",first_name=name)

@app.route("/user/<name>")
def User(name):
    return render_template("base.html",name=name)

@app.route("/user/jinja")
def jinjaFilter():
    fav_fruit=["apple","oranges",3]
    sports=["running","boxing","kabbadi","kho-kho","cricket"]
    name=["sameer","tanveer","faizan",41]
    stuff="this is the <strong>Bold</strong> tag"
    return render_template("jinjaFilter.html",stuff=stuff,fav_fruit=fav_fruit,sports=sports,name=name)

if __name__=="__main__":
    app.run(debug=True)


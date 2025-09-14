from flask import Flask, request, render_template, url_for, redirect, flash
import model

app = Flask(__name__)
app.secret_key = "FlashForBlogProject"

@app.route('/', methods=['GET'])
def all_blogs():
    blogs = model.read_db()
    return render_template("index.html", blogs=blogs)

@app.route('/create/blog', methods=['GET'])
def c_blog():
    return render_template("create.html")

@app.route('/create/blog', methods=['POST'])
def create_blog():
    author = request.form['author']
    text = request.form['text']
    db = model.read_db()
    db.append({'id': len(db) + 1, 'author': author, 'text': text })
    model.save_to_db(db)
    flash("created success!")
    return redirect(url_for("all_blogs"))  

if __name__ == "__main__":
    app.run(debug=True)
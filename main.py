import requests
from flask import Flask, render_template


app = Flask(__name__)
blog_url ="https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(blog_url)
blog_post = response.json()

@app.route('/')
def home():
    return render_template("index.html", blog_post = blog_post)

@app.route('/post/<int:blog_id>')
def posts(blog_id):
    return render_template("post.html", blogs=blog_post, blog_id=blog_id)


if __name__ == "__main__":
    app.run(debug=True)

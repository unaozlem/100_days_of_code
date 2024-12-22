from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
response=requests.get(blog_url)
blog_data=response.json()


@app.route('/')
def home():
    return render_template("index.html", blogs=blog_data)




@app.route('/post/<int:index>')
def get_blog_text(index):
    clicked_post = None
    for blog in blog_data:
        if blog['id'] == index:
            clicked_post = blog
    return render_template("post.html", blogs=clicked_post)

if __name__ == "__main__":
    app.run(debug=True)

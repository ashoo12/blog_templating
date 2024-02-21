from flask import Flask, render_template
import requests



app = Flask(__name__)

n_point_url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(n_point_url)
all_posts = response.json()
@app.route('/')
def get_post():
    return render_template("index.html",blogs=all_posts)


@app.route("/post/<int:index>")
def show_posts(index):

        return render_template("post.html",posts=all_posts,id=index)




if __name__ == "__main__":
    app.run(debug=True)
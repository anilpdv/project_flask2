from flask import Flask,redirect,request,url_for,render_template
from models import *

app = Flask(__name__)

@app.before_request
def before_request():
    initialize_db()

@app.teardown_request
def teardown_request(exception):
    db.close()


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/main/')
def main_page():

    return render_template('main.html',posts=Post.select().order_by(Post.date.desc()))


@app.route('/new_post/')
def new_post():
    return render_template('new_post.html')

@app.route('/create/',methods=['POST'])
def create_post():
    Post.create(
        book_title =request.form['title'],
        book_author =request.form['author'],
        text =request.form['post']
          )
    return redirect(url_for('main_page'))



if __name__ =='__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from models import User, init_db
from config import Config


import sqlite3
import logging

app = Flask(__name__)

app.config.from_object(Config)



# Configuration for Flask-Mail
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'b.akudbilla@alustudent.com'
app.config['MAIL_PASSWORD'] = 'YOUR_APP_PASSWORD'
app.config['MAIL_DEFAULT_SENDER'] = 'b.akudbilla@alustudent.com'

mail = Mail(app)

# Setup logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask-Login
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database setup
init_db()

@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    c.execute('SELECT id, username, password FROM users WHERE id = ?', (user_id,))
    user = c.fetchone()
    conn.close()
    if user:
        return User(*user)
    return None

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect(Config.DATABASE)
        try:
            c = conn.cursor()
            c.execute('SELECT id, username, password FROM users WHERE username = ?', (username,))
            user_row = c.fetchone()
            conn.close()
            if user_row and User.verify_password(password, user_row[2]):
                user = User(id=user_row[0], username=user_row[1], password=user_row[2])
                login_user(user)
                return redirect(url_for('home'))
        finally:
            conn.close()
        
        flash('Invalid credentials')
    return render_template('login.html')



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        hashed_password = User.hash_password(password)
        try:
            conn = sqlite3.connect(Config.DATABASE)
            c = conn.cursor()
            c.execute('INSERT INTO users (first_name, last_name, username, password) VALUES (?, ?, ?, ?)',
                      (first_name, last_name, username, hashed_password))
            conn.commit()
            conn.close()
            flash('Registration successful')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            print("######")
            flash('Username already exists')
        finally:
            conn.close()
    return render_template('signup.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/blog/<article_id>')
@login_required
def article(article_id):
    return render_template("article.html")

@app.route('/blog')
@login_required
def blog():
    return render_template("blog.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/book')
@login_required
def book():
    return render_template("book.html")

@app.route('/book_appointment', methods=['POST'])
@login_required
def book_appointment():
    expert_name = request.form['expertName']
    appointment_date = request.form['appointmentDate']
    appointment_time = request.form['appointmentTime']
    user_email = request.form['email']

    try:
        msg = Message("Appointment Confirmation",
                      recipients=[user_email])
        msg.body = f"Your appointment with {expert_name} is confirmed for {appointment_date} at {appointment_time}."
        mail.send(msg)
        flash('Appointment booked successfully! Check your email for confirmation.', 'success')
    except Exception as e:
        flash('Appointment booked, but there was an error sending the email confirmation.', 'warning')
        logging.error('Error sending email: %s', str(e))

    return redirect(url_for('book'))

@app.route('/discussions')
@login_required
def discussions():
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    c.execute("SELECT * FROM posts ORDER BY date DESC")
    posts = []
    for post in c.fetchall():
        post_dict = {'id': post[0], 'author': post[1], 'title': post[2], 'content': post[3], 'date': post[4], 'replies': []}
        c.execute("SELECT * FROM replies WHERE post_id=? ORDER BY date ASC", (post[0],))
        for reply in c.fetchall():
            post_dict['replies'].append({'author': reply[2], 'content': reply[3], 'date': reply[4]})
        posts.append(post_dict)
    conn.close()
    return render_template('discussions.html', posts=posts)

@app.route('/add_post', methods=['POST'])
@login_required
def add_post():
    author = request.form['author']
    title = request.form['title']
    content = request.form['content']
    date = datetime.now().strftime("%B %d, %Y")
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    c.execute("INSERT INTO posts (author, title, content, date) VALUES (?, ?, ?, ?)",
              (author, title, content, date))
    conn.commit()
    conn.close()
    return redirect(url_for('discussions'))

@app.route('/add_reply/<int:post_id>', methods=['POST'])
@login_required
def add_reply(post_id):
    author = request.form['author']
    content = request.form['content']
    date = datetime.now().strftime("%B %d, %Y")
    conn = sqlite3.connect('forum.db')
    c = conn.cursor()
    c.execute("INSERT INTO replies (post_id, author, content, date) VALUES (?, ?, ?, ?)",
              (post_id, author, content, date))
    conn.commit()
    conn.close()
    return redirect(url_for('discussions'))

# Test route for email sending
@app.route('/test_email')
def test_email():
    try:
        msg = Message("Test Email", recipients=['your_email@gmail.com'])
        msg.body = "This is a test email from Flask-Mail."
        mail.send(msg)
        return "Email sent!"
    except Exception as e:
        logging.error('Error sending test email: %s', str(e))
        return f"Failed to send email. Error: {str(e)}"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure secret key

# Configuration for Flask-Mail (Optional: Uncomment and configure if you want to send emails)
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
# app.config['MAIL_PASSWORD'] = 'your_email_password'
# mail = Mail(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/skills")
def skills():
    return render_template("skills.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        
        # Optional: Send email using Flask-Mail
        """
        try:
            msg = Message("New Contact Form Submission",
                          sender=email,
                          recipients=["khribech.chouaib@gmail.com"])
            msg.body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash("An error occurred while sending your message. Please try again later.", "danger")
        """
        
        # For now, we'll just flash a success message
        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

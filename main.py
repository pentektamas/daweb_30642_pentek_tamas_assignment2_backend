from flask import Flask
from flask_cors import CORS
from flask_mail import Mail, Message
from flask import request
import pandas as pd

app = Flask(__name__)
app.secret_key = 'secretKey'
app.config.update(dict(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME='pentek.tomy@gmail.com',
    MAIL_PASSWORD='tljzdqohwlxkwmuu'
))
CORS(app)

mail = Mail(app)


@app.route('/contactUsEmail', methods=["GET", "POST"])
def get_contact():
    global ind
    data = request.get_json()
    if request.method == 'POST':
        msg = Message('Test Email', sender='test@gmail.com', recipients=[data['email']])
        msg.body = 'Dear ' + str(data[
                                     'name']) + ",\n\nThank you for the email. We will answer as soon as possible.\nIt's an auto generated email.\nPlease don't answer!\n\n Best regards,\n DentaWEB Team"
        msg.subject = str(data['subject']) + ' Response'
        mail.send(msg)
        res = pd.DataFrame(
            {'name': data['name'], 'email': data['email'], 'subject': data['subject'], 'message': data['message']},
            index=[0])
        res.to_csv('./incomingMessages.csv', mode='a', index=False, header=False)
        return "Success"
    else:
        return "Error"


if __name__ == '__main__':
    app.run(debug=True)

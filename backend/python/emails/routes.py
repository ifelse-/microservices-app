from flask import Flask, request, jsonify, Blueprint
from sendmail import EmailSender
emails_blueprint = Blueprint('emails_api_routes', __name__, url_prefix='/api/emails')


@emails_blueprint.route('/process', methods=['GET'])
def index():
    return "hello it's working"


@emails_blueprint.route('/send', methods=['POST'])
def process_email():
    email_data = request.json  # Get email data from the POST request
    print(email_data)
    # Process the email here
    email_sender = EmailSender()

    # Specify the recipient email, subject, and message
    recipient_email = 'marvin@giveme5ive.com'
    subject = 'Your Subject'
    message = 'This is the body of your email.'

    # Send the email
    email_sender.send_email(recipient_email, subject, message)
    # You can access email attributes like subject, body, recipient, etc., in 'email_data'
    # Implement your email processing logic here
    return jsonify({'message': 'Email processed successfully'})

from selenium import webdriver
from flask import Flask, render_template


# Create a Flask application instance
app = Flask(__name__)

# Start a browser instance
driver = webdriver.Chrome()


# Set up a route to interact with the button
@app.route('/')
def test_button():
    server_url = "https://ticketsales.dev/auth/signup"  # Replace with your server's URL
    driver.get(server_url)  # Your Flask app's URL
    button = driver.find_element_by_id('testButton')
    button.click()
    return 'Button clicked'


if __name__ == '__test__':
    app.run()

from selenium import webdriver
from flask import Flask, render_template


# Create a Flask application instance
app = Flask(__name__)

# Start a browser instance
driver = webdriver.Chrome()


# Set up a route to interact with the button
@app.route('/test_button')
def test_button():
    driver.get('http://127.0.0.1:5001')  # Your Flask app's URL
    button = driver.find_element_by_id('testButton')
    button.click()
    return 'Button clicked'


if __name__ == '__test__':
    app.run()
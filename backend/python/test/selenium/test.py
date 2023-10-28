from selenium import webdriver
from flask import Flask, render_template


# Create a Flask application instance
app = Flask(__name__)


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

server_url = "https://ticketsales.dev/"  # Replace with your server's URL
driver.get(server_url)  # Your Flask app's URL
# Set up a route to interact with the button

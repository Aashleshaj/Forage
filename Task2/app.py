from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the main route (the homepage)
@app.route('/')
def home():
    return "<h1>Hello, Flask!</h1><p>This is my first Flask application.</p>"

# Define a second route to show how routing works
@app.route('/about')
def about():
    return "<h2>About Page</h2><p>Flask is a lightweight web framework.</p>"

# Run the server
if __name__ == '__main__':
    # debug=True allows the server to auto-reload when you make code changes
    app.run(debug=True)
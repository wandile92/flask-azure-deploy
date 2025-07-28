from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask! This is my Cloud Deployment on Azure."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) # Azure App Service often uses 8000 or 80.

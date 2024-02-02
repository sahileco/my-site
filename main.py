from flask import Flask, render_template
import os

app = Flask(__name__)

# Get the absolute path of the 'templates' folder
template_folder = os.path.abspath('templates')
app = Flask(__name__, template_folder=template_folder)

@app.route('/')
def home():
    try:
        return render_template('sahil')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)

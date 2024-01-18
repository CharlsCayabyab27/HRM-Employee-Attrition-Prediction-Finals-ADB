from flask import Flask, render_template
from nbconvert.exporters import HTMLExporter
import nbformat
from flask_socketio import SocketIO
from tensorflow.keras.models import load_model
import joblib
import mysql.connector

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Load the trained model
model = load_model('model.h5')

# Compile the model with necessary configurations
# model.compile(optimizer=..., loss=..., metrics=[...])

# Load one-hot encoder
try:
    with open('OneHotEncoder.joblib', 'rb') as file:
        one_hot_encoder = joblib.load(file)
except FileNotFoundError:
    # Handle the case where the OneHotEncoder file is not found
    print("Error: OneHotEncoder.joblib not found.")
    one_hot_encoder = None  # Set to None or handle appropriately

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'aaa'
}

@app.route('/jupyter')
def jupyter():
    notebook_path = 'aaaaa.ipynb'

    try:
        with open(notebook_path, 'r', encoding='utf-8') as f:
            notebook_content = nbformat.read(f, as_version=4)

        html_exporter = HTMLExporter()
        html_body, _ = html_exporter.from_notebook_node(notebook_content)

        return render_template('jupyter.html', notebook_html=html_body)
    except Exception as e:
        # Handle errors, e.g., notebook not found or invalid format
        return f'Error: {e}', 404

if __name__ == '__main__':
    app.run(debug=True)

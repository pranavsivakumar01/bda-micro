from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)


file_path = r'datasets/NikeProductDescriptions.csv'
data = pd.read_csv(file_path)

@app.route('/search', methods=['POST'])
def search_product():
    title = request.json.get('title', '')
    result = data[data['Title'].str.contains(title, case=False, na=False)]
    if not result.empty:
        return jsonify(result.to_dict(orient='records'))
    else:
        return jsonify([])

if __name__ == '__main__':
    app.run(port=5000)

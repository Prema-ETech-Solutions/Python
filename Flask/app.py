from flask import Flask , jsonify ,request
import csv
import codecs


app = Flask(__name__)


# Base return test
@app.route('/')
def test():
    return 'Good to Go ....'

# End point 01
@app.route('/Go')
def Go():
    return 'Go'

# query parameters
# http://127.0.0.1:5000/query?user=question
@app.route('/query')
def query():
    user = request.args.get('user')
    return jsonify({"user" :user }) 


# path parameters
# http://127.0.0.1:5000/path/2/1/
@app.route('/path/<int:val>/<int:val1>/')
def path(val,val1):
    return jsonify({"value1": val,"value2": val1,"sum": val+val1,"sub": val-val1,"mul": val*val1,"div": val/val1, }) 


# Post  with json
# http://127.0.0.1:5000/post_json

# {
#   "id": 10,
#   "title": "HP Pavilion 15-DK1056WM",
#   "description": "HP Pavilion 15-DK1056WM Gaming...",
#   "price": 1099,
#   "discountPercentage": 6.18,
#   "rating": 4.43,
#   "stock": 89,
#   "brand": "HP Pavilion",
#   "category": "laptops",
#   "thumbnail": "https://i.dummyjson.com/data/products/10/thumbnail.jpeg",
#   "images": [
#     "https://i.dummyjson.com/data/products/10/1.jpg",
#     "https://i.dummyjson.com/data/products/10/2.jpg",
#     "https://i.dummyjson.com/data/products/10/3.jpg",
#     "https://i.dummyjson.com/data/products/10/thumbnail.jpeg"
#   ]
# }
@app.route('/post_json', methods=['POST'])
def process_json():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

# Post Csv

@app.route('/csv', methods=['POST'])
def csv_Read():
    print("Enter")
    flask_file = request.files['file']
    if not flask_file:
        return 'Upload a CSV file'
    

    data = []
    stream = codecs.iterdecode(flask_file.stream, 'utf-8')
    for row in csv.reader(stream, dialect=csv.excel):
        if row:
            data.append(row)
            
    return jsonify(data)
    # return "Err"
    


if __name__ == '__main__':
    app.run(debug=True)
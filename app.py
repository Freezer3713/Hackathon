from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from all_functions import get_course_info, get_grade_data, prof_rating, print_course_info

app = Flask(__name__, static_folder="./static", static_url_path="/static")
CORS(app)

@app.route('/')
def index():
    return render_template('Hackathon.html')

@app.route('/api/prof_rating/<prof_name>', methods=['GET'])
def api_prof_rating(prof_name):
    # Assuming prof_name is provided as a URL parameter
    result = prof_rating(prof_name)
    return jsonify(result)

@app.route('/api/get_grade_data', methods=['POST'])
def api_get_grade_data():
    data = request.json
    course_name = data.get('course_name')  # Adjust based on how you send data from frontend
    result = get_grade_data(course_name)
    return jsonify(result)

@app.route('/api/get_course_info', methods=['POST'])
def api_get_course_info():
    data = request.json
    subject = data.get('subject')  # Adjust based on how you send data from frontend
    class_code = data.get('class_code')  # Adjust based on how you send data from frontend
    result = get_course_info(subject, class_code)
    return jsonify(result)

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)

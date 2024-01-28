from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from functions_all import get_course_info, print_course_info, get_grade_data, prof_rating

import pprint

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    
    return render_template('Hackathon.html')


@app.route('/api/prof_rating/<prof_name>')
def api_prof_rating(prof_name):
    print(prof_name)
    #data = request.json
    '''
    print('======')
    pprint.pprint(data)
    prof_name = data['prof_name']
    result = prof_rating(prof_name)
    return jsonify(result)
    '''
    return prof_name

@app.route('/api/get_grade_data', methods=['POST'])
def api_get_grade_data():
    data = request.json
    course_name = data['course_name']
    result = get_grade_data(course_name)
    return jsonify(result)

@app.route('/api/get_course_info', methods=['POST'])
def api_get_course_info():
    data = request.json
    subject = data['subject']
    class_code = data['class_code']
    result = get_course_info(subject, class_code)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)


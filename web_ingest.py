from flask import jsonify

from flask import Flask

from tasks.tasks import status, create_new

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379'
app.config['CELERY_RESULT_EXPIRES'] = 20
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Cyber Scan</h1><p>Home Page TEST.</p>'''

# http://127.0.0.1:5000/api/v1/resources/status/<scan_id>
@app.route('/api/v1/resources/status/<scan_id>', methods=['GET'])
def get_status(scan_id):
    return jsonify(status(scan_id)), 200


# http://127.0.0.1:5000/api/v1/resources/newscan
# for simplicity using GET , not POST
@app.route('/api/v1/resources/newscan', methods=['GET'])
def new_scan():
    scan = create_new.delay()
    return jsonify({"task_id": scan.id}), 202

app.run()

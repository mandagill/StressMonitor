from flask import Flask, render_template, session, request, jsonify
import time
import pdb
import fitbit
import celery_worker

app = Flask(__name__)
app.secret_key = "thisisakeyfortestpurposesNOT-THE-PROD-KEY"
# TODO how to put a timeout on the session? E.g. if no interaction from the user for an hour, turn it off?
# Possibly prompt the user with an "are you still there?" message
app.config.update(
	CELERY_BROKER_URL='redis://localhost:6379',
    CELERY_RESULT_BACKEND='redis://localhost:6379'
)

celery = celery_worker.make_celery(app)


@app.route("/")
def index():
	
	return render_template("landing.html")


@app.route("/begin_tracking", methods=['POST'])
def begin_tracking():
	# request.form is a dictionary
	if request.form.get('message') == "Turn the tracking on plz kthx":
		session['tracking_status'] = 1

	response_msg = {'response_msg': "tracking is enabled!"}

	track_variance()

	return jsonify(response_msg)


@app.route("/stop_tracking", methods=['POST'])
def stop_tracking():
	if request.form.get('message') == "Okay now stop!":
		session['tracking_status'] = 0

	response_msg = {'response_msg': "tracking has been disabled"}

	print response_msg
	return jsonify(response_msg)


@app.route("/fitbit-input")
def consume_api():
	"""This is just a stub to take the FitBit data until I wire 
	the HR stream up to something interesting """
	pass


@celery.task()
def track_variance():

	while session['tracking_status'] == 1:
		time.sleep(10)
		print "Tracking status is: ", session['tracking_status']
	# pdb.set_trace()


def main():
	pass


if __name__ == "__main__":
	app.run(debug=True)


from flask import Flask, render_template, session, request, jsonify
import time
import pdb
import fitbit

app = Flask(__name__)
app.secret_key = "thisisakeyfortestpurposesNOT-THE-PROD-KEY"
# TODO how to put a timeout on the session? E.g. if no interaction from the user for an hour, turn it off?
# Possibly prompt the user with an "are you still there?" message


@app.route("/")
def index():
	
	return render_template("landing.html")


@app.route("/begin_tracking", methods=['POST'])
def begin_tracking():
	# request.form is a dictionary
	if request.form.get('message') == "Turn the tracking on plz kthx":
		session['tracking_status'] = 1

	response_msg = {'response_msg': "tracking is enabled!"}

	print jsonify(response_msg)
	return jsonify(response_msg)


@app.route("/stop_tracking", methods=['POST'])
def stop_tracking():
	if request.form.get('message') == "Okay now stop!":
		session['tracking_status'] = 0

	response_msg = {'response_msg': "tracking has been disabled"}

	print response_msg
	return jsonify(response_msg)


@app.route("/track_variance")
def track_variance():

	# This makes the page hang and I can't click the stop-tracking button any longer
	while session['tracking_status'] == 1:
		time.sleep(10)
		print "Tracking status is: ", session['tracking_status']
	# pdb.set_trace()


def main():
	pass


if __name__ == "__main__":
	app.run(debug=True)


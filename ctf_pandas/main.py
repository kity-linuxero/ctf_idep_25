from flask import Flask, request, jsonify, send_from_directory
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)

# The secret flag is now stored on the server
SECRET_FLAG = "427567426f756e74794769726c73436c7562"

@app.route('/')
def index():
    # Serve the main ctf2.html file
    return send_from_directory('.', 'ctf2.html')

@app.route('/verificar', methods=['POST'])
def verify_flag():
    """
    This endpoint verifies the win condition.
    The client must send a JSON payload like: {"bamboo": 280}
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid request. Expected JSON."}), 400

    bamboo_amount = data.get('bamboo')

    # Securely check the win condition on the server
    if bamboo_amount == 280:
        return jsonify({"flag": SECRET_FLAG})
    else:
        return jsonify({"error": "Win condition not met."}), 403

# This is the new root application that will handle the /pandas prefix
application = DispatcherMiddleware(Flask('dummy_app'), {
    '/pandas': app
})

if __name__ == '__main__':
    # Use 0.0.0.0 to be accessible within the Docker container
    # We run the 'application' object, not the 'app' object
    run_simple('0.0.0.0', 8080, application, use_reloader=True, use_debugger=True)
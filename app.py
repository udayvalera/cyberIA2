from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# Define the route and method
@app.route('/api/greet', methods=['GET'])
def greet_user():
    # Fetch the 'name' parameter from the query string, default to 'Guest'
    user_name = request.args.get('name', 'Guest')
    # Create the response message
    response_message = {"message": f"Hello, {user_name}!"}
    # Return the response as JSON
    return jsonify(response_message)

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)

from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Hello World with Webhook
    ---
    responses:
      200:
        description: Returns a Hello World message
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Hello World with Webhook"
    """
    return jsonify({"message": "Hello World with Webhook"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
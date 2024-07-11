from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Define accounts
accounts = {
    "main_account": {
        "account_id": "10000000000000000000000000000000000000000000000000000000000",
        "balance": 1000000000000000000000000000000000000000000000000000000000 
    },
    "target_account": {
        "account_id": "1976278463",
        "balance": 0
    }
}

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/send', methods=['POST'])
def send_money():
    data = request.get_json()
    amount = data['amount']
    if accounts["main_account"]["balance"] >= amount:
        accounts["main_account"]["balance"] -= amount
        accounts["target_account"]["balance"] += amount
        return jsonify({
            "message": "Transaction successful",
            "main_account_balance": accounts["main_account"]["balance"],
            "target_account_balance": accounts["target_account"]["balance"]
        })
    else:
        return jsonify({
            "message": "Insufficient funds",
            "main_account_balance": accounts["main_account"]["balance"],
            "target_account_balance": accounts["target_account"]["balance"]
        }), 400

if __name__ == '__main__':
    app.run(debug=True)

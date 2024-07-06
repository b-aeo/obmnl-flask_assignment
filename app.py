from flask import Flask, request, jsonify, url_for, redirect, render_template

# Instantiate Flask functionality

app = Flask("fin_transactions")

# Sample data

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation

@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions = transactions)

# Create operation

@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")

    elif request.method == "POST":

        transaction = {
            "id" : len(transactions) + 1
            "date" : request.form[date]
            "amount" : request.form[amount]
        }
        transactions.append(transaction)
        return redirect(url_for(get_transactions))

# Update operation

@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
def edit_transaction(add_transaction_id):
    if request.method == "GET":
        for dic in transactions:
            if add_transaction_id in dic.values():
                return render_template("edit.html", transaction=transaction)
    
    elif request.method == "POST":
        counter = 0
         for dic in transactions:
            if add_transaction_id in dic.values():
                transaction = {
                "id" : len(transactions) + 1
                "date" : request.form[date]
                "amount" : request.form[amount]
            }
                transactions[counter] = transaction
                return redirect(url_for(get_transactions))
            
            counter += 1

# Delete operation



# Run the Flask app
    
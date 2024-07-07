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
    balance = 0
    for dic in transactions:
        balance += dic.get("amount")
    return render_template("transactions.html", transactions = transactions, total_balance = balance)

# Create operation

@app.route("/add", methods = ["GET", "POST"])
def add_transaction():
    if request.method == "GET":
        return render_template("form.html")

    elif request.method == "POST":

        transaction = {
            "id" : len(transactions) + 1,
            "date" : request.form["date"],
            "amount" : request.form["amount"]
        }
        transactions.append(transaction)
        return redirect(url_for("get_transactions"))

# Update operation

@app.route("/edit/<int:transaction_id>", methods = ["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "GET":
        for dic in transactions:
            if transaction_id in dic.values():
                return render_template("edit.html", transaction=dic)
    
    elif request.method == "POST":
        counter = 0
        for dic in transactions:
            if transaction_id in dic.values():
                transaction = {
                "id" : len(transactions) + 1,
                "date" : request.form["date"],
                "amount" : request.form["amount"]
                }
                transactions[counter] = transaction
                return redirect(url_for("get_transactions"))
            
            counter += 1

# Delete operation

@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    counter = 0
    for dic in transactions:
        if transaction_id in dic.values():
            del transactions[counter]
            return redirect(url_for("get_transactions"))
        counter += 1


## Search Transactions

@app.route("/search", methods = ["GET", "POST"])
def search_transactions():
    if request.method == "POST":
        min1 = float(request.form["min_amount"])
        max2 = float(request.form["max_amount"])
        filtered_transactions = []
        for dic in transactions:
            if min1 <= float(dic.get("amount")) <= max2:
                filtered_transactions.append(dic)
        return render_template("transactions.html", transactions = filtered_transactions)
    elif request.method == "GET":
        return render_template("search.html")

## Total balance feature

@app.route("/balance")
def total_balance():
    balance = 0
    for dic in transactions:
        balance += dic.get("amount")
    return str(f"Total Balance : {balance}")


# Run the Flask app
    
if __name__ == "__main__":
    app.run(debug = True)



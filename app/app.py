from flask import Flask, render_template, request

app = Flask(__name__)

# Launch Page-------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user_input=None)

# Prescription View Page--------------------------------------------
@app.route('/prescription', methods=['GET', 'POST'])
def prescription():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('prescription.html', user_input=user_input)
    return render_template('prescription.html', user_input=None)

# Inventory View Page----------------------------------------------
@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    # if request.method == 'POST':
    #     user_input = request.form['user_input']
    #     return render_template('inventory.html', user_input=user_input)
    return render_template('inventory.html', user_input=None)

# Supply Order View Page--------------------------------------------
@app.route('/supply', methods=['GET', 'POST'])
def supply():
    return render_template('supply.html', user_input=None)


if __name__ == '__main__':
    app.run(debug=True)

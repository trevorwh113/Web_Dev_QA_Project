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

# Client View Page--------------------------------------------
@app.route('/prescription/client', methods=['GET', 'POST'])
def client():
    if request.method == 'POST':
        return render_template('client.html')
    return render_template('client.html')

# Prescription Creation View Page--------------------------------------------
@app.route('/prescription/client/pre-creation', methods=['GET', 'POST'])
def pre_creation():
    if request.method == 'POST':
        user_input = [request.form['dname'],
                      request.form['DIN'],
                      request.form['dosage'],
                      request.form['preBy'],
                      request.form['interval']]
        return render_template('client.html')
    return render_template('create_prescription.html')

# Inventory View Page----------------------------------------------
@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('inventory.html', user_input=user_input)
    return render_template('inventory.html', user_input=None)

# Supply Order View Page--------------------------------------------
@app.route('/supply', methods=['GET', 'POST'])
def supply():
    return render_template('supply.html', user_input=None)


if __name__ == '__main__':
    app.run(debug=True)

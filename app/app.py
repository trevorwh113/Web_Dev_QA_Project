from flask import Flask, render_template, request
import utility
from client import Client

app = Flask(__name__)

# Launch Page-------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user_input=None)

# Prescription View Page--------------------------------------------
@app.route('/prescription', methods=['GET', 'POST'])
def prescription():
    # Backend link to get the data.
    data = utility.get_all_clients()

    # Filter data set according to user's search parameters.
    if request.method == 'POST':
        try:
            par = request.form['search_par']
        except:
            par = None
        data = utility.filter_clients(data, par)

    # Renders the page.
    return render_template('prescription.html', data=data)


# Client View Page--------------------------------------------
@app.route('/prescription/client', methods=['GET', 'POST'])
#will prolly have client pushed through from other page so client(client): and data will be easier
def client():
    # Backend link to get the data.
    client = utility.get_all_clients()[0]
    data = [client.active_prescripts, client.old_prescripts]
    # Render"s the page.
    return render_template('client.html', data=data)

# Prescription Creation View Page--------------------------------------------
@app.route('/prescription/client/pre-creation', methods=['GET', 'POST'])
def pre_creation():
    if request.method == 'POST':
        user_input = request.form['user_input']
        return render_template('create_prescription.html', user_input=user_input)
    return render_template('create_prescription.html', user_input=None)

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

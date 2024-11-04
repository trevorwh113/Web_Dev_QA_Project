"""
The main control flow of the app. Bridges between the backend link
and the front end UI (html/css/js).
"""

from flask import Flask, render_template, request, jsonify
import utility
from client import Client

app = Flask(__name__)

# Launch Page-------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html', user_input=None)


# Clients Search Page--------------------------------------------
@app.route('/clients', methods=['GET', 'POST'])
def clients():
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
    return render_template('clients_search.html', data=data)

# Clients Information Page---------------------------------------------
@app.route('/clients/<phone_number>', methods=['GET', 'POST'])
def clients_info(phone_number):
    # Backend link to get the data about the client.
    client = utility.get_client_by_phone(phone_number)
    # Renders the page.
    return render_template('clients_info.html', client=client)

# Clients Prescription Creation Page-------------------------------------
@app.route('/clients/<phone_number>/create', methods=['GET', 'POST'])
def clients_create(phone_number):
    if request.method == 'POST':
        # Backend link to save the data....
        user_input = [int(request.form['DIN']),
                      request.form['preBy'],
                      request.form['refill']]
        entry = utility.valid_drug(user_input[0])
        if(entry != None):          
            utility.save_new_prescription(phone_number, user_input, entry)
            # Reloads the client's information page.
            return clients_info(phone_number)
        else:
            return render_template('clients_create.html', phone_number=phone_number, alert=True)
    return render_template('clients_create.html', phone_number=phone_number, alert=False)

  
# Inventory Search Page----------------------------------------------
@app.route('/inventory', methods=['GET', 'POST'])
def inventory_search():
    # Backend link to get the data.
    data = utility.get_all_inv()

    # Filter data set according to user's search parameters.
    if request.method == 'POST':
        try:
            par = request.form['search_par']
        except:
            par = None
        data = utility.filter_inv(data, par)

    # Renders the page.
    return render_template('inventory_search.html', data=data)

# Inventory Information Page ---------------------------------------------
@app.route('/inventory/<din>', methods=['GET', 'POST'])
def inventory_info(din):
    return render_template('inventory_info.html', din=din)


# Supply Order View Page--------------------------------------------
@app.route('/supply', methods=['GET', 'POST'])
def supply():
    return render_template('supply.html', user_input=None)

################################################################
@app.route('/update_list', methods=['POST'])
def update_lists():
    data = request.get_json() # retrieve the data sent from JavaScript
    # process the data using Python code
    phone = data['id']
    actives = data['active']
    olds = data['old']

    utility.update_prescriptions(phone, actives, olds)
    return jsonify(result=phone)

if __name__ == '__main__':
    app.run(debug=True)

"""
The main control flow of the app. Bridges between the backend link
and the front end UI (html/css/js).
"""

from flask import Flask, render_template, request
import utility

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
    # if request.method == 'POST':
    #     try:
    #         par = request.form['search_par']
    #     except:
    #         par = None
    #     data = utility.filter_inv(data, par)

    # Renders the page.
    return render_template('prescription.html', data=data)

# Client Prescription Page---------------------------------------------
@app.route('/prescription/<phone_number>', methods=['GET', 'POST'])
def client_pres_page(phone_number):
    return render_template('client_pres_page.html', phone_number=phone_number)


# Inventory View Page----------------------------------------------
@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
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
    return render_template('inventory.html', data=data)

# Drug Information Page---------------------------------------------
@app.route('/inventory/<din>', methods=['GET', 'POST'])
def drug_info_page(din):
    return render_template('drug_info_page.html', din=din)


# Supply Order View Page--------------------------------------------
@app.route('/supply', methods=['GET', 'POST'])
def supply():
    return render_template('supply.html', user_input=None)


if __name__ == '__main__':
    app.run(debug=True)

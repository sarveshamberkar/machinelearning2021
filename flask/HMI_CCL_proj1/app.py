from flask import Flask, render_template, request, redirect, url_for
from firebase import firebase
app = Flask(__name__)
f_base = firebase.FirebaseApplication('https://be-ccl-miniproject-default-rtdb.firebaseio.com/', None)


@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')


@app.route('/track', methods=['GET', 'POST'])
def track():
    return render_template('track.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    name = ''
    unique_id = ''
    status = 0
    if request.method == 'POST':
        unique_id = request.form['UniqueID']
        status = 1
        print(unique_id)
        content = f_base.get('be-ccl-miniproject-default-rtdb/complaint',unique_id)
        print(content)
        return render_template('track.html', status=status,unique_id=unique_id)
    else:
        return render_template('track.html')


@app.route('/donedisplay', methods=['POST', 'GET'])
def donedisplay():
    if request.method == 'POST':
        f_name = request.form['firstname']
        l_name = request.form['lastname']
        address = request.form['q4_address4[addr_line1]']
        street_address = request.form['q4_address4[addr_line2]']
        city_address = request.form['q4_address4[city]']
        phone = request.form['q5_phoneNumber5[full]']
        e_email = request.form['q6_email6']
        crime_type = request.form['q8_howDid8']
        complaint_details = request.form['q11_feedbackAbout11']
        suspect_details = request.form['q12_suggestionsIf']
        data = {
            'f_name': f_name,
            'l_name': l_name,
            'address': address,
            'street_address': street_address,
            'city_address': city_address,
            'phone': phone,
            'email': e_email,
            'crime_type': crime_type,
            'complaint_details': complaint_details,
            'suspect_details': suspect_details
        }
        f_base.post('be-ccl-miniproject-default-rtdb/complaint',data)
        database = f_base.get('be-ccl-miniproject-default-rtdb/complaint','')
        to_get_key = ''
        print(database)
        for key,data in database.items():
            if (data['f_name']==f_name) and (data['l_name']==l_name) and(data['phone']==phone):
                to_get_key = key
                break


    return render_template('Thank You.html',tracking_no = to_get_key)


@app.route('/complaint', methods=['POST', 'GET'])
def complaint():
    return render_template('New_Customer_Registration_Form.html')


if __name__ == '__main__':
    app.run(debug=True)

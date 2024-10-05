from flask import Flask, request, url_for, render_template, flash, session, redirect

from appointment import Appointment
from customer import Customer
from service import ALL_SERVICES
import datetime
from schedule import Schedule

app = Flask(__name__)
app.secret_key = "iFXoraNd"    

# globals
CURRENT_DATE = datetime.datetime.now().date()
MAXIMUM_BOOK_DATE = CURRENT_DATE + datetime.timedelta(days=60)
WORKING_HOURS = [
    "10:00 - 11:45", "11:45 - 12:30", "12:30 - 13:15",
    "13:15 - 14:00", "14:00 - 14:45", "14:45 - 15:30"
]

@app.route("/")
def home():
    # default sessions
    session['logged-in'] = False
    session['customer'] = None
    return render_template("home.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        fname, lname, phoneNum, email, address, username, password = request.form['firstName'], request.form['lastName'], request.form['phoneNumber'], request.form['email'], request.form['address'], request.form['username'], request.form['password']
        AddCustomer(fname, lname, phoneNum, email, address)
        AddUser(username, password)
        customer_obj = Customer(fname, lname, email, phoneNum, address)
        CloseDatabase()
        cust_num = getCustomerNumber(customer_obj)[0]
        CloseDatabase()
        # customer dictionary object
        cust_dict = {'ID': cust_num,'fname': fname, 'lname': lname, 'email': email, 'phone': phoneNum, 'address': address}
        session['logged-in'] = True
        session['customer'] = cust_dict
        session['user'] = {'username':username, 'password':password}
        return redirect(url_for("BookAppointment", name=f"{fname.capitalize()} {lname.capitalize()}"))
    else:
        return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    errorMessage = "provide correct login credentials."
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        User = Login(username, password)
        cust_num = getCustomerNumber(User)[0]
        fname, lname, email, phone, address = User.first_name, User.last_name, User.email, User.phoneNum, User.address
        CloseDatabase()
        # customer dict
        cust_dict = {'ID': cust_num,'fname': fname, 'lname': lname, 'email': email, 'phone': phone, 'address': address}
        if User:
            session['logged-in'] = True
            session['customer'] = cust_dict
            session['user'] = {'username': username, 'password': password}
            return redirect(url_for("popup", name=f"{User.first_name.capitalize()} {User.last_name.capitalize()}"))
        return render_template("login.html", errorMessage=errorMessage)
    else:
        flash("Provided incorrect Username or password. Try Again :(")
        return render_template("login.html", errorMessage=errorMessage)
    
    
@app.route("/BookAppointment", methods=["GET", "POST"])
def BookAppointment():
    if session['logged-in']:
        if request.method == "POST":
            schedule_date = request.form['schedule_date']
            schedule_time = request.form['schedule_time']
            service_num = int(request.form['service'])
            schedule = Schedule(schedule_date, schedule_time)
            cust_num, fname, lname, email, phone, address = session['customer'].get('ID'), session['customer'].get('fname'), session['customer'].get('lname'), session['customer'].get('email'), session['customer'].get('phone'), session['customer'].get('address')
            customer = Customer(fname, lname, email, phone, address)
            appointment = Appointment(schedule, cust_num, service_num)
            AddAppointmentRequest(appointment, cust_num)
            
            return redirect(url_for("booking_sucessful"))
        else:
            username = session['user'].get('username')
            return render_template("booking.html", services=ALL_SERVICES,
                current_date=CURRENT_DATE, max_book_date=MAXIMUM_BOOK_DATE,
                working_hours=WORKING_HOURS, username=username)
    else:
        return redirect(url_for("login"))


@app.route("/popup<name>", methods=["GET", "SET"])
def popup(name):
    return render_template("popup.html", username=name)
    
    
@app.route("/view_appointments")
def view_appointments():
    return render_template("view_appointments.html")

@app.route("/base")
def base():
    return render_template("base.html")

@app.route("/About")
def about():
    return render_template("about.html")

@app.route("/Services")
def services():
    return render_template("services.html")

@app.route("/Contact")
def contact():
    return render_template("contact.html")

@app.route("/booked_sucessfully")
def booking_sucessful():
    return render_template("booking_sucessful.html")

if __name__ == "__main__":
    app.run(debug=False)

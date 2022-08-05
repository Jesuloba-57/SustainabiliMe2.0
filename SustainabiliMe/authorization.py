from flask import Blueprint, render_template, request, flash, redirect, url_for
from .db_model import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from .transAPI import Transport
from .recycle import Recycle
from geopy.geocoders import Nominatim

auth = Blueprint('auth', __name__)

@auth.route("/")
@auth.route('/landing')
def landing():
    return render_template('L_page.html')


@auth.route("/")
@auth.route('/home')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('auth.landing'))
    else:
        return render_template('home.html')
    
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if not user:
            flash('Email does not exist.', category='error')
            return render_template('login.html') 
            # user=current_user
        if not check_password_hash(user.password, password):
            flash('Incorrect password, try again.', category='error')
            return render_template('login.html') 
        
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return render_template('home.html')
    
    return render_template('login.html')
        # else:
        #     flash('Incorrect password, try again.', category='error')
        # # else:
        #     flash('Email does not exist.', category='error')

    # return render_template('login.html', user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.landing'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        user_name = request.form.get('userName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(user_name) < 2:
            flash('Username must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        else:
            new_user = User(email=email, user_name=user_name, 
                            password=generate_password_hash(password1, method='pbkdf2:sha1', salt_length=8))
            db.session.add(new_user)
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            db.session.commit()
            return(redirect(url_for('auth.login')))

    return render_template('sign_up.html', user=current_user)


# @auth.route("/")
@auth.route("/recycle", methods=['GET', 'POST'])
@login_required
def recycle():
    if request.method == "POST":
        item = request.form["item"]
        zipcode = request.form["zipcode"]
        locations = Recycle(zipcode, item)
        results = locations.get_locations()
        geolocator = Nominatim(user_agent="my-application-default")
        if results == -1:
            flash('Sorry, item not found', category='error')
        if results == -2:
            flash('Incorrect Zipcode. Try again!', category='error')
        else:
            if len(results) > 10:
                results = results[:10]
            for i in results:
                loc_lat = str(i['latitude'])
                loc_long = str(i['longitude'])
                coords = loc_lat + ", " + loc_long
                location = geolocator.reverse(coords)
                i['address'] = location
            return render_template('recycle_result.html', results=results)
    return render_template('recycle.html')


# @auth.route("/")
@auth.route("/transport", methods=['GET', 'POST'])
@login_required
def transportation():
    if request.method == "POST":
        src = request.form["usersrc"]
        dest = request.form["userdest"]
        path = Transport(src, dest)
        subtitle = f"Open Routes from {src} to {dest}"
        if path.get_transit() == "No route found.":
            subtitle = f"The are no routes from {src} to {dest} available at the moment."
            return render_template('transport_result.html', subtitle=subtitle)
        transport, destinations, total_times, final_times = path.get_transit()
        contents = {"transport": transport, "destination": destinations, "total": total_times, "final": final_times}
        return render_template('transport_result.html', subtitle=subtitle, contents=contents)
    return render_template('transport.html')
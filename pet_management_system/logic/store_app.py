from flask import Flask, render_template, request, flash, redirect, url_for

from pet_management_system.logic.pet import Pet

app = Flask(__file__)


@app.route('/')
def home():
    return render_template('store_home.html')


@app.route('/owners')
def owners():
    pass


@app.route('/add_owner')
def add_owner():
    pass


@app.route('pets')
def pets():
    pass


@app.route('/add_pet', methods=['POST'])
def add_pet():
    name = request.form['name']
    species = request.form['species']
    age = request.form['age']
    owner = request.form['owner']
    vaccinated = bool(request.form['vaccinated'])

    if not name or not species or not age or not owner or not vaccinated:
        flash("All fields are required.")
        return redirect(url_for('add_pet'))

    pet = Pet(name, species, age, owner, vaccinated)


@app.route('services')
def services():
    pass

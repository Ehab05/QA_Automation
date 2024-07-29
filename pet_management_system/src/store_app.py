from flask import Flask, render_template, request, flash, redirect, url_for

from pet_management_system.src.classes.pet import Pet

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


@app.route('/pets')
def pets():
    pass


@app.route('/add_pet', methods=['GET', 'POST'])
def add_pet():
    if request.method == 'POST':
        name = request.form['name']
        species = request.form['species']
        age = request.form['age']
        owner = request.form['owner']
        vaccinated = bool(request.form['vaccinated'])

        if not name or not species or not age or not owner or not vaccinated:
            flash("All fields are required.")
            return redirect(url_for('add_pet'))

        try:
            age = int(age)
        except ValueError:
            flash("Age must be a number.")
            return redirect(url_for('add_pet'))

        if not species.isalpha():
            flash("Species must contain only letters.")
            return redirect(url_for('add_pet'))

        pet = Pet(name, species, age, owner, vaccinated)
        flash("Pet added successfully!")
        return render_template('add_pet.html')
    return render_template('add_pet.html')


@app.route('/services')
def services():
    pass


if __name__ == '__main__':
    app.run(debug=True)

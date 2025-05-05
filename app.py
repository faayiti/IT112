from flask import Flask, render_template
from models import db, Car  # Import your db and Car model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cars.db'  # Path to SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable Flask-SQLAlchemy modification tracking
db.init_app(app)  # Initialize SQLAlchemy with your Flask app

# This decorator ensures the database is set up only once before the first request
@app.before_request
def create_tables():
    if not hasattr(app, 'has_run'):  # Run only once
        db.create_all()  # Create the database tables
        if Car.query.count() == 0:  # If there are no cars, populate the database
            cars = [
                Car(make="Nissan", model="Altima", year=2024),
                Car(make="Toyota", model="Corolla", year=2024),
                Car(make="BMW", model="X5", year=2024)
            ]
            db.session.add_all(cars)  # Add the cars to the database
            db.session.commit()  # Commit the changes
        app.has_run = True  # Mark that the setup has been done, so it doesn't run again

# Route to display the list of cars
@app.route('/')
def index():
    cars = Car.query.all()  # Query all the cars from the database
    return render_template('index.html', cars=cars)

# Route to show details for a specific car
@app.route('/car/<int:car_id>')
def car_detail(car_id):
    car = Car.query.get_or_404(car_id)  # Get the car by its ID, or show 404 if not found
    return render_template('detail.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)

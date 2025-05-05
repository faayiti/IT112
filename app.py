from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learners.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Learner model
class Learner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(50), nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'location': self.location
        }

# Create the database tables (run once)
with app.app_context():
    db.create_all()

# Route to return all learners as a JSON list
@app.route('/api/learners', methods=['GET'])
def get_learners():
    learners = Learner.query.all()
    return jsonify([l.serialize for l in learners]), 200

# Route to add new learners via POST (here we insert new learners in the code directly for simplicity)
@app.route('/api/learners', methods=['POST'])
def add_learner():
    try:
        data = request.get_json()
        new_learner = Learner(
            full_name=data['full_name'],
            location=data['location']
        )
        db.session.add(new_learner)
        db.session.commit()
        return jsonify({'message': 'Learner added successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to manually insert initial learners (you can comment this out once you've inserted them once)
@app.route('/api/init', methods=['GET'])
def init_learners():
    # Insert initial learners with ID, names, and cities
    learners_data = [
        {'id': 1, 'full_name': 'Jack Andrew', 'location': 'Monaco'},
        {'id': 2, 'full_name': 'Sophia Brook', 'location': 'Seattle'},
        {'id': 3, 'full_name': 'Austin Marco', 'location': 'Dubai'}
    ]
    
    # Clear current learners table (if needed)
    db.session.query(Learner).delete()

    for learner_data in learners_data:
        learner = Learner(id=learner_data['id'], full_name=learner_data['full_name'], location=learner_data['location'])
        db.session.add(learner)
    
    db.session.commit()
    return jsonify({'message': 'Initial learners added successfully'}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

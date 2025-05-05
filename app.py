from flask import Flask, render_template, request

app = Flask(__name__)

# Define fortunes for each color
fortunes = {
    "purple": ["You will discover new possibilities.", "The future holds a great surprise.", "A time of creativity is coming your way."],
    "turquoise": ["Clarity will help guide your next steps.", "You will find balance in your life.", "Your intuition will lead you to success."],
    "orange": ["A burst of energy will propel you forward.", "Expect some exciting changes in your life.", "You will achieve something you’ve long worked for."],
    "lightgreen": ["Growth and new beginnings are in store for you.", "You’ll soon experience a sense of calm.", "A small change will lead to big results."]
}

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle the form submission
@app.route('/fortune', methods=['POST'])
def fortune():
    # Get the form data
    user_name = request.form['user']
    selected_color = request.form['color']
    selected_number = int(request.form['number'])

    # Get the fortune based on the color and number
    color_fortunes = fortunes.get(selected_color, [])
    fortune = color_fortunes[selected_number - 1]  # Select fortune based on the number

    # Display the fortune
    return f"""
        <h1>Hello, {user_name}!</h1>
        <p>Your selected color: {selected_color}</p>
        <p>Your selected number: {selected_number}</p>
        <h2>Your fortune:</h2>
        <p>{fortune}</p>
    """

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

# Create a Flask web application instance
app = Flask(__name__)
# In-memory list to store tasks
tasks = []

# Route for the main page that displays the to-do list
@app.route('/')
def index():
    # Render the index.html template, passing the current list of tasks
    return render_template('index.html', tasks=tasks)

# Route to handle adding a new task via POST request
@app.route('/add', methods=['POST'])
def add_task():
    # Get the task from the submitted form
    task = request.form['task']
    # Add the new task to the list
    tasks.append(task)
    # Redirect back to the main page
    return redirect(url_for('index'))

# Run the app if this file is executed directly
if __name__ == '__main__':
    app.run(debug=True)

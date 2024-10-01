from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML form
    return render_template('form.html')

@app.route('/process', methods=['POST'])
def process():
    try:
        # Get the form input values
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])

        # Process the input (e.g., add the numbers)
        result = num1 + num2

        # Return the result in a new HTML page
        return f'''
        <html>
        <body>
            <h2>Result:</h2>
            <p>The sum of {num1} and {num2} is: {result}</p>
            <a href="/">Go Back</a>
        </body>
        </html>
        '''
    except ValueError:
        # Handle invalid input (non-numeric values)
        return '''
        <html>
        <body>
            <h2>Error:</h2>
            <p>Invalid input. Please enter valid numbers.</p>
            <a href="/">Go Back</a>
        </body>
        </html>
        '''

if __name__ == '_main_':
    app.run(debug=True)
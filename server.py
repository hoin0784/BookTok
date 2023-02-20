from flask import Flask , render_template

app = Flask(__name__)


# Just added for testing 
@app.route('/')
def hello_world():
  return render_template('main.html')


if __name__ == '__main__':

  # Added for debugging 
  app.run(debug=True)

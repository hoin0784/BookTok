from flask import Flask , render_template

app = Flask(__name__)

# Just added basic routes
@app.route('/')
def Home():
  return render_template('Home.html')

@app.route('/Bookshelf')
def BookShelf():
  return render_template('Bookshelf.html')

@app.route('/Account')
def Account():
  return render_template('Account.html')

if __name__ == '__main__':

  # Added for debugging 
  app.run(debug=True)

from flask import Flask , render_template

app = Flask(__name__)

# Just added basic routes
@app.route('/')
def Home():
  return render_template('Home.html')

@app.route('/bookshelf')
def BookShelf():
  return render_template('Bookshelf.html')

@app.route('/account')
def Account():
  return render_template('Account.html')

@app.route('/genres')
def Genres():
  return render_template('Genres.html')


if __name__ == '__main__':

  # Added for debugging 
  app.run(debug=True)

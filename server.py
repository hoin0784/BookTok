from flask import Flask, render_template,request, url_for, jsonify, json, redirect, session

import requests
import db
import sys

# auth imports
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv

# Load .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)


app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")

# Operates when accessing the URL for the first time
@app.before_first_request
def initialize():
  db.setup()


# ======== Auth Stuff ===========
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://" + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

# ===== End of Auth Stuff ========


# Just added basic routes
@app.route('/', methods = ['GET','POST'] )
def home():

   # Get the value of the form when the user clicked the button
  if request.method == 'POST':
    for key, value in request.form.items():
      if key == 'Romance':
        genres = key
      elif key == 'Thriller':
        genres = key
      elif key == 'Nonfiction':
        genres = key
      elif key == 'Horror':
        genres = key
      elif key == 'Comedy':
        genres = key
      else:
        genres = 'YoungAdult'

    request_url = f"https://openlibrary.org/subjects/{genres}.json"
    request_headers = {
        "Accept": "application/json"
    }
    response = requests.get(request_url, headers=request_headers)
    response_dict = json.loads(response.text)
    book_dict = response_dict["works"]

    title = []
    author = []

    for i in book_dict:
      title.append(i["title"])
      author.append(i["authors"][0]["name"])  # Get the author name

    length = len(title)

    try:
      genres = getattr(sys.modules[__name__], genres)
      return genres(title, author, length)
      
    except AttributeError:
      pass

  # If the method is ['GET] then just call NYT best seller
  else:
    
    # Requests NYT Bestseller 'combined print and ebook fiction' list (there's a lot of lists we can request)
    request_url = "https://api.nytimes.com/svc/books/v3/lists/current/Combined%20Print%20and%20E-Book%20Fiction.json?api-key=Jn4QJ3QZomcadk6kUzr7GKmJubrMVB6y"
    request_headers = {
      "Accept": "application/json"
    }
    response = requests.get(request_url, headers=request_headers)

    # Turn json into a python dictionary
    response_dict = json.loads(response.text)

    # Get only book list info from response_dict
    book_dict = response_dict["results"]["books"]

    # Arrays that will hold featured list data (title, author, cover url)
    featured_title = []
    featured_author = []
    featured_cover = []

    # Get only necessary data for featured list from book_dict
    for i in book_dict:
      featured_title.append(i["title"])
      featured_author.append(i["author"])
      featured_cover.append(i["book_image"])    

    length = len(featured_title)

  # Send featured list data to home.html
  # json.dump is just for debugging can be deleted later
  return render_template('home.html', length = length,
                                      cover_url = featured_cover, 
                                      featured_title = featured_title, 
                                      featured_author = featured_author,
                                      session=session.get('user'), pretty=json.dumps(session.get('user'), indent=4))

@app.route('/account')
def Account():
  return render_template('Account.html')

@app.route('/genres')
def Genres():
  return render_template('genres.html')

@app.route('/romance')
def Romance(title, author, length):

  return render_template('romance.html',length = length,
                                        romance_title = title,
                                        romance_author = author)
      
@app.route('/thriller')
def Thriller(title ,author,length): 
  
  return render_template('thriller.html', length = length,
                                          thriller_title = title,
                                          thriller_author = author)

@app.route('/nonfiction')
def Nonfiction(title, author, length):
  
  return render_template('nonfiction.html', length = length,
                                            non_fiction_title = title,
                                            non_fiction_author = author)

@app.route('/horror')
def Horror(title, author, length):

  return render_template('horror.html', length = length,
                                        horror_title = title,
                                        horror_author = author)

@app.route('/ya')
def YoungAdult(title, author, length):

  return render_template('young_adult.html',length = length,
                                            young_adult_title = title,
                                            young_adult_author = author)

@app.route('/comedy')
def Comedy(title, author, length):
  return render_template('comedy.html' , length =length,
                                         comedy_title = title,
                                         comedy_author = author)

@app.route('/BookSearchList', methods = ['GET','POST'])
def BookSearchList():

  # This route method is almost 'POST' method 
  if request.method == 'POST':
  
    # Get the user input from the form
    BookTitle = request.form.get('BookTitle')

    # Changed URL format for fetching ..
    # (ex: Harry potter -> Harry+potter)
    url_BookTitle = BookTitle.replace(" ", "+")
    
    # Source from : openlibrary.org 
    response = requests.get(f'http://openlibrary.org/search.json?title={url_BookTitle}&limit=20')

    # The response need to be convert to JSON format
    response = response.json()
    results = response['docs']

    # Set the array of the lists that I want to get
    book_title = []
    author_name = []
    cover_id = []
    isbn = []
    
    count = 0
    # print("results length checking...")
    # print(len(results))
    # 15

    # Get the most recent books data from the results length (cover,title,author)
    # Loop untill the length of results
    for i in range(len(results)):
           
      if 'title' in results[i] and 'author_name' in results[i] and 'isbn' in results[i]:
        
        book_title.append(results[i]['title'])  # 1
        isbn.append(results[i]['isbn'][0])  
        # cover_id.append(results[i]['cover_i']) 
        author_name.append(results[i]['author_name'][0]) 

        count+=1
      # else:
      #     break

    # Send the all data to the BookSearchList.html  
  return render_template('BookSearchList.html', count = count,
                                                isbn = isbn,
                                                cover_id = cover_id, 
                                                book_title = book_title, 
                                                author_name = author_name)

@app.route('/bookshelf', methods = ['GET','POST'])
def BookShelf():
  if request.method == 'GET':
    # after setting database, we should add code to bring user's bookshelf info
    # from database and show datas with GET request
    return render_template('Bookshelf.html')
  
  else:
    # POST request = When user created new bookshelf

    # Get new bookshelf name
    bookshelfName = request.form.get('BookshelfName')
    # for now, only newly created bookshelf is shown

    return render_template('Bookshelf.html', bookshelfName = bookshelfName)


if __name__ == '__main__':

  # Added for debugging 
  app.run(debug=True)
  # If this is not working then, try this...
  # flask --app server.py --debug run

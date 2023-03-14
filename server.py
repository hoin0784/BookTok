from flask import Flask, render_template,request, url_for, jsonify, json, redirect, session

import requests
import db
import sys
import os

# auth imports
from os import environ as env
from urllib.parse import quote_plus, urlencode

from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv

# Load .env file
ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

# Get the key from .env
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# Get NYT api key from .env
NYT_API_KEY = os.environ['NYT_API_KEY']


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
      if key == 'romance':
        genres = key
      elif key == 'thriller':
        genres = key
      elif key == 'nonfiction':
        genres = key
      elif key == 'horror':
        genres = key
      elif key == 'comedy':
        genres = key
      else:
        genres = 'children'
    
    request_url = f'https://www.googleapis.com/books/v1/volumes?q=subject:{genres}&maxResults=12&key={GOOGLE_API_KEY}'
    response = requests.get(request_url).json()
    items_length = len(response['items'])
    book_title = []
    author_names = []
    book_thumbnails = []
    book_published_dates = []
    book_isbn13 = []

    print(response)

    for i in range(items_length):
      book_title.append(response['items'][i]['volumeInfo']['title'])
      author_names.append(response['items'][i]['volumeInfo']['authors'][0])
      book_published_dates.append(response['items'][i]['volumeInfo']['publishedDate'])
      book_isbn13.append(response['items'][i]['volumeInfo']['industryIdentifiers'][0]['identifier'])

    # check if imageLinks is defined before appending to book_thumbnails
      if 'imageLinks' in response['items'][i]['volumeInfo']:
          book_thumbnails.append(response['items'][i]['volumeInfo']['imageLinks']['thumbnail'])
      else:
          book_thumbnails.append(None)

    try:
      genres = getattr(sys.modules[__name__], genres)
      
      return genres(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13)
      
    except AttributeError:
      pass

  # If the method is ['GET] then just call NYT best seller
  else:
    
    # Requests NYT Bestseller 'combined print and ebook fiction' list (there's a lot of lists we can request)
    request_url = f"https://api.nytimes.com/svc/books/v3/lists/current/Combined%20Print%20and%20E-Book%20Fiction.json?api-key={NYT_API_KEY}"
    request_headers = {
      "Accept": "application/json"
    }
    response = requests.get(request_url, headers=request_headers)
    # print(response.text)

    # Turn json into a python dictionary
    response_dict = json.loads(response.text)

    # Get only book list info from response_dict
    book_dict = response_dict["results"]["books"]

    # Arrays that will hold featured list data (title, author, cover url)
    featured_title = []
    featured_author = []
    featured_cover = []
    featured_isbn13 = []

    # Get only necessary data for featured list from book_dict
    for i in book_dict:
      featured_title.append(i["title"])
      featured_author.append(i["author"])
      featured_cover.append(i["book_image"])    
      featured_isbn13.append(i['isbns'][0]['isbn13'])
     
      length = len(featured_title)

  # Send featured list data to home.html
  # json.dump is just for debugging can be deleted later
  return render_template('home.html', cover_url = featured_cover, 
                                      featured_title = featured_title, 
                                      featured_author = featured_author,
                                      featured_isbn13 = featured_isbn13,
                                      length = length,
                                      session = session.get('user'), 
                                      pretty=json.dumps(session.get('user'), indent=4))

@app.route('/account')
def account():
  return render_template('Account.html', session = session.get('user'))

# @app.route('/genres')
# def Genres():
#   return render_template('genres.html', session = session.get('user'))

@app.route('/romance')
def romance(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13):

  return render_template('romance.html',romance_title = book_title,
                                        author_names = author_names,
                                        book_thumbnails = book_thumbnails,
                                        book_published_dates = book_published_dates,
                                        items_length = items_length,
                                        book_isbn13 = book_isbn13,
                                        session = session.get('user'))
      
@app.route('/thriller')
def thriller(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13):
  
  return render_template('thriller.html', thriller_title = book_title,
                                          author_names = author_names,
                                          book_thumbnails = book_thumbnails,
                                          book_published_dates = book_published_dates,
                                          items_length = items_length,
                                          book_isbn13 = book_isbn13,
                                          session = session.get('user'))

@app.route('/nonfiction')
def nonfiction(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13):
  
  return render_template('nonfiction.html', nonfiction_title = book_title,
                                            author_names = author_names,
                                            book_thumbnails = book_thumbnails,
                                            book_published_dates = book_published_dates,
                                            items_length = items_length,
                                            book_isbn13 = book_isbn13,
                                            session = session.get('user'))

@app.route('/horror')
def horror(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13):

  return render_template('horror.html', horror_title = book_title,
                                        author_names = author_names,
                                        book_thumbnails = book_thumbnails,
                                        book_published_dates = book_published_dates,
                                        items_length = items_length,
                                        book_isbn13 = book_isbn13,
                                        session=session.get('user'))

@app.route('/childrens')
def children(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13):

  return render_template('childrens.html',  children_title = book_title,
                                              author_names = author_names,
                                              book_thumbnails = book_thumbnails,
                                              book_published_dates = book_published_dates,
                                              items_length = items_length,
                                              book_isbn13 = book_isbn13,
                                              session = session.get('user'))

@app.route('/comedy')
def comedy(book_title, author_names, book_thumbnails, book_published_dates, items_length, book_isbn13):

  return render_template('comedy.html', comedy_title = book_title,
                                        author_names = author_names,
                                        book_thumbnails = book_thumbnails,
                                        book_published_dates = book_published_dates,
                                        items_length = items_length,
                                        book_isbn13 = book_isbn13,
                                        session = session.get('user'))

@app.route('/BookSearchList', methods = ['GET','POST'])
def book_search_list():

  # This route method is almost 'POST' method 
  if request.method == 'POST':
  
    # Get the user input from the form
    title = request.form.get('book_title')

    # Changed URL format for fetching ..
    # (ex: Harry potter -> Harry+potter)
    url_book_title = title.replace(" ", "+")
  
    # This is already defaulted 10 (from Google Books Api), so we do not need to set max.
    # I have set the global variable GOOGLE_API_KEY from line 21. 

    url = f'https://www.googleapis.com/books/v1/volumes?q={url_book_title}&maxResults=12&key={GOOGLE_API_KEY}'
    response = requests.get(url).json()
    items_length = len(response['items'])

    book_title =[]
    author_names = []
    book_thumbnails = []
    book_published_dates =[]

    # Get the data from the json (title, authors, thumbnail,publishedDate)
    
    for i in range(items_length):
      book_title.append(response['items'][i]['volumeInfo'].get('title', ''))
      author_names.append(response['items'][i]['volumeInfo'].get('authors', [''])[0])
      book_thumbnails.append(response['items'][i]['volumeInfo'].get('imageLinks', {}).get('thumbnail', ''))
      book_published_dates.append(response['items'][i]['volumeInfo'].get('publishedDate', ''))

  return render_template('BookSearchList.html', items_length=items_length,
                                                book_title = book_title,
                                                author_names = author_names,
                                                book_thumbnails = book_thumbnails,
                                                book_published_dates = book_published_dates,
                                                session = session.get('user'))


@app.route('/bookshelf', methods = ['GET','POST'])
def book_shelf():
  if session.get('user') is None:
    return render_template('UserOnly.html', session = session.get('user'))

  else:
    # Get user's email address
    user_session = session.get('user')
    user_info = user_session['userinfo']
    user_email = user_info['email']

    with db.get_db_cursor(True) as cur:
      # Get user's bookshelf list
      cur.execute("SELECT bookshelfname FROM userinfo WHERE useremail = %s;", (user_email,))
      rows = cur.fetchall()
      bookshelves = []
      for row in rows:
        bookshelves.append(row[0])
      
      # Get list of shelved books
      books = []
      for bookshelf in bookshelves:
        cur.execute("SELECT bookTitle FROM shelvedbooks WHERE useremail = %s AND bookshelfname = %s;", (user_email, bookshelf,))
        temp = [row for row in cur.fetchall()]
        books.append(temp)

    if request.method == 'GET':
      return render_template('Bookshelf.html', session=session.get('user'),
                                               bookshelves=bookshelves,
                                               books=books)

    else:  
      # POST request = When user created new bookshelf

      # Get new bookshelf name
      new_bookshelf = request.form.get('bookshelfName')
      bookshelves.append(new_bookshelf)
      
      with db.get_db_cursor(True) as cur:
        # Create a bookshelf in database
        cur.execute("INSERT INTO userinfo(userEmail, bookshelfName) values (%s, %s);", (user_email, new_bookshelf,))
          
        # Render the HTML code for the newly created bookshelf
      return render_template('Bookshelf.html', session=session.get('user'),
                                               bookshelves=bookshelves,
                                               books=books)
    

@app.route('/delete/<bookshelf>', methods = ['POST'])
def delete_bookshelf(bookshelf):
  # Get user's email address
  user_session = session.get('user')
  user_info = user_session['userinfo']
  user_email = user_info['email']

  # Delete bookshelf from database
  with db.get_db_cursor(True) as cur:
    cur.execute("DELETE FROM userinfo WHERE userEmail = %s AND bookshelfName = %s;", (user_email, bookshelf,))
    cur.execute("DELETE FROM shelvedbooks WHERE userEmail = %s AND bookshelfName = %s;", (user_email, bookshelf,))

  return redirect(url_for('book_shelf'))


# add a featured book to your bookshelf
@app.route('/add_featured_book', methods = ['POST'])
def add_featured_book():

  # get the bookshelf that was selected
  bookshelf_name = request.form.get('bookshelf_name')
  
  # if no bookshelf has been selected do nothing
  if(bookshelf_name == ''):
    print('Book was not added to any bookshelves.')
    return {"random": "data1"}
  
  # if a legit bookshelf has been selected, continue...
  else:
    # Get user's email address
    user_session = session.get('user')
    user_info = user_session['userinfo']
    user_email = user_info['email']

    # get book isbn13/book title data to send to database
    book_isbn13 = request.form.get('isbn13')
    book_title = request.form.get('book_title')

    # print(book_isbn13)
    # print(bookshelf_name)
    # print(book_title)
    # print(user_email)

    # everything is good, send data to database
    db.add_book_to_bookshelf(user_email, bookshelf_name, book_isbn13, book_title)
    print('Book added to a bookshelf.')
    return {"random": "data1"}

if __name__ == '__main__':

  # Added for debugging 
  app.run(debug=True)
  # If this is not working then, try this...
  # flask --app server.py --debug run

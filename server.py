from flask import Flask , render_template,request, url_for

import requests

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

# @app.route('/BookSearchList', methods = ['GET'])
# def BookSearchList():

#   title = request.args.get('BookTitle')
#   print("---- GET TEST ----")
#   print(title)

#   return render_template('BookSearchList.html')



@app.route('/BookSearchList', methods = ['GET','POST'])
def BookSearchList():

  # This route method is almost 'POST' method (I guess ?)
  if request.method == 'POST':
  
    # Get the user input from the form
    BookTitle = request.form.get('BookTitle')

    # Changed URL format for fetching ..
    # (ex: Harry potter -> Harry+potter)
    url_BookTitle = BookTitle.replace(" ", "+")
    
    # Source from : openlibrary.org 
    response = requests.get(f'http://openlibrary.org/search.json?title={url_BookTitle}&limit=10')

    # The response need to be convert to JSON format
    response = response.json()
    results = response['docs']

    # Set the array of the lists that I want to get
    book_title = []
    author_name = []
    cover_id = []
    isbn = []
    
    count = 0

    # Get the most recent books data from the results length (cover,title,author)
    # Loop untill the length of results
    for i in range(len(results)):
           
      if 'title' in results[i] and 'author_name' in results[i] and 'cover_i' in results[i]:

        cover_id.append(results[i]['cover_i'])
        book_title.append(results[i]['title'])
        author_name.append(results[i]['author_name'])
        # Since there are lots of isbn get the first one
        isbn.append(results[i]['isbn'][0])

        count+=1
      # else:
      #   break

    # Send the all data to the BookSearchList.html  
  return render_template('BookSearchList.html', count = count,
                                                isbn = isbn,
                                                cover_id = cover_id, 
                                                book_title = book_title, 
                                                author_name = author_name)

if __name__ == '__main__':

  # Added for debugging 
  app.run(debug=True)
  # If this is not working then, try this...
  # flask --app server.py --debug run

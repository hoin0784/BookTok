# Module 1 Group Assignment

CSCI 5117, Spring 2023, [assignment description](https://canvas.umn.edu/courses/355584/pages/project-1)

## App Info:

* Team Name: Booktok
* App Name: Booktok
* App Link: <https://booktok.onrender.com/> 


### Students

* Fiorela Esquivel Martinez esqui049@umn.edu
* Hoin Jang, jang0064@umn.edu
* Monika Bartulovic, bartu043@umn.edu
* Sol Kim kim01540@umn.edu
* ...


## Key Features

**Describe the most challenging features you implemented
(one sentence per bullet, maximum 4 bullets):**

<<<<<<< HEAD
* Booktok uses the Google Books APIs to search for genres and individual book titles
* Booktok uses the New York times APIs to show NYT Bestseller (Featured List)
=======
** Our most challenging and prominent feature was our Bookshelf feature, in which users can create bookshelves and add books to them.
** 

## Testing Notes

**Is there anything special we need to know in order to effectively test your app? (optional):**

* ...

>>>>>>> ce94d25385e7c77f25a533191cf43842bd0c2e18

## Screenshots of Site
Figure 1: This is BookTok homepage ,which features a search bar, some genres and the bestsellers of books. 
<img src = "static/images/MainPage.png">

Figure 2: This is a user's bookshelf page that has a form to create/delete a new bookshelves and shows their current bookshelves.
<img src = "static/images/Bookshelf.png">

Figure 3: This is search results page for book "hobbit"
<img src = "static/images/SearchBook.png">

Figure 4: This is the detailed book page that appears when the user clicks on one of the images of "The hobbit" books.
<img src = "static/images/BookDetailed.png">


![](static/images/landingpage.png?raw=true)
![](static/images/searchresultspage.png?raw=true)
![](static/images/accountpage.png?raw=true)
![](static/images/bookshelfpage.png?raw=true)

## Mock-up 

<<<<<<< HEAD
Mock-ups link : <https://www.figma.com/file/0xv3ZRWf61KXjlvsNLr7UL/BookTok-WireFrame?node-id=0%3A1>
=======
There are a few tools for mock-ups. Paper prototypes (low-tech, but effective and cheap), Digital picture edition software (gimp / photoshop / etc.), or dedicated tools like moqups.com (I'm calling out moqups here in particular since it seems to strike the best balance between "easy-to-use" and "wants your money" -- the free teir isn't perfect, but it should be sufficient for our needs with a little "creative layout" to get around the page-limit)

In this space please either provide images (around 4) showing your prototypes, OR, a link to an online hosted mock-up tool like moqups.com

**[Add images/photos that show your paper prototype (around 4)](https://stackoverflow.com/questions/10189356/how-to-add-screenshot-to-readmes-in-github-repository) along with a very brief caption:**

![](https://media.giphy.com/media/26ufnwz3wDUli7GU0/giphy.gif)


Link to our mock-ups: https://www.figma.com/file/0xv3ZRWf61KXjlvsNLr7UL/BookTok-WireFrame?node-id=0%3A1
>>>>>>> ce94d25385e7c77f25a533191cf43842bd0c2e18


## External Dependencies


* Google Books API / NYT API: We used Google Books API and NYT API to search for genres,individual book titles and show bestsellers of books. This was primarily accomplished by using their search API interpolation. After a user adds a search result, we query their main API interpolation for a work to get information on author, title, and cover image. 

  Such as: <https://www.googleapis.com/books/v1/volumes?q={book_title}&key={Google_API_KEY}><br>
  In this case, book title is what user search and the key of Google_API_KEY is in .env file

* python-dotenv: This library was used to handle loading the .env file more easily

* FontAwesome: We used FontAwesome to add styling of letters

* Pure CSS : We used Pure css to design our table, book lists, making a responsive website




<<<<<<< HEAD
=======
* use command [python -m pip install requests] to install the Requests http library
>>>>>>> ce94d25385e7c77f25a533191cf43842bd0c2e18

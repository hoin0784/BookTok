-- Created
CREATE TABLE userinfo (
    userEmail varchar not null,
    bookshelfName varchar not null
);

CREATE TABLE shelvedBooks (
  userEmail varchar not null,
  bookshelfName varchar not null,
  isbn varchar(20) not null,
  bookTitle varchar not null
);

insert into userinfo(useremail, bookshelfname) values ('esqui049@umn.edu', 'favorites');

insert into shelvedbooks(useremail, bookshelfname, isbn, booktitle) values ('kim01540@umn.edu', 
                                                                            'my mystery books', 
                                                                            '', 
                                                                            '');

-- \dt             : (print out table )
-- \d (table name) : (print out table info)
drop table Book;
SELECT * from Book;

-- delete data from table
TRUNCATE TABLE  table_name;

-- OR make the class of book, profile
-- create table Book(
--   cover_id      SERIAL PRIMARY KEY,
--   book_title    varchar(20),
--   author_name   varchar(20),
--   isbn          number(20),    
-- );
-- Next...
-- we need to make the user profile table....





    <!-- <table class="pure-table pure-table-horizontal" id="bookshelf">
        <thead>
            {{bookshelves}}
        </thead>
        <tbody>
            <tr>
                <td>book name</td>
            </tr>
            <tr>
                <td>book name</td>
            </tr>
            <tr>
                <td>book name</td>
            </tr>
            <tr>
                <td>book name</td>
            </tr>
        </tbody>
    </table> -->

<!-- {% for shelfName, books in bookshelves.items() %}
    <table>
        <thead>
            {{shelfName}}
        </thead>
        <tbody>
            {% for book in books %}
            <tr>
                <td>{{book}}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
{% endfor %} -->
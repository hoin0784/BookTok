-- \dt             : (print out table )
-- \d (table name) : (print out table info)
drop table Book;
SELECT * from Book;

-- OR make the class of book, profile
create table Book(
  cover_id      SERIAL PRIMARY KEY,
  book_title    varchar(20),
  author_name   varchar(20),
  isbn          number(20),    
);
-- Next...
-- we need to make the user profile table....

-- This is just sketch
CREATE TABLE bookshelf (
    user varchar not null,
    shelfName varchar not null
);


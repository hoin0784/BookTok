
function add_book(id, shelf_name, book_title) {
    console.log("adding book...");
    console.log(id);
    console.log(shelf_name);
    console.log(book_title);


    let data = new FormData()
    data.append("isbn13", id)
    data.append("bookshelf_name", shelf_name)
    data.append("book_title", book_title)
    fetch('/add_featured_book', {
        "method": "POST",
        "body": data,
    })
    // .then(...)
}

// document.querySelector('#clickCount').addEventListener('click', buttonClick);

// var names = document.getElementsByName("featured_shelves");
// for (var i = 0; i < names.length; i++) {
//     // let id = names[i].getAttribute( 'id' );
//     let id = names[i].id;
//     console.log("id: ", id);
//     // console.log(id);
//     // if (names[i].onchange == true) {
//     //     add_book(id);
//     // }
//     names[i].onchange = add_book(id);
// }

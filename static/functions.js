// Show pop up box when "Create new bookshelf" button is clicked
function newShelfForm() {
    document.getElementById("popupBox").style.display = 'block';
};


// Hide pop up box when "delete" button is clicked
function closePopup(){
    document.getElementById("popupBox").style.display = 'none';
}



// // code reference: Stackoverflow https://stackoverflow.com/questions/14643617/create-table-using-javascript
// function createShelf() {
//     const body = document.body, tbl = document.createElement('table');

//     for (let i = 0; i < 4; i++) {
//         const tr = tbl.insertRow();
//         for (let j = 0; j < 1; j++) {
//             if (i === 1 && j === 1) {
//                 break;
//             } 
//             else {
//                 const td = tr.insertCell();
//                 td.appendChild(document.createTextNode(`Add a book`));
//                 td.style.border = '1px solid black';
//                 if (i === 1 && j === 1) {
//                 td.setAttribute('rowSpan', '2');
//                 }
//             }
//         }
//     }
//     body.appendChild(tbl);
// };
// Show pop up box when "Create new bookshelf" button is clicked
function newShelfForm() {
    document.getElementById("popupBox").style.display = 'block';
};

// delete bookshelf
function delete_bookshelf(){
  console.log("hello");

};

// Hide pop up box when "delete" button is clicked
function closePopup(){
    document.getElementById("popupBox").style.display = 'none';
}

// After new bookshelf is created
// Bring GET request result after POST request
$(document).ready(function() {
  $('#newBookshelf').submit(function(event) {
    event.preventDefault();
    var formData = $(this).serializeArray();
    var jsonData = {};

    $.each(formData, function() {
      jsonData[this.name] = this.value;
    });
  
    $.ajax({
      type: 'POST',
      url: '/bookshelf',
      data: JSON.stringify(jsonData),
      contentType: 'application/json',
      success: function(response) {
        $('#result').text(response.message);
      },
      error: function(xhr, status, error) {
        console.error(error);
      }
    });
  });
});

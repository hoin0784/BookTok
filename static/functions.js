// Show pop up box when "Create new bookshelf" button is clicked
function newShelfForm() {
    document.getElementById("popupBox").style.display = 'block';
};


// Hide pop up box when "delete" button is clicked
function closePopup(){
    document.getElementById("popupBox").style.display = 'none';
}


$(document).ready(function() {
    $('#newBookshelf').submit(function(event) {
      event.preventDefault();
  
      // Serialize the form data into a JSON object
      var formData = $(this).serializeArray();
      var jsonData = {};
      $.each(formData, function() {
        jsonData[this.name] = this.value;
      });
  
      // Send an AJAX POST request to the server with the form data
      $.ajax({
        type: 'POST',
        url: '/bookshelf',
        data: JSON.stringify(jsonData),
        contentType: 'application/json',
        success: function(response) {
          // Handle the successful response from the server
          console.log('Form submitted successfully:', response);
  
          // Update the page with the response data
          $('#result').text(response.message);
        },
        error: function(xhr, status, error) {
          // Handle the error response from the server
          console.error('Error submitting form:', error);
        }
      });
    });
  });
  
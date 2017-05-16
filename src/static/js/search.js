// This facilitates the AJAX Search Feature
$('#search-form').submit(function(e){
$.post('/search/', $(this).serialize(), function(data){
$('#cust').html(data);
});
e.preventDefault();
});

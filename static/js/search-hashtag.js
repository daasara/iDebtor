var hashTags = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('query'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  remote: '/customer.json?query=%QUERY'
});

hashTags.initialize();

$('.customer-search').typeahead(
		{hint: true,
        highlight: true,
        minLength: 2}, 
        {
  displayKey: 'query',
  source: hashTags.ttAdapter()
});

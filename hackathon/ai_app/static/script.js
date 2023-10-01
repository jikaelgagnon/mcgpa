const searchText = document.getElementById('course_autocomplete');
const submitSearch = document.getElementById('select-button');
const selectionList = document.getElementById('selections');

submitSearch.addEventListener('click', function(){
  const newLI = document.createElement('li');
  newLI.value = searchText.textContent;
  selectionList.appendChild(newLI);
})


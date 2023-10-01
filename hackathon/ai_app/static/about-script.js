const data = [1, 2, 3, 4, 5];
  
fetch('/process-data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({data: data})
})
.then(response => response.text())
.then(result => {
  console.log(result);
})
.catch(error => {
  console.error('Error:', error);
});
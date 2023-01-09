// Get form element
const addForm = document.getElementById('add-form');

// Add event listener to form
addForm.addEventListener('submit', e => {
  // Prevent default behavior (form submission)
  e.preventDefault();

  // Get task from form
  const task = document.getElementById('task').value;

  // Send POST request to API to add todo item
  fetch('/todo', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ task: task })
  })
  .then(response => response.json())
  .then(data => console.log(data));
});
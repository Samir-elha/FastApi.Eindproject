// Get div element to display list of todo items
const todoList = document.getElementById('todo-list');

// Send GET request to API to get list of todo items
fetch('/todo')
  .then(response => response.json())
  .then(todos => {
    // Clear todo list
    todoList.innerHTML = '';

    // Loop through list of todo items
    todos.forEach(todo => {
      // Create div for todo item
      const todoDiv = document.createElement('div');
      todoDiv.classList.add('todo');

      // Create span for todo task
      const taskSpan = document.createElement('span');
      taskSpan.innerText = todo.task;

      // Create button to edit todo item
      const editButton = document.createElement('button');
      editButton.innerText = 'Edit';
      editButton.addEventListener('click', () => {
        // Get new task from user
        const newTask = prompt('Enter new task');

        // Send PUT request to API to update todo item
        fetch(`/todo/${todo.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ task: newTask })
        })
        .then(response => response.json())
        .then(data => {
          // Update task span with new task
          taskSpan.innerText = data.task;
        });
      });

      // Create button to delete todo item
      const deleteButton = document.createElement('button');
      deleteButton.innerText = 'Delete';
      deleteButton.addEventListener('click', () => {
        // Send DELETE request to API to delete todo item
        fetch(`/todo/${todo.id}`, {
          method: 'DELETE'
        })
        .then(response => {
          // Remove todo item from list
          todoDiv.remove();
        });
      });

      // Append task span, edit button, and delete button to todo div
      todoDiv.appendChild(taskSpan);
      todoDiv.appendChild(editButton);
      todoDiv.appendChild(deleteButton);

      // Append todo div to todo list
      todoList.appendChild(todoDiv);
    });
  });
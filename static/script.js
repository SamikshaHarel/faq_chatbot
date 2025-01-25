function addTask() {
    const task = document.getElementById('task-input').value;
    const reminder_time = document.getElementById('reminder-time').value;

    if (!task) {
        alert('Please enter a task!');
        return;
    }

    fetch('/add_task', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ task: task, reminder_time: reminder_time })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadTasks(); // Reload the task list
    });
}

function listenForTask() {
    fetch('/listen_task', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('task-input').value = data.task;
    });
}

function loadTasks() {
    fetch('/get_tasks')
        .then(response => response.json())
        .then(data => {
            const taskList = document.getElementById('tasks');
            taskList.innerHTML = '';
            data.forEach(task => {
                const li = document.createElement('li');
                li.innerHTML = `
                    <div class="task-info">
                        <span>${task.task}</span><br>
                        Reminder: <span>${task.reminder_time || 'Not set'}</span>
                    </div>
                    <div class="status">${task.status}</div>
                `;
                taskList.appendChild(li);
            });
        });
}

// Load tasks on page load
window.onload = loadTasks;

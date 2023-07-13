import { Component } from '@angular/core';

@Component({
  selector: 'app-todo',
  templateUrl: './todo.component.html',
  styleUrls: ['./todo.component.css']
})
export class TodoComponent {
  tasks: { title: string; completed: boolean }[] = [];
  newTask: string = '';
  editMode: number | null = null; // Keeps track of the edit mode index

  addTask() {
    if (this.newTask.trim()) {
      this.tasks.push({ title: this.newTask, completed: false });
      localStorage.setItem('tasks', JSON.stringify(this.tasks));
      this.newTask = '';
    }
  }

  completeTask(task: { title: string; completed: boolean }) {
    task.completed = true;
    localStorage.setItem('tasks', JSON.stringify(this.tasks));
  }

  deleteTask(task: { title: string; completed: boolean }) {
    const taskIndex = this.tasks.indexOf(task);
    if (taskIndex > -1) {
      this.tasks.splice(taskIndex, 1);
      localStorage.setItem('tasks', JSON.stringify(this.tasks));
    }
    
  }

  ngOnInit() {
    const storedTasks = localStorage.getItem('tasks');
    if (storedTasks) {
      this.tasks = JSON.parse(storedTasks);
    }
  }
  toggleEditMode(index: number) {
    this.editMode = this.editMode === index ? null : index;
  }

  saveTask(index: number) {
    this.editMode = null;
    // You can optionally add additional logic here, such as validation
    // or saving the edited task to a database or storage
    localStorage.setItem('tasks', JSON.stringify(this.tasks));
  }
}

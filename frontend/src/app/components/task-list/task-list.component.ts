import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';



interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
}

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [CommonModule, MatCardModule, MatButtonModule],
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent {
  tasks: Task[] = [
    {
      id: 1,
      title: 'Learn Angular',
      description: 'Understand components, bindings, and services.',
      status: 'todo'
    },
    {
      id: 2,
      title: 'Connect to Flask API',
      description: 'Make HTTP requests to backend.',
      status: 'in-progress'
    }
  ];
  deleteTask(id: number): void {
    const confirmed = confirm('Are you sure you want to delete this task?');
  
    if (confirmed) {
      this.tasks = this.tasks.filter(task => task.id !== id);
    }
  }
  
}



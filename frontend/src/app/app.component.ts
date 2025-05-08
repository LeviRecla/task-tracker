import { Component, OnInit } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { TaskListComponent } from './components/task-list/task-list.component';
import { MatDialogModule, MatDialog } from '@angular/material/dialog';
import { AddTaskDialogComponent } from './components/add-task-dialog/add-task-dialog.component';
import { TaskService, Task } from './services/task.service';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TaskListComponent, MatButtonModule, MatDialogModule, AddTaskDialogComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  tasks: Task[] = [];

  constructor(private dialog: MatDialog, private taskService: TaskService) {}

  ngOnInit(): void {
    this.taskService.getTasks().subscribe({
      next: (data) => (this.tasks = data),
      error: (err) => console.error('Error fetching tasks:', err)
    });
  }

  onAddTask(): void {
    const dialogRef = this.dialog.open(AddTaskDialogComponent);

    dialogRef.afterClosed().subscribe((newTask: Task | undefined) => {
      if (newTask) {
        this.taskService.getTasks().subscribe({
          next: (data) => this.tasks = data,
          error: (err) => console.error('Error refreshing tasks:', err)
        });
        
      }
    });
  }
}

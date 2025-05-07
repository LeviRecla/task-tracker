import { Component } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { TaskListComponent } from './components/task-list/task-list.component';
import { MatDialogModule, MatDialog } from '@angular/material/dialog';
import { AddTaskDialogComponent } from './components/add-task-dialog/add-task-dialog.component';



@Component({
  selector: 'app-root',
  standalone: true,
  imports: [TaskListComponent, MatButtonModule, MatDialogModule, AddTaskDialogComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  constructor(private dialog: MatDialog) {}

  onAddTask(): void {
    this.dialog.open(AddTaskDialogComponent);
  }
}



import { AppComponent } from './app.component';
import { TaskListComponent } from './components/task-list/task-list.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

export const appConfig = {
  standalone: true,
  component: AppComponent,
  imports: [
    TaskListComponent
  ],
  providers: [provideAnimationsAsync()]
};

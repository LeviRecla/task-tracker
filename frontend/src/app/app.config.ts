import { provideHttpClient } from '@angular/common/http';
import { AppComponent } from './app.component';

export const appConfig = {
  standalone: true,
  component: AppComponent,
  providers: [
    provideHttpClient()
  ]
};

import { Routes } from '@angular/router';
import { Login } from '../Components/Auth/login/login';
import { Home } from '../Components/Main/home/home';

export const routes: Routes = [
    { path: '', component: Login },
    { path: 'home', component: Home }
];

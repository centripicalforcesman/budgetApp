import { Routes } from '@angular/router';
import { BudgetsComponent } from './features/budgets/budgets.component';

export const routes: Routes = [
    {
        path: '', 
        component: BudgetsComponent 
    },
    {
        path: ':year/:month', 
        component: BudgetsComponent 
    }
];

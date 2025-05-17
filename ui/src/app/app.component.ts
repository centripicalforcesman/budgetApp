// import { Component } from '@angular/core';
// import { RouterOutlet } from '@angular/router';

// @Component({
//   selector: 'app-root',
//   imports: [RouterOutlet],
//   templateUrl: './app.component.html',
//   styleUrl: './app.component.scss'
// })
// export class AppComponent {
//   title = 'ui';
// }

import { Component } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { BudgetService } from './features/budgets/services/budget.service'

@Component({
    selector: 'button-demo',
    templateUrl: './app.component.html',
    standalone: true,
    imports: [ButtonModule]
})
export class AppComponent {
    constructor(private budgetService: BudgetService) {}

    loadBudget(): void {
        this.budgetService.getBudgets();
    }
}
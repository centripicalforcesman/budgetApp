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

import { Component, OnInit } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { BudgetService } from './features/budgets/services/budget.service'
import { Budget } from './shared/models/budget';

@Component({
    selector: 'button-demo',
    templateUrl: './app.component.html',
    standalone: true,
    imports: [ButtonModule]
})
export class AppComponent {

    budgets!: Budget[]
    constructor(private budgetService: BudgetService) {}

    ngOnInit() {
        this.productService.getProductsMini().then((data) => {
            this.products = data;
        });
        this.budgetService.getBudgets().subscribe(budgets => { 
            this.budgets = budgets;
        });
    }

    loadBudget(): void {
        this.budgetService.getBudgets().subscribe(budgets => { 
            console.log(budgets)
        });
    }
}
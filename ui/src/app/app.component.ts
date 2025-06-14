//TODO: move all of this code to its own component. and out of base app.component

import { Component, OnInit } from '@angular/core';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { CardModule } from 'primeng/card';
import { AccordionModule } from 'primeng/accordion';
import { BudgetService } from './features/budgets/services/budget.service'
import { Budget } from './shared/models/budget';
import { CommonModule } from '@angular/common';
import { BudgetGroup } from './shared/models/budgetGroup';

@Component({
    selector: 'budget-group',
    templateUrl: './app.component.html',
    standalone: true,
    imports: [TableModule, CommonModule, CardModule, ButtonModule, AccordionModule],
})
export class AppComponent {

    budgetGroups!: BudgetGroup[];

    constructor(private budgetService: BudgetService) {
    }

    ngOnInit() {

        this.budgetService.getBudgets().subscribe(budget => { 
            this.budgetGroups = budget.budgetGroups;
        });
    }

    loadBudget(): void {
        this.budgetService.getBudgets().subscribe(budgets => { 
            console.log(budgets)
        });
    }
}
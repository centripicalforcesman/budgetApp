import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, ActivatedRouteSnapshot } from '@angular/router';
import { ButtonModule } from 'primeng/button';
import { TableModule } from 'primeng/table';
import { CardModule } from 'primeng/card';
import { AccordionModule } from 'primeng/accordion';
import { BudgetService } from '../../features/budgets/services/budget.service'
import { CommonModule } from '@angular/common';
import { BudgetGroup } from '../../shared/models/budgetGroup';
import { InputTextModule } from 'primeng/inputtext';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'budgets',
  standalone: true,
  imports: [TableModule, CommonModule, CardModule, ButtonModule, AccordionModule, InputTextModule, FormsModule],
  templateUrl: './budgets.component.html',
  styleUrl: './budgets.component.scss'
})

export class BudgetsComponent implements OnInit {
    private year: number
    private month: number
    budgetGroups!: BudgetGroup[];

    constructor(
      private budgetService: BudgetService,
      private route: ActivatedRoute) {

        this.year = Number(this.route.snapshot.paramMap.get('year'));
        this.month = Number(this.route.snapshot.paramMap.get('month'));
        console.log(`year: ${this.year}`);
        console.log(`month: ${this.month}`);

    }

    ngOnInit() {

        this.budgetService.getBudgetsByYearMonth(this.year, this.month).subscribe(budget => { 
            this.budgetGroups = budget.budgetGroups;
            this.budgetGroups.forEach(bg => bg.shouldShowRows = true);
        });
    }

    loadBudget(): void {
        this.budgetService.getBudgets().subscribe(budgets => { 
            console.log(budgets)
        });
    }
}


//TODO: move all of this code to its own component. and out of base app.component

// import { Component, OnInit } from '@angular/core';
// import { ButtonModule } from 'primeng/button';
// import { TableModule } from 'primeng/table';
// import { CardModule } from 'primeng/card';
// import { AccordionModule } from 'primeng/accordion';
// import { BudgetService } from './features/budgets/services/budget.service'
// import { Budget } from './shared/models/budget';
// import { CommonModule } from '@angular/common';
// import { BudgetGroup } from './shared/models/budgetGroup';
// import { InputTextModule } from 'primeng/inputtext';
// import { FormsModule } from '@angular/forms';

// @Component({
//     selector: 'budget-group',
//     templateUrl: './app.component.html',
//     standalone: true,
//     imports: [TableModule, CommonModule, CardModule, ButtonModule, AccordionModule, InputTextModule, FormsModule],
// })
// export class AppComponent {

//     budgetGroups!: BudgetGroup[];

//     constructor(private budgetService: BudgetService) {
//     }

//     ngOnInit() {

//         this.budgetService.getBudgets().subscribe(budget => { 
//             this.budgetGroups = budget.budgetGroups;
//             this.budgetGroups.forEach(bg => bg.shouldShowRows = true);
//         });
//     }

//     loadBudget(): void {
//         this.budgetService.getBudgets().subscribe(budgets => { 
//             console.log(budgets)
//         });
//     }
// }
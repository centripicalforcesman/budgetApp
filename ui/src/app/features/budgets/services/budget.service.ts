import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Budget } from 'src/app/shared/models/budget';

@Injectable({
  providedIn: 'root' // or provide in feature module if scoped
})
export class BudgetService {
  private apiUrl = 'http://127.0.0.1:5000/budgets';

  constructor(private http: HttpClient) {}

  getBudgets(): Observable<Budget> {
    // this.http.get<string>(this.apiUrl).subscribe(budgets => { 
    //   console.log(budgets)
    // });
    //just hardcoded for now.  Will change
    return this.http.get<Budget>(`${this.apiUrl}/1`);
  }

  getBudgetsByYearMonth(year: number, month: number): Observable<Budget> {
    // this.http.get<string>(this.apiUrl).subscribe(budgets => { 
    //   console.log(budgets)
    // });

    return this.http.get<Budget>(`${this.apiUrl}/${year}/${month}`);
  }

  addBudget(budget: Budget): Observable<Budget> {
    return this.http.post<Budget>(this.apiUrl, budget);
  }

  // other CRUD methods...
}
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Budget } from 'src/app/shared/models/budget';

@Injectable({
  providedIn: 'root' // or provide in feature module if scoped
})
export class BudgetService {
  private apiUrl = 'http://127.0.0.1:5000/budgets/1';

  constructor(private http: HttpClient) {}

  getBudgets(): Observable<Budget> {
    // this.http.get<string>(this.apiUrl).subscribe(budgets => { 
    //   console.log(budgets)
    // });

    return this.http.get<Budget>(this.apiUrl);
  }

  addBudget(budget: Budget): Observable<Budget> {
    return this.http.post<Budget>(this.apiUrl, budget);
  }

  // other CRUD methods...
}
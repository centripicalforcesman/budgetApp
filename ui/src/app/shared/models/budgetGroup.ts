import { BudgetItem } from "./budgetItem";

export interface BudgetGroup {
    id: number;
    name: string;
    shouldShowRows: boolean,//move this to a class to implement a default value.
    budgetItems: BudgetItem[]
}
import { BudgetGroup } from "./budgetGroup";

export interface Budget {
    id: number;
    month: number;
    year: number;
    budgetGroups: BudgetGroup[]
}

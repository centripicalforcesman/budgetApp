import unittest
from budgets.services.GetBudget import GetBudget

class TestGetBudget(unittest.TestCase):

    def test_first(self):
        getBudget = GetBudget()
        budget_id = 3
        expectedOutput = f"this is from GetBudget.Execute: {budget_id}"
        actualOutput = getBudget.Execute(budget_id)
        self.assertEqual(expectedOutput, actualOutput)

print(__name__)
if __name__ == '__main__':
    unittest.main()
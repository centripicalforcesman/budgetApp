
# Modular Monolith Architecture for a Budgeting App
## This is some notes from ChatGPT.  Likely not going to use everything here.  Just want to record.

## Overview
A **modular monolith** is a single application with a modular, well-organized structure. It provides the simplicity of a monolith while incorporating principles of microservices, such as separation of concerns and loosely coupled modules. This is ideal for building scalable, maintainable applications while avoiding the complexity of microservices.

---

## Characteristics of a Modular Monolith
1. **Logical Boundaries**: The application is divided into well-defined modules, each handling a specific domain (e.g., users, budgets, expenses).
2. **Low Coupling**: Modules interact minimally and are designed to be independent.
3. **Explicit Interfaces**: Modules communicate through well-defined APIs or interfaces, avoiding tight integration.
4. **Independent Deployment Readiness**: While part of the same codebase, modules are designed to eventually be split into standalone services if needed.

---

## Key Differences: Modular Monolith vs Traditional Monolith
| **Traditional Monolith**              | **Modular Monolith**                  |
|---------------------------------------|---------------------------------------|
| Tightly coupled code across domains   | Loosely coupled, domain-driven modules |
| Direct access to other module’s data  | Communication via explicit interfaces |
| Harder to scale or refactor           | Easier to refactor or scale incrementally |
| All business logic mixed together     | Logic is encapsulated in domain modules |

---

## Structure of a Modular Monolith
### Folder Structure
Here’s a sample folder structure for a **Python-based modular monolith**:
```
app/
├── main.py                  # Application entry point
├── config.py                # Global configuration
├── shared/                  # Shared utilities (e.g., logging, exceptions)
│   ├── logger.py
│   ├── database.py          # Shared DB connection setup
│   └── errors.py            # Custom exceptions
├── modules/                 # Application modules (domains)
│   ├── users/               # User management module
│   │   ├── __init__.py
│   │   ├── routes.py        # API endpoints
│   │   ├── services.py      # Business logic
│   │   ├── repositories.py  # Database access
│   │   ├── models.py        # SQLAlchemy models
│   │   └── schemas.py       # Pydantic schemas
│   ├── budgets/             # Budget module
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   ├── services.py
│   │   ├── repositories.py
│   │   ├── models.py
│   │   └── schemas.py
│   └── expenses/            # Expense tracking module
│       ├── __init__.py
│       ├── routes.py
│       ├── services.py
│       ├── repositories.py
│       ├── models.py
│       └── schemas.py
├── tests/                   # Tests organized by module
│   ├── test_users.py
│   ├── test_budgets.py
│   └── test_expenses.py
└── migrations/              # Database migrations
```

---

## Communication Between Modules
Modules in a modular monolith communicate using:
1. **Function Calls**: Directly call methods from other modules.
2. **Event Bus/Publisher-Subscriber Pattern** (optional): Use an in-memory event bus for decoupling.

### Example 1: Direct Function Call
If an **Expense Module** needs user data:
```python
# expenses/services.py
from app.modules.users.services import get_user_by_id

def validate_user_and_add_expense(user_id, expense_data):
    user = get_user_by_id(user_id)
    if not user:
        raise ValueError("User does not exist.")
    # Add expense logic here
```

### Example 2: Event-Driven Communication
If you want more decoupling, implement an event bus:
```python
# shared/event_bus.py
class EventBus:
    _subscribers = {}

    @classmethod
    def subscribe(cls, event_name, callback):
        cls._subscribers.setdefault(event_name, []).append(callback)

    @classmethod
    def publish(cls, event_name, data):
        for callback in cls._subscribers.get(event_name, []):
            callback(data)
```

- **Subscribe in one module:**
```python
# budgets/events.py
from shared.event_bus import EventBus

def handle_budget_updated(data):
    print(f"Budget updated: {data}")

EventBus.subscribe("budget_updated", handle_budget_updated)
```

- **Publish in another:**
```python
# budgets/services.py
from shared.event_bus import EventBus

def update_budget(budget_id, updates):
    # Update budget logic here
    EventBus.publish("budget_updated", {"budget_id": budget_id, "updates": updates})
```

---

## Database Design
In a modular monolith, you can:
1. **Use a Shared Database**: All modules share a single database but access only their specific tables.
2. **Encapsulate Database Access**: Each module exposes an API to query its own data, preventing direct access to other modules’ tables.

### Example Schema
- **`users` table** (User Module)
- **`budgets` table** (Budget Module)
- **`expenses` table** (Expense Module, linked to Budgets):
```sql
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    budget_id INT NOT NULL REFERENCES budgets(id),
    amount DECIMAL NOT NULL,
    description TEXT,
    category VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Advantages of a Modular Monolith
1. **Simpler to Develop**: All code is in one repository with no inter-service communication overhead.
2. **Easier to Test**: No need for network mocking; you can test modules as part of a single application.
3. **Well-Prepared for Growth**: Modules are self-contained, making it easier to split them into microservices if necessary.
4. **Encapsulation**: Modules don’t share internal details, reducing tight coupling.
5. **Single Deployment**: Only one deployment artifact to manage.

---

## When to Choose a Modular Monolith
- **Medium-Scale Projects**: Projects that are not too small to benefit from modularity but don’t require full microservices.
- **Growth in Mind**: If you’re expecting the app to grow and want to prepare for a possible migration to microservices.
- **Small Team**: A modular monolith avoids the DevOps and operational complexity of microservices, making it easier for small teams to manage.

---

## Best Practices for a Modular Monolith
1. **Encapsulation**: Ensure modules manage their own data and expose functionality through explicit APIs.
2. **Domain-Driven Design**: Align modules with business domains (e.g., Users, Budgets, Expenses).
3. **Use Shared Utilities Wisely**: Keep shared utilities in a dedicated `shared/` folder and avoid inter-module dependencies.
4. **Prepare for Scalability**: Use patterns like the event bus or APIs to simulate inter-service communication.
5. **Testing**: Test modules independently while ensuring end-to-end integration works as expected.

---

## Conclusion
A modular monolith combines the simplicity of a monolith with the flexibility of modular design. It’s a great way to build a clean, maintainable budgeting app while leaving room to grow into a microservices architecture if needed.

Let me know if you'd like help implementing this or specific examples for any of the components!

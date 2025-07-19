# Stage 4 Tasks

This repository contains three Python applications developed to demonstrate core programming concepts such as classes, file handling, JSON data storage, modular programming, and Git usage.

---

## 1. Student Report Card App

###  Goal:
Manage students' subjects, scores, average, and grade in a terminal app.

###  Features:
- Create and store student records using JSON
- Calculate average and assign grades
- View all or specific student records
- Update scores

###  Key Files:
- `main.py` – CLI for the app

### Commit Messages:
```
git commit -m "Add Student class and JSON save feature"
git commit -m "Fix average score calculation"
```

---

## 2. Bookstore Inventory System

### Goal:
Manage a bookstore inventory including stock, pricing, and author information.

### Features:
- Add, view, and search books
- Save/load inventory using `books.json`
- Round prices using `math.ceil()`
- Separated logic into `inventory.py`

### Key Files:
- `main.py` – CLI for bookstore app
- `inventory.py` – Core logic and helper functions
- `books.json` – Persistent inventory data

### Git Usage:
- Branching for features
```
git checkout -b feature-search
git commit -m "Add book search functionality"
git merge feature-search
```

---

## 3. Personal Budget Tracker

### Goal:
Track personal spending by date and category.

### Features:
- Add transactions with timestamps
- Group spending by category
- Save/load transactions from `transactions.json`
- Organized helper functions in `budget_utils.py`

### Key Files:
- `main.py` – Main interface
- `budget_utils.py` – Transaction class and utility functions
- `transactions.json` – Stored expense data

### Commit Messages:
```
git commit -m "Initial commit: Add Transaction class and file utils"
git commit -m "Add feature to view all transactions"
git commit -m "Implement summary by category function"
```

---
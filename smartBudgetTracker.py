"""
Program: budgetTracker.py
Author: Maiwase Tembo
Modified by: Maiwase Tembo
Date Modified: 09/29/24
Tool takes in inputs for expenses and provides insights
"""
# budgetTracker.py

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Main application window
class BudgetTrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Smart Budget Tracker")
        self.geometry("500x400")

        # Labels and entries for income and expenses
        self.income_label = tk.Label(self, text="Enter Income:")
        self.income_label.pack()

        self.income_entry = tk.Entry(self)
        self.income_entry.pack()

        self.expense_label = tk.Label(self, text="Enter Expense:")
        self.expense_label.pack()

        self.expense_entry = tk.Entry(self)
        self.expense_entry.pack()

        # Dropdown to choose category
        self.category_label = tk.Label(self, text="Select Category:")
        self.category_label.pack()

        self.category = tk.StringVar()
        self.category_dropdown = ttk.Combobox(self, textvariable=self.category)
        self.category_dropdown['values'] = ("Food", "Transport", "Entertainment", "Others")
        self.category_dropdown.pack()

        # Button to add transaction
        self.add_button = tk.Button(self, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack(pady=10)

        # Financial Insights (Placeholder for now)
        self.insights_label = tk.Label(self, text="Financial Insights:")
        self.insights_label.pack(pady=20)

        # View current balance
        self.balance_label = tk.Label(self, text="Current Balance: $0")
        self.balance_label.pack(pady=10)

        # Button to show financial insights (To be extended)
        self.insights_button = tk.Button(self, text="View Insights", command=self.show_insights)
        self.insights_button.pack()

    def add_transaction(self):
        try:
            income = float(self.income_entry.get())
            expense = float(self.expense_entry.get())
            category = self.category.get()

            # Placeholder for real calculations and data storage
            messagebox.showinfo("Transaction Added", f"Income: {income}\nExpense: {expense}\nCategory: {category}")

            # Clear entries after adding
            self.income_entry.delete(0, tk.END)
            self.expense_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid numbers.")

    def show_insights(self):
        # Placeholder for financial insights feature
        messagebox.showinfo("Insights", "This feature will display visual charts of your spending and income.")

# Run the application
if __name__ == "__main__":
    app = BudgetTrackerApp()
    app.mainloop()

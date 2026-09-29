import csv # To process CSV files
import os

HISTORY = "payments.csv"

def view_history(): # Checks if history file exists or not
    if not os.path.exists(HISTORY):
        print("No payments made yet.")
        return
    print("\n--- Payment History ---")
    with open(HISTORY, "r", newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if row[0] == "time":
                continue
            if len(row) >= 6:
                print((row[5] or "-") + " | " + row[0] + " | ₹" + (row[3] or "-") + " | " + (row[4] or "-"))
    print()
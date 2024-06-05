# CREDIT CARD FRAUD DETECTION 
import tkinter as tk
from tkinter import messagebox

def predict_fraud():
    try:
        # Get the input values
        time = float(entry_time.get())
        amount = float(entry_amount.get())
        
        # Simple rule-based approach
        if amount > 1000:
            messagebox.showinfo("Fraud Detection", "Fraudulent Transaction Detected!")
        else:
            messagebox.showinfo("Fraud Detection", "No Fraud Detected.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Credit Card Fraud Detection")

# Create labels and entry fields
tk.Label(root, text="Time (in seconds):").grid(row=0, column=0)
entry_time = tk.Entry(root)
entry_time.grid(row=0, column=1)

tk.Label(root, text="Amount:").grid(row=1, column=0)
entry_amount = tk.Entry(root)
entry_amount.grid(row=1, column=1)

# Create predict button
predict_button = tk.Button(root, text="Predict", command=predict_fraud)
predict_button.grid(row=2, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
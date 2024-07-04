import tkinter as tk
from tkinter import ttk

from count import CryptCalc
# Define global variables
table_frame = None
result_frame = None

def create_tables():
    global table_frame, result_frame
    
    # Retrieve number of rows and columns for each table
    try:
        rows1 = int(entry_rows1.get())
        cols1 = int(entry_cols1.get())
        rows2 = int(entry_rows2.get())
        cols2 = int(entry_cols2.get())
    except ValueError:
        tk.messagebox.showerror("Error", "Please enter valid integers for rows and columns.")
        return

    # Destroy previous widgets (if any)
    if table_frame is not None:
        table_frame.destroy()
    if result_frame is not None:
        result_frame.destroy()

    # Create a new frame for tables
    table_frame = ttk.Frame(root)
    table_frame.grid(row=3, column=0, columnspan=4, padx=20, pady=10)

    # Create Table 1 UI
    ttk.Label(table_frame, text="(r,m)").grid(row=0, column=0, columnspan=cols1)
    table1_entries = []
    for i in range(rows1):
        row_entries = []
        for j in range(cols1):
            entry = ttk.Entry(table_frame, width=10)
            entry.grid(row=i+1, column=j, padx=5, pady=5)
            row_entries.append(entry)
        table1_entries.append(row_entries)

    # Create Table 2 UI
    ttk.Label(table_frame, text="Ga,b").grid(row=0, column=cols1+2, columnspan=cols2)  # Adjust column to create space between tables
    table2_entries = []
    for i in range(rows2):
        row_entries = []
        for j in range(cols2):
            entry = ttk.Entry(table_frame, width=10)
            entry.grid(row=i+1, column=cols1+2+j, padx=5, pady=5)  # Adjust column to create space between tables
            row_entries.append(entry)
        table2_entries.append(row_entries)
    
    # Fx input
    ttk.Label(root, text="Fx (1111 => x^3+x^2+x+1):").grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)
    entry_fx = ttk.Entry(root, width=15)
    entry_fx.grid(row=4, column=1, padx=5, pady=5)
    
    #Create Button calculate
    ttk.Button(root, text="Calculate", command=lambda: calculate_results(table1_entries, table2_entries, entry_fx)).grid(row=5, columnspan=4, pady=10)

def calculate_results(table1_entries, table2_entries, fx_entry):
    global result_frame
    
    # Get input values from Table 1 entries
    table1_values = []
    for row in table1_entries:
        row_values = []
        for entry in row:
            value = entry.get()
            if is_binary_string(value):  # Check if input is a valid binary string
                row_values.append(value)
            else:
                tk.messagebox.showerror("Error", "Please enter valid binary strings (only '0's and '1's) in Table 1.")
                return
        table1_values.append(row_values)

    # Get input values from Table 2 entries
    table2_values = []
    for row in table2_entries:
        row_values = []
        for entry in row:
            value = entry.get()
            if is_binary_string(value):  # Check if input is a valid binary string
                row_values.append(value)
            else:
                tk.messagebox.showerror("Error", "Please enter valid binary strings (only '0's and '1's) in Table 2.")
                return
        table2_values.append(row_values)

    # Perform calculation
    fx = fx_entry.get()
    fx =  [int(char) for char in fx]
    calc = CryptCalc(fx)
    results = calc.multiply_matrices(table1_values,table2_values)
    

    # Display results in a new frame
    result_frame = ttk.Frame(root)
    result_frame.grid(row=6, column=0, columnspan=4, padx=20, pady=10)

    ttk.Label(result_frame, text="Results").grid(row=0, column=0, columnspan=len(results[0]))

    for i in range(len(results)):
        for j in range(len(results[i])):
            ttk.Label(result_frame, text=results[i][j]).grid(row=i+1, column=j, padx=5, pady=5)

def is_binary_string(s):
    """ Check if a string consists only of '0's and '1's """
    return all(char in '01' for char in s)

root = tk.Tk()
root.title("Input Tables")

# Table 1 size input
ttk.Label(root, text="(r,m) Size (Rows x Columns):").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_rows1 = ttk.Entry(root, width=5)
entry_rows1.grid(row=0, column=1, padx=5, pady=5)
ttk.Label(root, text="x").grid(row=0, column=2, padx=5, pady=5)
entry_cols1 = ttk.Entry(root, width=5)
entry_cols1.grid(row=0, column=3, padx=5, pady=5)

# Table 2 size input
ttk.Label(root, text="G a,b Size (Rows x Columns):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_rows2 = ttk.Entry(root, width=5)
entry_rows2.grid(row=1, column=1, padx=5, pady=5)
ttk.Label(root, text="x").grid(row=1, column=2, padx=5, pady=5)
entry_cols2 = ttk.Entry(root, width=5)
entry_cols2.grid(row=1, column=3, padx=5, pady=5)

# Button to create tables
ttk.Button(root, text="Create Matrix", command=create_tables).grid(row=2, columnspan=4, pady=10)

root.mainloop()

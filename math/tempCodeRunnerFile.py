  # Parallel Resistance Inputs
    tk.Label(window, text="Enter Resistor 1 (Ω):", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
    r1_entry = tk.Entry(window, font=("Arial", 12), width=15)
    r1_entry.pack(pady=5)

    tk.Label(window, text="Enter Resistor 2 (Ω):", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
    r2_entry = tk.Entry(window, font=("Arial", 12), width=15)
    r2_entry.pack(pady=5)

    tk.Label(window, text="Enter Resistor 3 (Ω) (Optional):", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
    r3_entry = tk.Entry(window, font=("Arial", 12), width=15)
    r3_entry.pack(pady=5)

    tk.Button(
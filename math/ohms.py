import tkinter as tk

def run_gui():
    global voltage_entry, current_entry, resistance_entry, r1_entry, r2_entry, r3_entry, result_label, window

    window = tk.Tk()
    window.title("Ohm's Law Calculator")
    window.geometry("600x700")  # Increased size for better layout
    window.configure(bg="#2C3E50")  # 🔹 Dark blue-gray background

    # Title Label
    tk.Label(window, text="Ohm's Law Calculator", font=("Arial", 16, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

    # Voltage Input
    tk.Label(window, text="Enter Voltage (V):", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
    voltage_entry = tk.Entry(window, font=("Arial", 12), width=15)
    voltage_entry.pack(pady=5)

    # Current Input
    tk.Label(window, text="Enter Current (I):", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
    current_entry = tk.Entry(window, font=("Arial", 12), width=15)
    current_entry.pack(pady=5)

    # Resistance Input
    tk.Label(window, text="Enter Resistance (Ω):", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
    resistance_entry = tk.Entry(window, font=("Arial", 12), width=15)
    resistance_entry.pack(pady=5)

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

    # Parallel Resistance Button
    tk.Button(window, text="Calculate Parallel Resistance", command=calculate_parallel_resistance, font=("Arial", 12), bg="#9B59B6", fg="white", width=25).pack(pady=3)

    # Ohm’s Law Buttons
    tk.Button(window, text="Calculate Voltage", command=calculate_voltage, font=("Arial", 12), bg="#3498DB", fg="white", width=20).pack(pady=3)
    tk.Button(window, text="Calculate Current", command=calculate_current, font=("Arial", 12), bg="#2ECC71", fg="white", width=20).pack(pady=3)
    tk.Button(window, text="Calculate Resistance", command=calculate_resistance, font=("Arial", 12), bg="#E74C3C", fg="white", width=20).pack(pady=3)

    # Result Label
    result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="yellow", bg="#2C3E50")
    result_label.pack(pady=10)

    window.mainloop()


# Ohm’s Law Calculations
def calculate_voltage():
    try:
        current = float(current_entry.get())
        resistance = float(resistance_entry.get())
        voltage = current * resistance
        result_label.config(text=f"Voltage = {voltage:.5f} V", fg="yellow")
    except ValueError:
        result_label.config(text="❌ Enter valid numbers!", fg="red")

def calculate_current():
    try:
        voltage = float(voltage_entry.get())
        resistance = float(resistance_entry.get())
        if resistance == 0:
            result_label.config(text="❌ Error: Resistance cannot be zero!", fg="red")
            return
        current = voltage / resistance
        result_label.config(text=f"Current = {current:.5f} A", fg="yellow")
    except ValueError:
        result_label.config(text="❌ Enter valid numbers!", fg="red")

def calculate_resistance():
    try:
        voltage = float(voltage_entry.get())
        current = float(current_entry.get())
        if current == 0:
            result_label.config(text="❌ Error: Current cannot be zero!", fg="red")
            return
        resistance = voltage / current
        result_label.config(text=f"Resistance = {resistance:.5f} Ω", fg="yellow")
    except ValueError:
        result_label.config(text="❌ Enter valid numbers!", fg="red")


# Parallel Resistance Calculation
def calculate_parallel_resistance():
    try:
        # Get values, default to 0 if empty
        r1 = float(r1_entry.get()) if r1_entry.get() else 0
        r2 = float(r2_entry.get()) if r2_entry.get() else 0
        r3 = float(r3_entry.get()) if r3_entry.get() else 0

        # Filter out zero values
        resistors = [r for r in [r1, r2, r3] if r > 0]

        if len(resistors) < 2:
            result_label.config(text="❌ Enter at least two resistances!", fg="red")
            return

        # Parallel Resistance Formula: 1 / (1/R1 + 1/R2 + 1/R3)
        reciprocal_sum = sum(1/r for r in resistors)  # Sum of reciprocals
        r_eq = 1 / reciprocal_sum if reciprocal_sum else float('inf')  # Avoid division by zero

        result_label.config(text=f"Parallel Resistance = {r_eq:.5f} Ω", fg="yellow")
    
    except ValueError:
        result_label.config(text="❌ Enter valid numbers!", fg="red")


# Run GUI
run_gui()

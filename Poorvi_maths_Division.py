import tkinter as tk
from tkinter import ttk, messagebox

class DivisionVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Long Division - Canvas Visual (Correct Quotient)")
        self.geometry("1200x900")
        self.configure(bg="white")
        self.setup_ui()

    def setup_ui(self):
        input_frame = ttk.Frame(self)
        input_frame.pack(pady=10)

        ttk.Label(input_frame, text="Dividend:", font=("Arial", 12)).grid(row=0, column=0, padx=10)
        self.entry_dividend = ttk.Entry(input_frame, width=20)
        self.entry_dividend.grid(row=0, column=1)

        ttk.Label(input_frame, text="Divisor:", font=("Arial", 12)).grid(row=1, column=0, padx=10)
        self.entry_divisor = ttk.Entry(input_frame, width=20)
        self.entry_divisor.grid(row=1, column=1)

        ttk.Button(self, text="Visualize Division", command=self.visualize_division).pack(pady=10)

        self.canvas = tk.Canvas(self, width=750, height=500, bg="white", bd=2, relief="sunken")
        self.canvas.pack()

    def visualize_division(self):
        self.canvas.delete("all")

        dividend_str = self.entry_dividend.get()
        divisor_str = self.entry_divisor.get()

        if not dividend_str.isdigit() or not divisor_str.isdigit() or int(divisor_str) == 0:
            messagebox.showerror("Input Error", "Please enter a valid whole number dividend and a non-zero divisor.")
            return

        dividend = int(dividend_str)
        divisor = int(divisor_str)
        digits = list(map(int, dividend_str))
        remainder = 0
        quotient_digits = []

        step_y = 80
        x_start = 100
        x_gap = 30
        y = step_y + 30
        first_division_done = False

        # Draw divisor and dividend bracket
        self.canvas.create_text(x_start, step_y, text=divisor, font=("Courier", 16))
        self.canvas.create_line(x_start + 30, step_y - 15, x_start + 30 + len(digits) * x_gap, step_y - 15)
        self.canvas.create_line(x_start + 30, step_y - 15, x_start + 30, step_y + 20)

        # Draw dividend digits
        for i, d in enumerate(digits):
            self.canvas.create_text(x_start + 60 + i * x_gap, step_y, text=str(d), font=("Courier", 25))

        # Division logic
        current = 0
        for i, digit in enumerate(digits):
            current = remainder * 10 + digit
            if current < divisor and not first_division_done:
                # Before first division, skip showing 0s
                remainder = current
                quotient_digits.append("")  # empty string for visual alignment
                continue

            first_division_done = True
            q_digit = current // divisor
            product = q_digit * divisor
            remainder = current - product
            quotient_digits.append(str(q_digit))

            x_pos = x_start + 60 + i * x_gap
            self.canvas.create_text(x_pos, step_y - 30, text=str(q_digit), font=("Courier", 25))

            # Draw current and subtraction
            self.canvas.create_text(x_pos, y, text=str(current), font=("Courier", 25))
            text_str = '-' + str(product)
            text_width = len(text_str) * 8  # Approx width per char in Courier
            self.canvas.create_text(x_pos - text_width // 2, y + 20, text=text_str, font=("Courier", 25))
            self.canvas.create_line(x_pos - text_width // 2, y + 30, x_pos + text_width // 2, y + 30)

            # Draw arrow
            if i < len(digits) - 1:
                self.canvas.create_text(x_start + 60 + (i + 1) * x_gap, y + 45, text='↓', font=('Arial', 10 ))

            y += 60  # next step

        # Final remainder
        self.canvas.create_text(x_start + 60 + len(digits) * x_gap, y, text=str(remainder), font=("Courier", 25))


# Run the app
if __name__ == "__main__":
    app = DivisionVisualizer()
    app.mainloop()

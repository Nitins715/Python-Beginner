import tkinter as tk
import random

# Game settings
ROWS = 3
COLS = 3
MAX_LINES = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}

# Generate slot machine result
def get_spin():
    all_symbols = []
    for symbol, count in symbol_count.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(COLS):
        column = random.sample(all_symbols, ROWS)
        columns.append(column)

    return columns

# Check winnings
def check_winnings(columns, lines, bet):
    winnings = 0
    winning_lines = []

    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            if column[line] != symbol:
                break
        else:
            winnings += symbol_value[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# GUI App
class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine 🎰")

        self.balance = 100

        # Balance label
        self.balance_label = tk.Label(root, text=f"Balance: $ {self.balance}", font=("Arial", 14))
        self.balance_label.pack(pady=10)

        # Bet input
        self.bet_entry = tk.Entry(root)
        self.bet_entry.insert(0, "10")
        self.bet_entry.pack(pady=5)

        # Lines input
        self.lines_entry = tk.Entry(root)
        self.lines_entry.insert(0, "1")
        self.lines_entry.pack(pady=5)

        # Spin button
        self.spin_button = tk.Button(root, text="SPIN", command=self.spin)
        self.spin_button.pack(pady=10)

        # Slot display
        self.slot_labels = []
        for r in range(ROWS):
            row = []
            frame = tk.Frame(root)
            frame.pack()
            for c in range(COLS):
                label = tk.Label(frame, text="-", width=5, height=2, font=("Arial", 18), borderwidth=2, relief="solid")
                label.pack(side="left", padx=5, pady=5)
                row.append(label)
            self.slot_labels.append(row)

        # Result label
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

    def spin(self):
        try:
            bet = int(self.bet_entry.get())
            lines = int(self.lines_entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input!")
            return

        if lines < 1 or lines > MAX_LINES:
            self.result_label.config(text="Lines must be 1-3")
            return

        total_bet = bet * lines

        if total_bet > self.balance:
            self.result_label.config(text="Not enough balance!")
            return

        slots = get_spin()

        # Display slots
        for c in range(COLS):
            for r in range(ROWS):
                self.slot_labels[r][c].config(text=slots[c][r])

        winnings, winning_lines = check_winnings(slots, lines, bet)

        self.balance += winnings - total_bet
        self.balance_label.config(text=f"Balance: $ {self.balance}")

        if winnings > 0:
            self.result_label.config(text=f"You won $ {winnings} on lines {winning_lines}")
        else:
            self.result_label.config(text="No win, try again!")

# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()

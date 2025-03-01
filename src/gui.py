import customtkinter as ctk
import webbrowser
from problem_loader import load_problems, get_random_problem

class ProblemGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Random Problem Generator")
        self.geometry("500x400")  # Increased window size to fit counters
        self.problems = load_problems("src/problems.csv")  # Ensure the path is correct
        self.create_widgets()
        self.update_counters()  # Initialize counters

    def create_widgets(self):
        """Create buttons, labels, and counters for the GUI."""
        # Label for difficulty selection
        self.label = ctk.CTkLabel(self, text="Select Difficulty:")
        self.label.pack(pady=10)

        # Buttons for Easy, Medium, and Hard
        self.easy_button = ctk.CTkButton(
            self,
            text="Easy",
            command=lambda: self.select_problem("Easy")
        )
        self.easy_button.pack(pady=5)

        self.medium_button = ctk.CTkButton(
            self,
            text="Medium",
            command=lambda: self.select_problem("Medium")
        )
        self.medium_button.pack(pady=5)

        self.hard_button = ctk.CTkButton(
            self,
            text="Hard",
            command=lambda: self.select_problem("Hard")
        )
        self.hard_button.pack(pady=5)

        # Label to display the selected problem
        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.pack(pady=20)

        # Frame to hold the counters
        self.counter_frame = ctk.CTkFrame(self)
        self.counter_frame.pack(pady=10)

        # Labels for counters
        self.easy_counter_label = ctk.CTkLabel(self.counter_frame, text="Easy: 0")
        self.easy_counter_label.pack(pady=5)

        self.medium_counter_label = ctk.CTkLabel(self.counter_frame, text="Medium: 0")
        self.medium_counter_label.pack(pady=5)

        self.hard_counter_label = ctk.CTkLabel(self.counter_frame, text="Hard: 0")
        self.hard_counter_label.pack(pady=5)

        self.total_counter_label = ctk.CTkLabel(self.counter_frame, text="Total: 0")
        self.total_counter_label.pack(pady=5)

    def select_problem(self, difficulty):
        """Select and display a random problem of the given difficulty."""
        problem = get_random_problem(self.problems, difficulty)
        if problem:
            self.result_label.configure(text=f"{problem['Problem Name']}")
            webbrowser.open(problem["URL"])  # Open the URL directly
        else:
            self.result_label.configure(text="No problems found for this difficulty.")

    def update_counters(self):
        """Update the counters for Easy, Medium, Hard, and Total problems."""
        easy_count = len([p for p in self.problems if p["Difficulty"].lower() == "easy"])
        medium_count = len([p for p in self.problems if p["Difficulty"].lower() == "medium"])
        hard_count = len([p for p in self.problems if p["Difficulty"].lower() == "hard"])
        total_count = len(self.problems)

        # Update the counter labels
        self.easy_counter_label.configure(text=f"Easy: {easy_count}")
        self.medium_counter_label.configure(text=f"Medium: {medium_count}")
        self.hard_counter_label.configure(text=f"Hard: {hard_count}")
        self.total_counter_label.configure(text=f"Total: {total_count}")
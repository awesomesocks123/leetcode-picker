import customtkinter as ctk
import webbrowser
from problem_loader import load_problems, get_random_problem

class ProblemGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Random Problem Generator")
        self.geometry("400x250")
        self.problems = load_problems("src/problems.csv")  # Ensure the path is correct
        self.create_widgets()

    def create_widgets(self):
        """Create buttons and labels for the GUI."""
        self.label = ctk.CTkLabel(self, text="Select Today's Review LeetCode Problem Based on Difficulty:")
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

    def select_problem(self, difficulty):
        """Select and display a random problem of the given difficulty."""
        problem = get_random_problem(self.problems, difficulty)
        if problem:
            self.result_label.configure(text=f"{problem['Problem Name']}")
            webbrowser.open(problem["URL"])  # Open the URL directly
        else:
            self.result_label.configure(text="No problems found for this difficulty.")
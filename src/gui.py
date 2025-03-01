import customtkinter as ctk
import webbrowser
from problem_loader import load_problems, get_random_problem

class ProblemGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Random Problem Generator")
        self.geometry("300x250")  # Increased window size to fit counters
        self.problems = load_problems("src/problems.csv")  
        self.create_widgets()
        self.update_counters()  # Initialize counters

    def create_widgets(self):
        """Create buttons, labels, and counters for the GUI."""
        # Label for difficulty selection
        self.label = ctk.CTkLabel(self, text="Select Difficulty:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Buttons for Easy, Medium, and Hard
        self.easy_button = ctk.CTkButton(
            self,
            text="Easy",
            command=lambda: self.select_problem("Easy")
        )
        self.easy_button.grid(row=1,column=0, padx=10, pady=5, stick='w')

        self.medium_button = ctk.CTkButton(
            self,
            text="Medium",
            command=lambda: self.select_problem("Medium")
        )
        self.medium_button.grid(row=2,column=0, padx=10, pady=5, stick='w')

        self.hard_button = ctk.CTkButton(
            self,
            text="Hard",
            command=lambda: self.select_problem("Hard")
        )
        self.hard_button.grid(row=3,column=0, padx=10, pady=5, stick='w')

        # Label to display the selected problem
        self.result_label = ctk.CTkLabel(self, text="")
        self.result_label.grid(row=4, column=0, columnspan=6, padx=10, pady=20, sticky="w")

        # Frame to hold the counters    s
        self.counter_frame = ctk.CTkFrame(self)
        
        self.counter_frame.grid(row=1, column=1, rowspan=4, padx=20, pady=10, sticky="nsew")

        # Labels for counters
        self.total_counter_label = ctk.CTkLabel(self.counter_frame, text="Total: 0")
        self.total_counter_label.pack(pady=5, padx=10)

        self.easy_counter_label = ctk.CTkLabel(self.counter_frame, text="Easy: 0")
        self.easy_counter_label.pack(pady=5, padx=10)

        self.medium_counter_label = ctk.CTkLabel(self.counter_frame, text="Medium: 0")
        self.medium_counter_label.pack(pady=5, padx=10)

        self.hard_counter_label = ctk.CTkLabel(self.counter_frame, text="Hard: 0")
        self.hard_counter_label.pack(pady=5, padx=10)

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
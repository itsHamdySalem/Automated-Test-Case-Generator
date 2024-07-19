import tkinter as tk
from tkinter import messagebox
from test_case_generator import AutomatedTestCaseGenerator

class TestCaseGeneratorUI:
    def __init__(self, root):
        """
        Initialize the TestCaseGeneratorUI object.

        Args:
            root (tk.Tk): The root Tkinter window.
        """
        self.root = root
        self.root.title("Automated Test Case Generator")
        self.root.geometry("724x512")
        self.create_widgets()

    def create_widgets(self):
        """
        Create and layout the widgets for the UI.
        """
        tk.Label(self.root, text="Enter Server Global Options (comma-separated):", font=("Arial", 14)).pack(pady=20)

        self.options_entry = tk.Entry(self.root, width=60, font=("Arial", 14))
        self.options_entry.pack(pady=10)

        generate_button = tk.Button(self.root, text="Generate Test Cases", command=self.generate_test_cases_ui, font=("Arial", 14), bg='#4CAF50', fg='white', borderwidth=2, relief="flat", padx=10, pady=5)
        generate_button.pack(pady=30)

    def generate_test_cases_ui(self):
        """
        Handle the event when the "Generate Test Cases" button is clicked.
        Reads the options input, generates test cases, and saves them to a CSV file.
        """
        options_input = self.options_entry.get().strip()
        if not options_input:
            messagebox.showerror("Error", "Options list cannot be empty.")
            return
        
        options = [option.strip() for option in options_input.split(',')]
        if len(options) != len(set(options)):
            messagebox.showerror("Error", "Options list should have unique elements.")
            return

        try:
            test_case_generator = AutomatedTestCaseGenerator(options)
            test_case_generator.generate_test_cases()
            test_case_generator.generate_csv_file("output/server_test_cases.csv")
            messagebox.showinfo("Success", "Test cases generated and saved to 'output/server_test_cases.csv'.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

def run_ui():
    """
    Main entry point for running the TestCaseGeneratorUI.
    """
    root = tk.Tk()
    app = TestCaseGeneratorUI(root)
    root.mainloop()

if __name__ == "__main__":
    run_ui()

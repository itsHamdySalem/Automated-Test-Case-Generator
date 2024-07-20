from typing import List
import logging
import itertools
import os
import csv
import re

class AutomatedTestCaseGenerator:
    def __init__(self, options: List[str], values: List[str] = ['TRUE', 'FALSE', 'NA'], client_types: List[str] = ['Master', 'Slave']):
        """
        Initialize AutomatedTestCaseGenerator object

        Args:
            options (List[str]): List of server global options.
            values (List[str], optional): List of possible values for each option. Defaults to ['TRUE', 'FALSE', 'NA'].
            client_types (List[str], optional): List of client types. Defaults to ['Master', 'Slave'].
        """
        if not options or len(options) < 1:
            raise ValueError("Options list cannot be empty.")
        if len(options) != len(set(options)):
            raise ValueError("Options list should have unique elements.")
        if any(self.contains_special_characters(option) for option in options):
            raise ValueError("Options list cannot contains special characters.")
        
        self.options = options
        self.values = values
        self.client_types = client_types
        self.test_cases = []
        self.headers = []

        logging.basicConfig(level=logging.INFO)

    def contains_special_characters(self, text: str) -> bool:
        """
        Check if the text contains special characters.

        Args:
            text (str): The text to check.

        Returns:
            bool: True if special characters are found, False otherwise.
        """
        # Regex to match any character that is not alphanumeric or underscore
        return bool(re.search(r'[^a-zA-Z0-9_]', text))

    def generate_headers(self):
        """
        Generate column headers for the output csv file
        """
        self.headers = ["TestCase ID"]
        for client_type in self.client_types:
            for option in self.options:
                self.headers.append(f"{client_type} Option For {option}")
        self.headers.append("Valid TC")
        for option in self.options:
            self.headers.append(f"Expected {option}")

    def generate_all_combinations(self):
        """
        Generate all possible combinations of test cases
        """
        n = len(self.client_types) * len(self.options)
        combinations = list(itertools.product(self.values, repeat=n))
        self.test_cases = [list(combination) for combination in combinations]
        
        logging.info(f"Generated {len(self.test_cases)} test case combinations.")

    def generate_expected_output(self):
        """
        Generate the expected output of the generated test cases
        """
        for idx, test_case in enumerate(self.test_cases):
            valid_tc = True
            current_test_case = test_case.copy()
            expected_options = ['TRUE'] * len(self.options)

            for i in range(len(self.options)):
                if current_test_case[i] == 'FALSE':
                    expected_options[i] = 'FALSE'

            for i in range(len(self.options), 2 * len(self.options)):
                slave_value = current_test_case[i]
                master_value = expected_options[i - len(self.options)]
                if slave_value != 'NA' and slave_value != master_value:
                    valid_tc = False
                    break

            current_test_case.insert(0, idx + 1)
            if not valid_tc:
                current_test_case.append('NO')
                current_test_case.extend(['NA'] * len(expected_options))
            else:
                current_test_case.append('YES')
                current_test_case.extend(expected_options)
            
            self.test_cases[idx] = current_test_case
        
        logging.info("Expected outputs and validity generated for all test cases.")

    def generate_test_cases(self):
        """
        Generate test cases, expected output, and headers
        """
        self.generate_headers()
        self.generate_all_combinations()
        self.generate_expected_output()
        
        logging.info("Test cases generated.")

    def generate_csv_file(self, csv_file_path: str):
        """
        Write the generated test cases to a csv file

        Args:
            csv_file_path (str): Path to the csv file
        """
        if not self.test_cases:
            raise ValueError("No test cases to write. Please generate test cases first using generate_test_cases().")
        
        directory = os.path.dirname(csv_file_path)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        try:
            with open(csv_file_path, 'w', newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(self.headers)
                for test_case in self.test_cases:
                    csv_writer.writerow(test_case)
            logging.info(f"Test cases written to {csv_file_path}")
        except PermissionError:
            logging.error(f"Permission error: Cannot write to the file {csv_file_path}")
            raise
        except FileNotFoundError:
            logging.error(f"File not found error: {csv_file_path}")
            raise
        except Exception as e:
            logging.error(f"An error occurred while writing to the file: {e}")
            raise

# Example usage:
if __name__ == "__main__":
    options = ['BufferData', 'TimeOut']
    test_case_generator = AutomatedTestCaseGenerator(options=options)
    test_case_generator.generate_test_cases()
    test_case_generator.generate_csv_file("Assignment1/output/server_test_cases.csv")

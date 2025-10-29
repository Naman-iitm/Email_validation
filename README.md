Email Validation Script
This is a simple Python script for basic email format validation. It checks whether the inputted email meets common requirements and displays user-friendly error messages in case of mistakes or improper formatting.
Features
	•	Checks minimum email length (6+ characters)
	•	Ensures the first character is a letter
	•	Validates the presence and count of ‘@’ (must appear exactly once)
	•	Confirms the domain: proper position of ‘.’ at the end (supports ‘.com’, ‘.in’, etc.)
	•	Detects and rejects spaces, uppercase letters, and invalid special characters
	•	Provides clear error/success messages in the console
	•	Easy to use; runs in any Python 3 environment
Usage

# Clone or download the script
git clone https://github.com/yourusername/your-repo.git

# Go to the project directory
cd your-repo

# Run the script (Python 3 required)
python Email_validation.py

You will be prompted to enter an email address, and will receive instant feedback about its validity.
Example Output
--------------------------------------------------------------------------------------------------
Enter your email: user@gmail.com
Email format is right buddy !!!
--------------------------------------------------------------------------------------------------
or
--------------------------------------------------------------------------------------------------
Enter your email: user@@gmail.com
Oops! you have entered @ more than one time :-)
--------------------------------------------------------------------------------------------------

or
--------------------------------------------------------------------------------------------------
Enter your email: UsEr@Gmail.com
Oops! You have entered some space or some uppercase or any special character in your email
--------------------------------------------------------------------------------------------------
How It Works
	•	The script checks if your email follows these basic rules:
	•	At least 6 characters
	•	Starts with an alphabet letter
	•	Contains exactly one ‘@’
	•	Ends with a proper domain (like ‘.com’, ‘.in’)
	•	No uppercase letters, spaces, or invalid special characters.
	•	If all these conditions are satisfied, you get a success message; otherwise, a clear hint is given.
Customization
You can modify the script to:
	•	Support more top-level domains (TLDs)
	•	Allow certain special characters or stricter rules
	•	Improve language for local audiences
License
This project is released under the MIT License.
Replace any placeholder URLs with your rea

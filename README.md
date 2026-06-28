🤖 Automaton Leads
A tool to extract and organize potential customer contacts (leads) from text files, identifying names, phone numbers, and email addresses.

🚀 What this project does
. Reads a plain text file (conversas.txt) containing raw conversation data

. Uses Regular Expressions (Regex) to identify and extract:

 . 📧 Email addresses

 . 📞 Phone numbers (Brazilian and international formats)

 . 👤 Person names

. Saves the extracted data into a structured CSV file (leads.csv) for easy import into spreadsheets or CRMs.

📁 Project Structure
text
automaton_leads/
├── app.py            # Main application script
├── conversas.txt     # Input file with raw text data
├── leads.csv         # Output file with extracted leads
├── .gitignore        # Git ignore file
└── README.md         # This file
🧩 Technologies Used
. Python 3.10+

. Regular Expressions (re)

. CSV module

📦 How to Run
1. git clone https://github.com/alcitech7-oss/automaton_leads.git
cd automaton_leads

2 . Prepare your data: Replace the content of conversas.txt with your own raw text.

3 . Run the script:
python app.py

4 . Check the results: The extracted leads will be saved in leads.csv.

✅ Project Status
Project validated and tested in a clean environment (cloned from scratch).

. ✔️ Dependencies successfully installed

. ✔️ Core features validated

. ✔️ Structure and documentation reviewed

. ✔️ Ready for use and demonstration

📌 Development History
. Initial structure: Lead extraction with regex

. Organization: Modular code and documentation

. Documentation: Updated README and added requirements.txt

. Final validation: Project tested and validated from scratch

🔮 Future improvements
. Add support for more file formats (.docx, .pdf)

. Implement a simple graphical interface

. Integrate with an API to validate emails and phone numbers

🙏 Credits & Original Work
This project was developed by alcitech7-oss.

📄 License
MIT — use, modify, and share freely.


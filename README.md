# 🤖 Automaton Leads

A tool to extract and organize potential customer contacts (leads) from text files, identifying names, phone numbers, and email addresses.

---

## 🚀 What this project does

- Reads a plain text file (`conversas.txt`) containing raw conversation data
- Uses **Regular Expressions (Regex)** to identify and extract:
  - 📧 Email addresses
  - 📞 Phone numbers (Brazilian and international formats)
  - 👤 Person names
- Saves the extracted data into a structured CSV file (`leads.csv`) for easy import into spreadsheets or CRMs.

---

## 📁 Project Structure
automaton_leads/
├── app.py # Main application script
├── conversas.txt # Input file with raw text data
├── leads.csv # Output file with extracted leads
├── .gitignore # Git ignore file
└── README.md # This file


---

## 🧩 Technologies Used

- Python 3.10+
- Regular Expressions (`re`)
- CSV module

---

## 📦 How to Run
## 📦 How to Run

1.  **Prepare your data:** Replace the content of `conversas.txt` with your own raw text.

2.  **Run the script:**
    ```bash
    python app.py
    ```

3.  **Check the results:** The extracted leads will be saved in `leads.csv`.



   ## 🔮 Future improvements

- Add support for more file formats (`.docx`, `.pdf`)
- Implement a simple graphical interface
- Integrate with an API to validate emails and phone numbers

🙏 Credits & Original Work
This project was developed by alictech7-oss.
📄 License
MIT — use, modify, and share freely.



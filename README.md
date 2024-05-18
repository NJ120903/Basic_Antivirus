## Basic_Antivirus


This Python script serves as a basic antivirus tool. It scans the current directory for `.exe` files and checks their MD5 hashes against a database of known malicious signatures.

### Features
- **MD5 Hash Calculation:** Accurately calculates the MD5 hash of file content.
- **Database Comparison:** Compares the calculated hash against a database of known malicious hashes.

### How to Use
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/basic-antivirus.git
   cd basic-antivirus
   ```
2. **Add Your Own Database:**
   - Open the script and add MD5 hashes of known malicious files to the `db` list.
3. **Run the Script:**
   ```bash
   python basic_antivirus.py
   ```

### Note
This is a basic antivirus tool. You need to add your own database of known malicious hashes to the `db` list for it to be effective.

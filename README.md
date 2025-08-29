### IGR-Orissa-Data-Entry-Bot
This bot automatically fills property data (Khata Number, Plot Number, Area) on the Odisha government's IGR website from an Excel file. It saves hours of manual data entry work.

IGR Data entry Bot - Step-by-Step Setup Guide

## STEP 1: Install Required Software

# 1.1 Install Python
- Go to https://www.python.org/downloads/
- Download Python (latest version)
- During installation, CHECK the box "Add Python to PATH"
- Click "Install Now"
- Restart your computer after installation

# 1.2 Install Google Chrome Browser
- Download and install Chrome from https://www.google.com/chrome/
- Make sure Chrome is updated to the latest version

## STEP 2: Prepare Your Files

# 2.1 Create a New Folder
- Create a new folder on your Desktop (example: "IGR Bot - EC")
- This folder will contain all your files

# 2.2 Save the Bot Code
- Copy the igro_bot.py code into a text file
- Save it as "igro_bot.py" in your "IGR Bot - EC" folder
- Make sure the file extension is .py (not .txt)

# 2.3 Prepare Your Excel File
- Create an Excel file named "data.xlsx" in the same folder
- The Excel file should have 3 columns with these EXACT headers:
  Column A: Khata
  Column B: Plot  
  Column C: Area

Example Excel format:
Khata       Plot    Area
123/456     789     0.25
124/457     790     0.30
125/458     791     0.20

# Important Notes about Excel Data:
- Only numbers, slash (/) and dash (-) are allowed in Khata and Plot fields
- Only numbers and decimal points (.) are allowed in Area field
- If any field is blank, the bot will use the previous row's value for that field
- The bot automatically cleans invalid characters from your data

## STEP 3: Install Required Python Packages

# 3.1 Open Command Prompt
- Press Windows Key + R
- Type "cmd" and press Enter
- A black window (Command Prompt) will open

# 3.2 Navigate to Your Folder
- In the command prompt, type:
  cd "C:\Users\abhis\OneDrive\Desktop\IGR Bot - EC"
- Press Enter
- (Replace with your actual folder path if different)

# 3.3 Install Packages
- Copy and paste this command in the command prompt:
  pip install pandas selenium webdriver-manager
- Press Enter
- Wait for installation to complete (may take 2-3 minutes)

## STEP 4: Running the Bot with Chrome Debugging

# 4.1 Start Chrome with Debugging Port
- IMPORTANT: Close all Chrome windows first
- Open Command Prompt (Windows Key + R, type "cmd", press Enter)
- Type this command and press Enter:
  chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeData"
- Chrome will open in debugging mode
- Keep this Command Prompt window open

# 4.2 Manual Login Process
- In the Chrome window that opened, navigate to https://www.igrodisha.gov.in/
- Login manually with your credentials:
  1. Enter your ID and password
  2. Complete OTP verification
  3. Navigate to "Apply Encumbrance Certificate" page
  4. Reach the page where you enter Khata/Plot/Area details
- Keep Chrome open and stay on this page

# 4.3 Start the Bot
- Open a NEW Command Prompt window (keep the first one open)
- Navigate to your bot folder:
  cd "C:\Users\abhis\OneDrive\Desktop\IGR Bot - EC"
- Start the bot:
  python igro_bot.py
- When prompted, choose option 2 (Use existing browser)
- Press ENTER when you see: "Press ENTER when you're ready to start data entry..."

# 4.4 Monitor Progress
- The bot will show progress messages like:
  "Processing record 1: Khata=123/456, Plot=789, Area=0.25"
  "✓ Successfully added record 1"
- Let the bot complete all records
- DO NOT close any windows during processing

# 4.5 Processing Multiple Files (Rerun Without Login)
- After the first run completes, you can process more data without logging in again:
  1. Update your "data.xlsx" file with new data
  2. Run the bot again: python igro_bot.py
  3. Choose option 2 (Use existing browser)
  4. No need to login again - Chrome stays logged in!

N.B. - By default, the delay timer is set to 1 second. You can change it in the "igro_bot.py" file by searching for the following and changing it:
# ✅ Force a small delay after clicking
time.sleep(1)

## STEP 5: What to Expect

Normal Operation:
- Bot fills each field automatically
- Waits for page loading
- Clicks "Add" button
- Moves to next record
- Shows success/failure messages

If Errors Occur:
- Bot handles website alerts automatically
- Skips problematic records and continues with next ones
- Shows error messages in the command prompt
- Continues until all records are processed

When Complete:
- You'll see "All records processed successfully!"
- Browser remains open for you to verify results
- You can process more files without logging in again

TROUBLESHOOTING

Problem: "Python is not recognized"
Solution: Reinstall Python and check "Add Python to PATH" during installation

Problem: "pip is not recognized"
Solution: Reinstall Python or manually add Python to system PATH

Problem: "Could not connect to existing Chrome session"
Solution: 
- Make sure Chrome was started with the debugging command
- Keep the first Command Prompt window (with Chrome debugging) open
- Make sure Chrome is still running

Problem: Bot crashes on first record
Solution: 
- Check if you're on the correct page (Khata/Plot/Area entry form)
- Ensure Excel file is named exactly "data.xlsx"
- Verify Excel has correct column headers

Problem: Some records show alerts
Solution: 
- Check your Excel data for invalid characters
- Bot automatically handles alerts and continues
- Invalid records will be skipped

IMPORTANT SAFETY TIPS

1. Backup Your Data: Keep a backup copy of your Excel file
2. Test First: Try with 2-3 records first before running all data
3. Stay Present: Monitor the bot while it runs
4. Keep Chrome Open: Don't close Chrome between runs to avoid re-login
5. Two Command Prompts: Keep both Command Prompt windows open during operation
6. Internet Connection: Ensure stable internet during operation

FILE STRUCTURE
Your folder should look like this:
IGR Bot - EC/
├── igro_bot.py          (the bot code)
├── data.xlsx            (your Excel file with data)
└── README.txt           (this instruction file)

DAILY WORKFLOW (After Initial Setup)

Morning Setup:
1. Start Chrome with debugging: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\ChromeData"
2. Login to IGR website once
3. Navigate to data entry page

Processing Files:
1. Update data.xlsx with your data
2. Run: python igro_bot.py → Choose option 2
3. Let bot process all records
4. Repeat for more files (no re-login needed!)

End of Day:
- Close both Command Prompt windows
- Close Chrome

SUCCESS INDICATORS
✓ Chrome opens in debugging mode
✓ You can login to IGR website manually
✓ Bot connects to existing Chrome session
✓ Bot shows "Processing record X" messages
✓ Website shows your data being added
✓ Final message: "All records processed successfully!"

---
Created for IGR Odisha Website Data Entry Automation
Last Updated: 29/08/2025

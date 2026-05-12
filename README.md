# Flutter Web App Automation - Selenium Test

This project automates the testing of a Flutter web application using Selenium WebDriver. It performs login, OTP verification, and Excel file upload operations.

## 📋 Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [Screenshots](#screenshots)

## ✨ Features

- ✅ **Automated Login**: Enters username and password using keyboard navigation
- ✅ **OTP Verification**: Automatically enters 6-digit OTP code
- ✅ **Excel File Upload**: Uploads Excel file with fallback methods
- ✅ **Screenshot Capture**: Takes screenshots at each step for debugging
- ✅ **Error Handling**: Comprehensive error handling with detailed logging
- ✅ **Flutter Web Support**: Handles Flutter web app's canvas-based UI

## 🔧 Prerequisites

Before running this project, ensure you have the following installed:

1. **Python 3.7 or higher**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Google Chrome Browser**
   - Download from: https://www.google.com/chrome/

3. **ChromeDriver** (automatically managed by Selenium 4.6+)
   - If using older Selenium versions, download manually from: https://chromedriver.chromium.org/

## 📦 Installation

### Step 1: Clone or Download the Project

```cmd
cd C:\Users\SAIDEEP D. GAUNKER\Desktop\watermellon2
```

### Step 2: Install Required Dependencies

Open Command Prompt (CMD) or PowerShell and run:

```cmd
pip install selenium
pip install pyautogui
```

**Alternative: Install all dependencies at once**

Create a `requirements.txt` file (already included in this project) and run:

```cmd
pip install -r requirements.txt
```

### Step 3: Verify Installation

Check if packages are installed correctly:

```cmd
pip list
```

You should see:
- `selenium` (version 4.0+)
- `pyautogui` (version 0.9+)

## 📁 Project Structure

```
watermellon2/
│
├── selenium_test.py              # Main automation script
├── requirements.txt              # Python dependencies
├── README.md                     # This file
│
├── test data/
│   └── excel for flutter testing.xlsx  # Test Excel file to upload
│
└── HTML Files (For reference):
    ├── page_source.html          # Login page source
    └── upload_page_source.html   # Upload page source
```

## 🚀 Usage

### Running the Test

1. **Open Command Prompt** in the project directory:
   ```cmd
   cd C:\Users\SAIDEEP D. GAUNKER\Desktop\watermellon2
   ```

2. **Run the script**:
   ```cmd
   python selenium_test.py
   ```

3. **Watch the automation**:
   - Chrome browser will open automatically
   - The script will perform all actions
   - Screenshots will be saved at each step
   - Browser will close after 10 seconds

### Expected Output

```
Step 1: Opening login page...
Logging in...
✓ Login submitted

Step 2: Entering OTP...
Navigating to first OTP box...
Entering digit 1: 1
Entering digit 2: 2
Entering digit 3: 3
Entering digit 4: 5
Entering digit 5: 6
Entering digit 6: 6
✓ OTP verified

Step 3: Uploading Excel file...
File path: C:\Users\SAIDEEP D. GAUNKER\Desktop\watermellon2\test data\excel for flutter testing.xlsx
✓ File exists
Looking for file input element...
✓ Found 1 file input(s)
✓ File path sent to input element

Step 4: Verifying data...
✓ Data displayed successfully!

✓ Test completed! Browser will close in 10 seconds...
Browser closed.
```

## 🔍 How It Works

### Step 1: Login
1. Opens the Flutter web app URL
2. Clicks on the page body to activate focus
3. Uses TAB navigation to move between fields:
   - Enters username: `flutteruser`
   - TABs to password field
   - Enters password: `password`
   - TABs to Login button and presses ENTER

### Step 2: OTP Verification
1. Waits for OTP page to load
2. TABs to the first OTP input box
3. Enters 6-digit OTP: `123456`
4. Flutter auto-advances to next box after each digit
5. TABs to Verify button and presses ENTER

### Step 3: Excel File Upload
1. **Primary Method**: Finds hidden `<input type="file">` element and sends file path directly
2. **Fallback Method** (if primary fails):
   - Clicks body to reset focus
   - Presses TAB twice:
     - TAB 1: Logout button (skipped)
     - TAB 2: Upload Excel button
   - Presses ENTER to open file picker
   - Uses PyAutoGUI to type file path
   - Presses ENTER to confirm upload

### Step 4: Data Verification
- Checks if uploaded data appears in page source
- Looks for sample data like "ABC1234" or "Jack John"

## 🛠️ Troubleshooting

### Issue 1: "selenium module not found"
**Solution:**
```cmd
pip install selenium
```

### Issue 2: "pyautogui module not found"
**Solution:**
```cmd
pip install pyautogui
```

### Issue 3: ChromeDriver version mismatch
**Solution:**
- Update Selenium to version 4.6+:
  ```cmd
  pip install --upgrade selenium
  ```
- Or download matching ChromeDriver manually

### Issue 4: File upload not working
**Solution:**
- Ensure the Excel file exists in `test data/` folder
- Check file path is correct
- Try running as Administrator

### Issue 5: Script clicks Logout instead of Upload
**Solution:**
- The script already handles this by pressing TAB twice
- If still failing, adjust the TAB count in line 137:
  ```python
  for i in range(3):  # Change 2 to 3 if needed
  ```

### Issue 6: PyAutoGUI not typing file path
**Solution:**
- Ensure file picker dialog is in focus
- Increase wait time before typing:
  ```python
  time.sleep(3)  # Increase from 2 to 3 seconds
  ```

## 📸 Screenshots

The script automatically captures screenshots at each step:

| Screenshot | Description |
|------------|-------------|
| `step1_after_login.png` | After submitting login credentials |
| `step2_otp_page.png` | OTP entry page |
| `step2_otp_entered.png` | After entering OTP digits |
| `step3_after_otp.png` | After OTP verification |
| `step3_upload_page.png` | Upload page before file selection |
| `step4_after_upload.png` | After successful file upload |
| `error.png` | Error screenshot (if test fails) |

## 🔐 Configuration

### Changing Credentials

Edit the following lines in `selenium_test.py`:

```python
# Line 28: Username
actions.send_keys("flutteruser").perform()

# Line 35: Password
actions.send_keys("password").perform()

# Line 58: OTP
otp = "123456"
```

### Changing Test File

Edit line 99 to use a different Excel file:

```python
file_path = os.path.abspath("test data\\your_file.xlsx")
```

### Changing URL

Edit line 18 to test a different environment:

```python
driver.get("https://your-app-url.com")
```

## 📝 Notes

- This script is designed for **Flutter web applications** that use canvas-based rendering
- The script uses **keyboard navigation (TAB + ENTER)** instead of element locators because Flutter renders UI on canvas
- **PyAutoGUI** is used as a fallback for file upload dialogs
- All wait times are optimized for stable execution; adjust if needed for slower connections

## 🤝 Contributing

Feel free to submit issues or pull requests to improve this automation script.

## 📄 License

This project is for testing purposes only.

## 👤 Author

**Saideep D. Gaunker**

---

**Last Updated:** May 11, 2026

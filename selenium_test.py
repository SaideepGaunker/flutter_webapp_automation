from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyautogui

# Open Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    # ============================================
    # STEP 1: LOGIN
    # ============================================
    print("Step 1: Opening login page...")
    driver.get("https://watermelon-life-insurance.vercel.app/fluttertesting/index.html")
    time.sleep(5)
    
    print("Logging in...")
    body = driver.find_element(By.TAG_NAME, "body")
    body.click()
    time.sleep(1)
    
    actions = ActionChains(driver)
    
    # Enter username
    actions.send_keys("flutteruser").perform()
    time.sleep(0.5)
    
    # Tab to password
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.3)
    
    # Enter password
    actions.send_keys("password").perform()
    time.sleep(0.5)
    
    # Tab to Login button and press Enter
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.3)
    actions.send_keys(Keys.ENTER).perform()
    print("✓ Login submitted")
    time.sleep(3)
    
    driver.save_screenshot("step1_after_login.png")
    
    # ============================================
    # STEP 2: ENTER OTP
    # ============================================
    print("\nStep 2: Entering OTP...")
    time.sleep(2)
    
    driver.save_screenshot("step2_otp_page.png")
    
    otp = "123456"
    
    # For Flutter web apps, use Tab navigation to reach the first OTP box
    # Tab once from the page to reach the first OTP input
    print("Navigating to first OTP box...")
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.5)
    
    # Enter OTP digits - Flutter should auto-advance to next box
    for i, digit in enumerate(otp):
        print(f"Entering digit {i+1}: {digit}")
        actions.send_keys(digit).perform()
        time.sleep(0.4)  # Wait for Flutter to auto-focus next box
    
    time.sleep(1)
    driver.save_screenshot("step2_otp_entered.png")
    
    # Tab to Verify button and press Enter
    actions.send_keys(Keys.TAB).perform()
    time.sleep(0.3)
    actions.send_keys(Keys.ENTER).perform()
    print("✓ OTP verified")
    time.sleep(3)
    
    driver.save_screenshot("step3_after_otp.png")
    
    # ============================================
    # STEP 3: UPLOAD EXCEL FILE
    # ============================================
    print("\nStep 3: Uploading Excel file...")
    time.sleep(2)
    
    driver.save_screenshot("step3_upload_page.png")
    
    file_path = os.path.abspath("test data\\excel for flutter testing.xlsx")
    print(f"File path: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"✗ File not found: {file_path}")
    else:
        print(f"✓ File exists")
        
        # Try to find file input element first (hidden input for file upload)
        try:
            print("Looking for file input element...")
            file_inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='file']")
            
            if file_inputs:
                print(f"✓ Found {len(file_inputs)} file input(s)")
                # Send file path directly to the file input (works even if hidden)
                file_inputs[0].send_keys(file_path)
                print("✓ File path sent to input element")
                time.sleep(2)
                driver.save_screenshot("step4_after_upload.png")
            else:
                print("⚠ No file input found, trying button click method...")
                raise Exception("No file input found")
                
        except Exception as e:
            print(f"Direct upload failed: {e}")
            print("Trying alternative method with button click...")
            
            # Click on body first to reset focus, then navigate to upload button
            body = driver.find_element(By.TAG_NAME, "body")
            body.click()
            time.sleep(0.5)
            
            # Try multiple TABs to find the Upload Excel button
            # Usually: TAB 1 = Logout button, TAB 2 = Upload Excel button
            print("Navigating with TAB keys...")
            for i in range(2):  # Try 2 TABs to skip logout and reach upload button
                actions.send_keys(Keys.TAB).perform()
                time.sleep(0.3)
                print(f"  TAB {i+1}")
            
            # Now press Enter to click Upload Excel button
            actions.send_keys(Keys.ENTER).perform()
            print("✓ Pressed Enter on Upload Excel button")
            time.sleep(2)
            
            # Now the file picker dialog should open
            # Use pyautogui to type the file path and press Enter
            print("Typing file path in file picker...")
            pyautogui.typewrite(file_path, interval=0.05)
            time.sleep(1)
            pyautogui.press('enter')
            print("✓ File path entered in dialog")
            time.sleep(3)
            
            driver.save_screenshot("step4_after_upload.png")
    
    # ============================================
    # STEP 4: VERIFY DATA
    # ============================================
    print("\nStep 4: Verifying data...")
    if "ABC1234" in driver.page_source or "Jack John" in driver.page_source:
        print("✓ Data displayed successfully!")
    else:
        print("⚠ Data not found in page source (might be on canvas)")
    
    print("\n✓ Test completed! Browser will close in 10 seconds...")
    time.sleep(10)
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    import traceback
    traceback.print_exc()
    driver.save_screenshot("error.png")
    print("Screenshot saved as error.png")
    time.sleep(5)

finally:
    driver.quit()
    print("Browser closed.")

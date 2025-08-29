import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager

def clean_khata_plot_data(value):
    """Clean Khata/Plot data to keep only numbers, slash (/) and dash (-)"""
    if pd.isna(value) or str(value).strip() == "" or str(value).lower() == "nan":
        return ""
    # Keep only numbers, slash and dash as allowed by the website
    cleaned = re.sub(r'[^0-9/\-]', '', str(value).strip())
    return cleaned

def clean_area_data(value):
    """Clean Area data to keep only numbers and dot (.) for decimal values"""
    if pd.isna(value) or str(value).strip() == "" or str(value).lower() == "nan":
        return ""
    # Keep only numbers and dot for area (decimal values allowed)
    cleaned = re.sub(r'[^0-9.]', '', str(value).strip())
    return cleaned

def handle_alert(driver):
    """Handle unexpected alert popups"""
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"Alert detected: {alert_text}")
        alert.accept()  # Click OK on the alert
        return True
    except:
        return False

# Load Excel file (change filename to data.xlsx or your file name)
# Read all columns as string to prevent automatic number formatting
data = pd.read_excel("data.xlsx", dtype=str)

# Start Chrome (only if not already running)
print("=== IGRO Bot - Data Entry Automation ===")
print("Options:")
print("1. Start new browser session")
print("2. Use existing browser (if already logged in)")
choice = input("Enter your choice (1 or 2): ").strip()

if choice == "1":
    # Start new Chrome session
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # keeps browser open
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    
    # Open IGROdisha site
    driver.get("https://www.igrodisha.gov.in/")
    print(">>> Please login manually and navigate to the data entry page.")
    input(">>> Press ENTER when you're ready to start data entry...")
    
elif choice == "2":
    # Connect to existing Chrome session
    print(">>> Make sure you're already logged in and on the data entry page.")
    print(">>> The bot will connect to your existing Chrome session.")
    
    # Connect to existing Chrome (requires chrome to be started with debugging port)
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "localhost:9222")
    
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("✓ Connected to existing Chrome session")
    except:
        print("❌ Could not connect to existing Chrome session.")
        print("Please close Chrome and restart this script with option 1.")
        exit()
        
    input(">>> Press ENTER when you're ready to start data entry...")
else:
    print("Invalid choice. Exiting.")
    exit()

# Prepare wait
wait = WebDriverWait(driver, 30)

# Store last valid values for carry-forward
last_khata = ""
last_plot = ""
last_area = ""

# Loop through all records in Excel
for index, row in data.iterrows():
    try:
        # Handle Khata (carry forward if blank after cleaning)
        khata_raw = row.get("Khata", "") if "Khata" in data.columns else row.iloc[0]
        khata_cleaned = clean_khata_plot_data(khata_raw)
        
        if khata_cleaned:
            khata = khata_cleaned
            last_khata = khata
        else:
            khata = last_khata
        
        # Handle Plot (carry forward if blank after cleaning)
        plot_raw = row.get("Plot", "") if "Plot" in data.columns else row.iloc[1]
        plot_cleaned = clean_khata_plot_data(plot_raw)
        
        if plot_cleaned:
            plot = plot_cleaned
            last_plot = plot
        else:
            plot = last_plot
        
        # Handle Area (carry forward if blank after cleaning)
        area_raw = row.get("Area", "") if "Area" in data.columns else row.iloc[2]
        area_cleaned = clean_area_data(area_raw)
        
        if area_cleaned:
            area = area_cleaned
            last_area = area
        else:
            area = last_area
        
        print(f"Processing record {index+1}: Khata={khata}, Plot={plot}, Area={area}")
        
        # Fill Khata
        khata_field = driver.find_element(By.ID, "ContentPlaceHolder1_txtKhataNo")
        khata_field.clear()
        khata_field.send_keys(khata)
        
        # Check for alert after entering Khata
        if handle_alert(driver):
            print(f"Alert after Khata entry - skipping record {index+1}")
            continue
        
        # Fill Plot
        plot_field = driver.find_element(By.ID, "ContentPlaceHolder1_txtPlotNo")
        plot_field.clear()
        plot_field.send_keys(plot)
        
        # Check for alert after entering Plot
        if handle_alert(driver):
            print(f"Alert after Plot entry - skipping record {index+1}")
            continue
        
        # Fill Area
        area_field = driver.find_element(By.ID, "ContentPlaceHolder1_Txt_area")
        area_field.clear()
        area_field.send_keys(area)
        
        # Check for alert after entering Area
        if handle_alert(driver):
            print(f"Alert after Area entry - skipping record {index+1}")
            continue
        
        # Wait until loader disappears before clicking Add
        wait.until(EC.invisibility_of_element_located((By.ID, "loader")))
        
        # Click Add button
        add_button = wait.until(EC.element_to_be_clickable((By.ID, "btnAdd")))
        add_button.click()
        
        # Check for alert after clicking Add button
        if handle_alert(driver):
            print(f"Alert after Add button click - record {index+1} may not be added properly")
        
        # ✅ Force a small delay after clicking
        time.sleep(2)
        
        # Wait again until loader disappears after click
        wait.until(EC.invisibility_of_element_located((By.ID, "loader")))
        
        print(f"✓ Successfully added record {index+1}: Khata={khata}, Plot={plot}, Area={area}")
        
    except UnexpectedAlertPresentException as e:
        print(f"Unexpected alert for record {index+1}: {e}")
        handle_alert(driver)
        continue
    except Exception as e:
        print(f"Error processing record {index+1}: {e}")
        handle_alert(driver)  # Try to handle any alert that might be present
        continue

print(">>> All records processed successfully!")
print(">>> You can now:")
print("    1. Update data.xlsx with new data")
print("    2. Run this script again (choose option 2)")
print("    3. Stay logged in - no need to login again!")
print(">>> Browser will stay open for your next session.")
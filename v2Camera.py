#THIS CODE RETRIEVES THE JSON DATA FROM THE M5STACK UNIT V2 WEBSITE
from requests_html import HTMLSession
import json
import time

# Function to process the data
def fetch_and_process_data():
    # Initialize the session
    session = HTMLSession()

    # Send GET request to the URL
    try:
        r = session.get('http://10.254.239.1')

        # Check if the request was successful
        if r.status_code == 200:
            print("Request successful!")
        else:
            print(f"Request failed with status code: {r.status_code}")
            return

        # Render the page using Playwright
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto('http://10.254.239.1')
            page.wait_for_timeout(500)  # Wait for 0.5 second to ensure the page loads

            # Extract rendered content
            html_content = page.content()
            browser.close()

        # Parse the rendered HTML with requests-html
        r.html.raw_html = html_content.encode('utf-8')

        # Extract and process data
        data = r.html.find('#func-result-pre')  #json data is located in webpage pre id="func-result-pre" tag
        for item in data:
            data_text = item.text
            # Parse JSON from the extracted text
            data_dict = json.loads(data_text)
            obj = data_dict.get('obj', [])
            for detail in obj:
                obj_type = detail.get('type', 'Unknown')  # Safely access 'type'
                prob = detail.get('prob', 'Unknown')  # Safely access 'prob'
                xCood = detail.get('x', 'Unknown')  # Safely access 'x'
                yCood = detail.get('y','Unknown')     #Safely access 'y'
                height = detail.get('h','Unknown')    #Safely access 'h'
                width = detail.get('w','Unknown')     #Safely access 'w'

                # Print the object type, probability, xcoord, yccoord, height, width
                print(f"Object Type: {obj_type}")
                print(f"Probability: {prob* 100}%")
                print(f"X Coordinates: {xCood}")
                print(f"Y Coordinates: {yCood}")
                print(f"height: {height}")
                print(f"width: {width}")


    except Exception as e:
        print(f"Error rendering or processing the page: {e}")

# Continuous execution loop
while True:
    fetch_and_process_data()
    print("Waiting for the next iteration...")
    time.sleep(5)  # Wait 5 seconds before the next iteration






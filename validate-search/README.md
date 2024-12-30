# Selenium Table Search Demo Test

This project contains a Python script that automates searching for "New York" in the [Selenium Playground Table Search Demo](https://www.lambdatest.com/selenium-playground/table-sort-search-demo), validating that the search results show exactly **5 entries** out of **24 total entries**.

## Requirements

- Python 3.x
- Google Chrome (or another supported browser)
- ChromeDriver (managed automatically via `webdriver-manager`)

## Setup

1. **Create a Virtual Environment (optional)**

   ```bash
   python -m venv venv
2. **Activate the virtual environment**
    ```
    .\venv\Scripts\activate
    ```
    
3.  **Install Dependencies**
    ```
    pip install -r requirements.txt

or manually install dependencies using
    ```pip install pytest selenium webdriver-manager```.
    
## Running the test
1. **Command line:**
Run the test with the help of ```pytest``` command. Open terminal and run the test with the command:
    ```
    pytest qa_selenium_test.py
2. **Manual test:**
Run the test manually using the test button located aside of the function `test_table_search` and view the result.

3. **Running the Test from `main.py`**: 
Alternatively, we can trigger the test directly from the `main.py` script. This method will run the `test_table_search()` function programmatically.

   - Ensure your environment is set up as mentioned in the previous steps.
   - Run the `main.py` script: ```python main.py```



## Code review
`setup_driver()`: Sets up Chrome WebDriver with `webdriver-manager`.

`test_table_search()`:  Searches for "New York" in the table and validates that the correct number of results (5) and total entries (24) are displayed.

## Browser Compatibility
Tested with **Google Chrome**. You can modify the WebDriver setup for other browsers.

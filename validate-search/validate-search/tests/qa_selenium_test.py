import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def setup_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    # options.add_argument("--headless") --if we need to run automation without UI
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://www.lambdatest.com/selenium-playground/table-sort-search-demo")
    driver.maximize_window()
    return driver

@pytest.fixture(scope="module")
def driver():
    driver = setup_driver()
    yield driver
    driver.quit()

@pytest.mark.parametrize("city, expected_count, total_entries", [("New York", 5, 24)])
def test_table_search(driver, city, expected_count, total_entries):
    box = driver.find_element(By.XPATH, "//input[@type='search']")
    for i in city:
        box.send_keys(i)
        time.sleep(0.5)
    time.sleep(2)

    results = driver.find_elements(By.XPATH, "//table[@id='example']//tbody/tr")

    rows = [row for row in results if city in row.text]
    count = len(rows)

    total = driver.find_element(By.XPATH, "//div[@id='example_info']").text
    box.clear()

    assert count == expected_count, f"Expected {expected_count} rows, but found {count} rows"
    assert str(total_entries) in total, f"Expected {total_entries} entries, but found {total} entries"
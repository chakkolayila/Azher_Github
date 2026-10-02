from playwright.sync_api import sync_playwright
from datetime import datetime

with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    # Navigate to Cricbuzz
    page.goto(
        "https://www.cricbuzz.com/cricket-match/live-scores",
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Wait a few seconds for scores to load
    page.wait_for_timeout(5000)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Save screenshot
    screenshot_file = f"cricbuzz_live_{timestamp}.png"

    page.screenshot(
        path=screenshot_file,
        full_page=True
    )

    print(f"Screenshot saved: {screenshot_file}")

    browser.close()
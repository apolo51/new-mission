import time
from playwright.sync_api import sync_playwright

def run(playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://bit.ly/3XS1Og6")
    time.sleep(3)
    page.locator('//*[@id="navbarSupportedContent"]/a').click()
    time.sleep(3)
    page.get_by_placeholder("Your Tron wallet address").fill("THidzB4aPpFo2h6mfNvsVXWDG8zLp1iqCk")
    time.sleep(3)
    page.locator('//*[@id="startBtn"]').click()
    time.sleep(10)
    page.locator("#sidenav-collapse-main > a.btn.btn-warning.btn-block").click()
    time.sleep(5)
    page.locator("#withdrawalModal > div > div > div.modal-body > div.row.text-sm > div.col-6.text-right > a").click()
    time.sleep(3)
    page.get_by_role("button", name=" Confirm Request").click()
    time.sleep(3)
    page.screenshot(path="screenshot.png")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
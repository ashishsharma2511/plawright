from playwright.sync_api import sync_playwright

def test_example():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://en.wikipedia.org/wiki/Main_Page")
        assert page.title() == "Wikipedia, the free encyclopedia"
        browser.close()

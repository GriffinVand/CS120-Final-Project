from playwright.sync_api import sync_playwright


def scrape_twitter(username, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo= 500)
        context = browser.new_context()
        page = context.new_page()
        
        page.goto("https://twitter.com/login")

        page.fill("//input[@autocomplete='username']", username)
        page.locator("//span[contains(text(), 'Next')]").click()

        page.fill("//input[@autocomplete='current-password']", password)
        page.locator("//span[contains(text(), 'Log in')]").click()

        page.wait_for_selector("[aria-label=\"Post\"]")
        print("SEE POST")

        tweets = page.get_by_test_id('tweet')
        first_tweet = tweets.nth(0)
        first_tweet.click()


        page.wait_for_timeout(10000)
        browser.close()

scrape_twitter('gooberlou1234', 'gooberloupassword')
from playwright.sync_api import sync_playwright

def scrape_facebook(username, password, target_url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.facebook.com/login")

        page.fill("#email", username)
        page.fill("#pass", password)
        page.click("button[name='login']")

        page.wait_for_selector("[aria-label='Search Facebook']")

        page.goto(target_url)

        page.wait_for_selector("[data-pagelet^='FeedUnit']")

        posts = page.locator("[data-pagelet^='FeedUnit']")
        posts_text = []
        for i in range(posts.count()):
            post = posts.nth(i).text_content()
            posts_text.append(post)

        browser.close()

        return posts_text

if __name__ == "__main__":
    username = "tbd"
    password = "tbd"
    target_url = "https://www.facebook.com/groups/specificgroup"  

    posts = scrape_facebook(username, password, target_url)

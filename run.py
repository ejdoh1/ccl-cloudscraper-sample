import cloudscraper as cs
t = cs.create_scraper().get("https://www.cclonline.com").text
open('ccl-home-page.html','w').write(t)

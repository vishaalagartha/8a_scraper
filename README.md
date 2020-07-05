# 8a_scraper

[8a](https://www.8a.nu/) is a great resource to aggregate statistics on sportclimbers and boulderers. They recently deployed a new version of their website that rendered all the prior scrapers obsolete.

This tool allows 8a users to scrape content from the website using their username, password, Selenium, and BeautifulSoup.

### USAGE

This package requires the user to also install Google Chrome and [ChromeDriver](https://chromedriver.chromium.org/downloads). Please ensure that both of the executables are in your `$PATH` variable.

The user must also have an email and password that can be used to log into [8a](https://www.8a.nu/)

Additionally, the user must set the following environment variables:

```
_8A_USERNAME='<8a email>'
_8A_PASSWORD='<8a password>'
```

These variables are accessed using `os.getenv()`.

### API
Currently, the package only contains 2 modules: users and ascents.

The package will be expanding to include other content as well, but this is a start.

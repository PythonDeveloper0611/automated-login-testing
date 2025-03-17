# Configuration settings for the automated login tests

# List of websites to test
WEBSITES = [
    {
        "name": "ExampleSite1",
        "url": "https://www.examplesite1.com/login",
        "username": "your-username1",
        "password": "your-password1",
    },
    {
        "name": "ExampleSite2",
        "url": "https://www.examplesite2.com/login",
        "username": "your-username2",
        "password": "your-password2",
    },
    # Add more websites as needed
]

# Browser settings
BROWSER = "chrome"  # Options: 'chrome', 'firefox'
HEADLESS = True  # Set to False if you want to see the browser
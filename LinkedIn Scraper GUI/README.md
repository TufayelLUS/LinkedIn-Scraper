# LinkedIn Lead Scraper GUI
This is a GUI version of the existing LinkedIn scraper that will collect company-wise leads under any company such as <a href="https://www.linkedin.com/company/unilever/">https://www.linkedin.com/company/unilever/</a><br>
This version no longer requires your login information, on the other hand, it will use your logged-in browser cookies instead. Keep reading, you'll get to know how to collect them from your account.

# Screenshot
<img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-Scraper/refs/heads/master/LinkedIn%20Scraper%20GUI/UI.png" />

# Features
* Supports storing cookie information in a file so you don't have to save it multiple times.
* Customizable Request delay system.
* Leads saved in the same folder as the software executable.
* Download and use, no installation required.

# Prerequisites
1. An account on LinkedIn is a must! You can create temporary profiles if you want.
* For more detailed instructions, please check the main readme file <a href="https://github.com/TufayelLUS/LinkedIn-Scraper/blob/master/README.md">here</a>.

# Disclaimer
Automating LinkedIn goes against their terms of service guidelines. As this repository is in demand, I thought of publishing a revised version according to the 2024 version of the website. Any issues with your LinkedIn account after using this script will be your liability.

# Limits
* Do not run it from an IP address from where you don't usually login to your LinkedIn account, otherwise, it may trigger their security system.
* Result is limited to 1,000 records only

# How to collect cookies?
1. Login to LinkedIn from your Chrome browser(or your favorite one) and navigate to <a href="https://www.linkedin.com/company/unilever/">https://www.linkedin.com/company/unilever/</a>
2. Right-click anywhere on that page and select "Inspect".
3. Go to the "networks" tab and in the "Filter" input box, type "graphql" and refresh the web page again while keeping the networks tab open.
4. You will see some matches shown below. Click on that, locate the "Headers" tab, copy the value from the cookies Response header, and paste it into the cookies placeholder of the script.
<img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-Scraper/master/LinkedIn%20Lead%20Scraper%202024%20Edition/help.png" />

# Usage
Open the software as it's a GUI software and you can use it since everything is self explanatory.

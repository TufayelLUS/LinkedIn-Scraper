# LinkedIn Lead Scraper 2024 Edition
This is an updated version of the existing LinkedIn scraper that will collect company-wise leads under any company such as <a href="https://www.linkedin.com/company/unilever/">https://www.linkedin.com/company/unilever/</a><br>
This version no longer requires your login information, on the other hand, it will use your logged-in browser cookies instead. Keep reading, you'll get to know how to collect them from your account.

# Prerequisites
1. Python 3.x only (Download from <a href="https://python.org/downloads">here</a>) and <b>make sure to tick on "Add to PATH" during installation in Windows machines</b>
2. Installation of below module using command line
<pre>pip3 install requests</pre>
3. An account on LinkedIn is a must! You can create temporary profiles if you want.

# Disclaimer
Automating LinkedIn goes against their terms of service guidelines. As this repository is in demand, I thought of publishing a revised version according to the 2024 version of the website. Any issues with your LinkedIn account after using this script will be your liability. 

# Limits
* Do not run it from an IP address from where you don't usually login to your LinkedIn account, otherwise, it may trigger their security system.
* Result is limited to 10,000 records only

# How to collect cookies?
1. Login to LinkedIn from your Chrome browser(or your favorite one) and navigate to <a href="https://www.linkedin.com/company/unilever/">https://www.linkedin.com/company/unilever/</a>
2. Right-click anywhere on that page and select "Inspect".
3. Go to the "networks" tab and in the "Filter" input box, type "graphql" and refresh the web page again while keeping the networks tab open.
4. You will see some matches shown below. Click on that, locate the "Headers" tab, copy the value from the cookies Response header, and paste it into the cookies placeholder of the script. 

# Usage
Once you have installed and set the prerequisites, open the code(.py file) with a text editor(must not be any rich text editor) and you will see the <i>company_link</i> placeholder to set the company link and cookie data(inside the double quote) and save the code<br>
Now you can double click the <b>LinkedIn_Leads.py</b> to execute and for Linux or mac users, in the terminal, cd to the script folder and type<br>
<pre>Python3 LinkedIn_Leads.py</pre>

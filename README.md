# LinkedIn Lead Scraper 🚀[<a href="https://github.com/TufayelLUS/LinkedIn-Scraper/tree/master/LinkedIn%20Lead%20Scraper%202024%20Edition">2024 Edition is released 🤩!</a>]
A LinkedIn Scraper to scrape up to 10k LinkedIn profiles and save their e-mail addresses if available!<br>
It collects 10k profiles from LinkedIn directory and their details like name, current position/headline and their location information. After all profiles are collected, it starts finding their email addresses
<br><br>
<a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper"><img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-Scraper/master/proxycurl.png" /></a><br>
 <b>Scrape public LinkedIn profile data at scale with <a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper">Proxycurl APIs</a>.</b><br>
 • Scraping Public profiles are battle-tested in court in HiQ VS LinkedIn
 case.<br>
 • GDPR, CCPA, SOC2 compliant<br>
 • High rate Limit- 300 requests/minute<br>
 • Fast APIs respond in ~2s<br>
 • Fresh data- 88% of data is scraped real-time, other 12% are not older than 29 days
 • High accuracy<br>
 • Tons of data points returned per profile<br>
 Built for developers, by developers<br>

# Prerequisites
1. Python 3.x only (Download from <a href="https://python.org/downloads">here</a>) and <b>make sure to tick on "Add to PATH" during installation in windows machines</b>
2. Installation of below module using command line
<pre>pip3 install requests</pre>
3. Account in LinkedIn is a must! You can create temporary profiles if you want.

# Variants Details
<code>Random_Scraper.py</code> is the initial development of the scraper that collects up to 10k random linkedin profiles from directory and picks info from their profile<br>
<code>CompanyWise_Leads.py</code> is the revised version of the code to be able to collect company wise employee profiles for more leads information.

# Limits
* Do not login from IP address from where you don't usually login to your linkedin account, otherwise it will trigger their security system and won't let you login.
* Result is limited to 10,000 records only
* First page data is not collected due to being away from API endpoint capability.

# Usage
Once you have installed and setup the prerequisites, open the code(.py file) with a text editor(must not be any rich text editor) and you will see linkedin_email and linkedin_password variables.<br>Put your linkedin email and password there(inside the double quote) and save the code<br>
Now you can double click the <b>Random_Scraper.py</b> or <b>CompanyWise_Leads.py</b> to execute and for linux or mac users, in the terminal, cd to script folder and type<br>
<pre>python3 Random_Scraper.py</pre>Or,<br>
<pre>python3 CompanyWise_Leads.py</pre>

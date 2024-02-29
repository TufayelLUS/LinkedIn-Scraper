# LinkedIn Lead Scraper 🚀<br><br>Having trouble with the base version? Check the "Cookie Based" version <a href="https://github.com/TufayelLUS/LinkedIn-Scraper/tree/master/LinkedIn%20Lead%20Scraper%202024%20Edition">here</a>
A LinkedIn Scraper to scrape up to 10k LinkedIn profiles and save their e-mail addresses if available!<br>
It collects 10k profiles from the LinkedIn directory and their details like name, current position/headline, and location information. After all profiles are collected, it starts finding their email addresses
<br><br>
<a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper"><img src="https://raw.githubusercontent.com/TufayelLUS/LinkedIn-Scraper/master/proxycurl.png" width="300px" height="100%" /></a><br>
 <b>Scrape public LinkedIn profile data at scale with <a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper">Proxycurl APIs</a>.</b><br>
 • Scraping Public profiles are battle-tested in court in HiQ VS LinkedIn
 case.<br>
 • GDPR, CCPA, SOC2 compliant<br>
 • High rate Limit- 300 requests/minute<br>
 • Fast APIs respond in ~2s<br>
 • Fresh data- 88% of data is scraped real-time, other 12% are not older than 29 days<br>
 • High accuracy<br>
 • Tons of data points returned per profile<br>
 Built for developers, by developers<br>

# Installation Guide
1. First, download Python software from Python's official website. Python 3.x only is supported. Download from <a href="https://python.org/downloads">here</a> or for a precise Python version, <a href="https://www.python.org/downloads/release/python-3118/">download this version</a> and scroll to the bottom to download the correct version based on your operating system and <b>make sure to tick on "Add to PATH" during installation in windows machines</b>
2. Now, from the start menu (Windows) or Applications list (Linux/Mac), search for Command Prompt (Windows) or terminal (on Mac/Linux) and copy-paste the command written below:
<pre>pip3 install requests</pre><br>
This will show some installation progress and will install the library eventually. If you see any pip warning, you may ignore that as that's optional.
* If pip doesn't get recognized as a command, please re-install Python with "Add python to executable path" enabled, or for Mac/Linux, run the command <code>apt-get install python3-pip</code>
3. An account on LinkedIn is a must! You can create temporary profiles if you want.

# Usage Guide 
1. Assuming that the Python software and the library required by this project are installed, time for the script execution. First, download the Python script of your choice and put it inside a folder.
2. Right-click on the Python script and select the option "Edit with IDLE". If you don't see this option, you have to figure that out yourself to fix the problem but a correct installation will show this option in the right-click menu.
3. This option should open up a code window. Locate the <u><i>linkedin_email</i></u> and <u><i>linkedin_password</i></u> placeholders and put your login details (don't worry, it won't get leaked to anyone). After that, set the desired company profile URL inside the <u><i>target_company_link</i></u> placeholder and save the changes by pressing the ctrl+s shortcut.
4. Now, locate the <b>Run</b> menu and select <b>Run Module</b> and the automation will start processing. When you see a <i>>>></i> at the bottom of the output screen, it will mean that the process has finished.

# Other Ways to Run the Script
## Windows
* You can set the configuration of email, password, and company profile link and save the changes. Double-clicking the Python file will also execute it.
## Linux/Mac
* In the terminal, cd to the script folder and type<br>
<pre>python3 Random_Scraper.py</pre>Or,<br>
<pre>python3 CompanyWise_Leads.py</pre>

# Variants Details
<code>Random_Scraper.py</code> is the initial development of the scraper that collects up to 10k random LinkedIn profiles from the directory and picks info from their profile<br>
<code>CompanyWise_Leads.py</code> is the revised version of the code to be able to collect company wise employee profiles for more leads information.<br>
If you're having issues with the login-based version(the base script), you can try either the <a href="https://github.com/TufayelLUS/LinkedIn-Scraper/tree/master/LinkedIn%20Lead%20Scraper%202024%20Edition">cookie version</a> (doesn't have e-mail scraping ability) or the <a href="https://github.com/TufayelLUS/LinkedIn-Scraper/tree/master/ProxyCurl_Version">ProxyCurl API integrated version</a> (Allows searching location, roles and have e-mail scraping capabilities)

# Limits
* Do not log in from the IP address from where you don't usually login to your LinkedIn account, otherwise, it will trigger their security system and won't let you log in.
* Result is limited to 10,000 records only (this is a limitation from LinkedIn's side)
* First-page data is not collected due to being away from API endpoint capability. But the <a href="https://github.com/TufayelLUS/LinkedIn-Scraper/tree/master/LinkedIn%20Lead%20Scraper%202024%20Edition">cookie version</a> will get you covered.
* For searching by location or by role, or if you don't want to use your own LinkedIn account, you have to use the <a href="https://github.com/TufayelLUS/LinkedIn-Scraper/tree/master/ProxyCurl_Version">ProxyCurl version</a> as they offer this ability.

# Disclaimer
Do not flood LinkedIn using your account on a large number to avoid issues with your account. If you want to anonymously scrape LinkedIn Leads for your business, you can check <a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper">Proxycurl APIs</a> to stay on the safe side (they offers trial access too for FREE!). 

# Loved This Open Source Project?
Star the repository and share it with your friends who might need this. More variants of the LinkedIn Scraper will come soon. Keep this on watch for more updates!

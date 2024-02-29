# LinkedIn Lead Scraper Anonymous Version 🚀
A LinkedIn Scraper dedicated to scraping company leads anonymously and saving their e-mail addresses if available!<br>
It collects profiles from the LinkedIn directory and their details like name, current position/headline, and location information. After all profiles are collected, it starts finding their email addresses and it doesn't require any account but <a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper">an API key from ProxyCurl</a> and that's all you need!<br>
You can set the location of the search results that you want or set the role that you're looking to have in the user profiles(ex. co-founder/human resources).
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
1. Get an API key from <a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper">ProxyCurl here</a>. 
2. Download Python software from Python's official website. Python 3.x only is supported. Download from <a href="https://python.org/downloads">here</a> or for a precise Python version, <a href="https://www.python.org/downloads/release/python-3118/">download this version</a> and scroll to the bottom to download the correct version based on your operating system and <b>make sure to tick on "Add to PATH" during installation in windows machines</b>
3. Now, from the start menu (Windows) or Applications list (Linux/Mac), search for Command Prompt (Windows) or terminal (on Mac/Linux) and copy-paste the command written below:
<pre>pip3 install requests</pre><br>
This will show some installation progress and will install the library eventually. If you see any pip warning, you may ignore that as that's optional.
* If pip doesn't get recognized as a command, please re-install Python with "Add python to executable path" enabled, or for Mac/Linux, run the command <code>apt-get install python3-pip</code>

# Usage Guide 
1. Assuming that the Python software and the library required by this project are installed, time for the script execution. First, download the Python script of your choice and put it inside a folder.
2. Right-click on the Python script and select the option "Edit with IDLE". If you don't see this option, you have to figure that out yourself to fix the problem but a correct installation will show this option in the right-click menu.
3. This option should open up a code window. Locate the <u><i>proxy_curl_api_key</i></u> (<a href="https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper">Get an API key from here</a>) placeholder and place the API key. After that, set the desired company profile URL inside the <u><i>company_link</i></u> placeholder and save the changes by pressing the ctrl+s shortcut. You can adjust the search configuration inside the <u><i>search_config</i></u> placeholder by following the <a href="https://nubela.co/proxycurl/docs#company-api-employee-listing-endpoint">instructions given here</a>
4. Now, locate the <b>Run</b> menu and select <b>Run Module</b> and the automation will start processing. When you see a <i>>>></i> at the bottom of the output screen, it will mean that the process has finished.

# Other Ways to Run the Script
## Windows
* You can set the configuration of email, password, and company profile link and save the changes. Double-clicking the Python file will also execute it.
## Linux/Mac
* In the terminal, cd to the script folder and type<br>
<pre>python3 LinkedIn_Scraper.py</pre>

# Loved This Open Source Project?
Star the repository and share it with your friends who might need this. More variants of the LinkedIn Scraper will come soon. Keep this on watch for more updates!

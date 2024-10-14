# Tested on: 10-14-2024
# Author: Tufayel Ahmed
# Github: https://www.github.com/TufayelLUS
# LinkedIn: https://www.linkedin.com/in/tufayel-ahmed-cse/
# Follow me on GitHub for more premium projects!
# This script collects all *COMPANY WISE* profiles listed in LinkedIn
# This version doesn't collect e-mail addresses as of now

import customtkinter as ctk
import threading
import requests
import re
import csv
import os
import json
from time import sleep
from tkinter import scrolledtext, Spinbox, messagebox

# Configuration file path
CONFIG_FILE = "config.json"
stop_requested = False

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# Load configuration
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    else:
        return {}


# Save configuration
def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)


class LinkedInScraper:
    def __init__(self, cookie, company_link, pagination_delay, output_callback, facet_callback, error_callback):
        self.cookie = cookie
        self.company_link = company_link
        self.pagination_delay = pagination_delay
        self.output_callback = output_callback
        self.facet_callback = facet_callback
        self.error_callback = error_callback
        self.session = requests.Session()
        self.output_file_name = "leads.csv"
        self.fieldnames = ["Profile Link", "Name", "Designation", "Location"]

    def saveData(self, dataset):
        try:
            with open(self.output_file_name, mode='a+', encoding='utf-8-sig', newline='') as csvFile:
                writer = csv.DictWriter(
                    csvFile, fieldnames=self.fieldnames, delimiter=',', quotechar='"')
                if os.stat(self.output_file_name).st_size == 0:
                    writer.writeheader()
                writer.writerow({
                    "Profile Link": dataset[0],
                    "Name": dataset[1],
                    "Designation": dataset[2],
                    "Location": dataset[3]
                })
        except Exception as e:
            self.error_callback(f"Error saving data: {e}")

    @classmethod
    def getCompanyID(cls, company_link, error_callback):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Dnt': '1',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/121.0.0.0 Safari/537.36',
        }
        try:
            resp = requests.get(company_link, headers=headers).text
        except Exception as e:
            error_callback(f"Failed to open {company_link}: {e}")
            return None
        try:
            companyID = re.findall(
                r'"objectUrn":"urn:li:organization:([\d]+)"', resp)[0]
            return companyID
        except IndexError:
            error_callback("Company ID not found.")
            return None

    def paginateResults(self, companyID):
        global stop_requested
        headers = {
            'Accept': 'application/vnd.linkedin.normalized+json+2.1',
            'Cookie': self.cookie,
            'Csrf-Token': re.findall(r'JSESSIONID="(.+?)"', self.cookie)[0],
            'Dnt': '1',
            'Referer': f'https://www.linkedin.com/search/results/people/?currentCompany=%5B%22{companyID}%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page=2&sid=7Gd',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                          ' Chrome/121.0.0.0 Safari/537.36',
            'X-Li-Lang': 'en_US',
            'X-Li-Page-Instance': 'urn:li:page:d_flagship3_search_srp_people_load_more;Ux/gXNk8TtujmdQaaFmrPA==',
            'X-Li-Track': '{"clientVersion":"1.13.9792","mpVersion":"1.13.9792","osName":"web","timezoneOffset":6,'
                          '"timezone":"Asia/Dhaka","deviceFormFactor":"DESKTOP","mpName":"voyager-web",'
                          '"displayDensity":1.3125,"displayWidth":1920.1875,"displayHeight":1080.1875}',
            'X-Restli-Protocol-Version': '2.0.0',
        }
        for page_no in range(0, 1000, 10):
            if stop_requested:
                stop_requested = False
                self.facet_callback("Scraping Stopped.")
                return
            self.facet_callback(f"Checking facet: {page_no}/990")
            link = (
                "https://www.linkedin.com/voyager/api/graphql?variables=(start:" + str(page_no) +
                ",origin:COMPANY_PAGE_CANNED_SEARCH,query:(flagshipSearchIntent:SEARCH_SRP,queryParameters:List("
                "(key:currentCompany,value:List(" + companyID + ")),"
                "(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&"
                "queryId=voyagerSearchDashClusters.e1f36c1a2618e5bb527c57bf0c7ebe9f"
            )
            try:
                resp = self.session.get(link, headers=headers).json()
            except Exception as e:
                self.error_callback(f"Failed to open {link}: {e}")
                continue
            results = resp.get('included', [])
            for person_data in results:
                if person_data.get('$type') == "com.linkedin.voyager.dash.search.EntityResultViewModel":
                    person_name = person_data.get(
                        'title', {}).get('text', 'N/A')
                    profile_link = person_data.get('navigationUrl', 'N/A')
                    designation = person_data.get(
                        'primarySubtitle', {}).get('text', 'N/A')
                    person_location = person_data.get(
                        'secondarySubtitle', {}).get('text', 'N/A')
                    profile_info = f"Profile Link: {profile_link}\nName: {
                        person_name}\nDesignation: {designation}\nLocation: {person_location}\n"
                    self.output_callback(profile_info)
                    dataset = [profile_link, person_name,
                               designation, person_location]
                    self.saveData(dataset)
            self.output_callback(
                f"Waiting for {self.pagination_delay} seconds...\n")
            sleep(self.pagination_delay)
        self.facet_callback("Scraping Completed.")

    def start_scraping(self):
        companyID = self.getCompanyID(
            self.company_link, self.error_callback)
        if companyID:
            self.paginateResults(companyID)


class LinkedInScraperGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("LinkedIn Company Profile Scraper")
        self.geometry("800x700")
        self.resizable(False, False)
        # Modes: system (default), light, dark
        ctk.set_appearance_mode("System")
        # Themes: blue (default), dark, green
        ctk.set_default_color_theme("blue")

        # Load config
        self.config_data = load_config()

        # Cookie Input
        self.cookie_label = ctk.CTkLabel(self, text="Enter LinkedIn Cookie:")
        self.cookie_label.pack(pady=(20, 5))

        self.cookie_textbox = ctk.CTkTextbox(self, width=760, height=100)
        self.cookie_textbox.pack(pady=(0, 20))
        self.cookie_textbox.insert("0.0", self.config_data.get("cookie", ""))

        # Pagination Delay Input
        self.delay_label = ctk.CTkLabel(
            self, text="Pagination Delay (seconds):")
        self.delay_label.pack(pady=(0, 5))

        # Create a frame to hold the Spinbox
        self.delay_frame = ctk.CTkFrame(self, width=760, height=40)
        self.delay_frame.pack(pady=(0, 20))

        # Use standard Tkinter Spinbox inside customtkinter frame
        self.delay_spinbox = Spinbox(self.delay_frame, from_=1, to=60, width=5)
        self.delay_spinbox.delete(0, 'end')
        self.delay_spinbox.insert(
            0, self.config_data.get("pagination_delay", 5))
        self.delay_spinbox.pack(pady=5, padx=10, side='left')

        # Company Link Input
        self.company_label = ctk.CTkLabel(
            self, text="Enter Company LinkedIn URL:")
        self.company_label.pack(pady=(0, 5))

        self.company_entry = ctk.CTkEntry(self, width=760)
        self.company_entry.pack(pady=(0, 20))
        self.company_entry.insert(0, self.config_data.get(
            "company_link", "https://www.linkedin.com/company/unilever/"))

        # Start Button
        self.start_button = ctk.CTkButton(
            self, text="Start Scraping", command=self.start_scraping_thread)
        self.start_button.pack(pady=(0, 20))

        # Facet Label
        self.facet_label = ctk.CTkLabel(self, text="Facet: N/A")
        self.facet_label.pack(pady=(0, 10))

        # Output Window with Scrollbar
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.pack(pady=(0, 10), fill="both", expand=True, padx=20)

        self.output_text = scrolledtext.ScrolledText(
            self.output_frame, wrap='word', width=90, height=15, state='disabled')
        self.output_text.config(bg="#2B2B2B", fg="white")
        self.output_text.pack(fill="both", expand=True)

    def update_facet(self, text):
        self.facet_label.configure(text=text)

    def append_output(self, text):
        self.output_text.configure(state='normal')
        self.output_text.insert(ctk.END, text + "\n")
        self.output_text.see(ctk.END)
        self.output_text.configure(state='disabled')

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def start_scraping_thread(self):
        global stop_requested
        if self.start_button.cget('text') == 'Stop Scraping':
            self.start_button.configure(text='Start Scraping')
            stop_requested = True
            return

        # Save cookie and other inputs to config
        cookie = self.cookie_textbox.get("0.0", ctk.END).strip()
        pagination_delay = self.delay_spinbox.get()
        company_link = self.company_entry.get().strip()

        if not cookie:
            messagebox.showwarning(
                "Input Required", "Please enter your LinkedIn cookie.")
            return
        if not company_link:
            messagebox.showwarning(
                "Input Required", "Please enter the company LinkedIn URL.")
            return

        try:
            pagination_delay = int(pagination_delay)
            if not (1 <= pagination_delay <= 60):
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Invalid Input", "Pagination delay must be an integer between 1 and 60.")
            return

        # Save to config
        self.config_data["cookie"] = cookie
        self.config_data["pagination_delay"] = pagination_delay
        self.config_data["company_link"] = company_link
        save_config(self.config_data)

        # Clear output window
        self.output_text.configure(state='normal')
        self.output_text.delete("1.0", ctk.END)
        self.output_text.configure(state='disabled')
        self.facet_label.configure(text="Starting...")

        # Disable start button to prevent multiple threads
        self.start_button.configure(text='Stop Scraping')

        # Initialize scraper
        scraper = LinkedInScraper(
            cookie=cookie,
            company_link=company_link,
            pagination_delay=pagination_delay,
            output_callback=self.append_output,
            facet_callback=self.update_facet,
            error_callback=self.show_error
        )

        # Start scraping in a separate thread
        threading.Thread(target=self.run_scraper,
                         args=(scraper,), daemon=True).start()

    def run_scraper(self, scraper):
        try:
            scraper.start_scraping()
        except Exception as e:
            self.show_error(f"An error occurred: {e}")
        finally:
            # Re-enable start button after completion
            self.start_button.configure(text='Start Scraping')


if __name__ == "__main__":
    app = LinkedInScraperGUI()
    app.mainloop()

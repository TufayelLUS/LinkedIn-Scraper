# Created on: 29-02-2024
# Author: Tufayel Ahmed
# Github: https://www.github.com/TufayelLUS
# LinkedIn: https://www.linkedin.com/in/tufayel-ahmed-cse/
# Follow me on GitHub for more premium projects!
# This script collects all *COMPANY WISE* profiles listed in LinkedIn
# This version doesn't collect e-mail addresses as of now
# Get your API Key from https://nubela.co/proxycurl?utm_campaign=influencer_marketing&utm_source=github&utm_medium=social&utm_content=tufayel_linkedin-scraper
import requests
import csv
import os
from time import sleep


s = requests.Session()
proxy_curl_api_key = ''  # place your API Key here
company_link = "https://www.linkedin.com/company/unilever/"  # target company link
# learn more about search_config options here: https://nubela.co/proxycurl/docs#company-api-employee-listing-endpoint
# If you're not sure, please hire a developer for helping you understand these
# This can help you narrow down profiles under specific country and people with specific role in the company
search_config = {
    'country': 'us',
    'enrich_profiles': 'enrich',
    'role_search': '(co)?-?founder',
    'page_size': '10',
    'employment_status': 'current',
    'sort_by': 'recently-joined',
    'resolve_numeric_id': 'false',
}
output_file_name = "leads.csv"  # output CSV excel file name
pagination_delay = 1  # delay in seconds before going to the next page


class LinkedIn:
    def __init__(self):
        self.fieldnames = ["Profile Link", "Name", "Designation", "Location", "Email"]

    def saveData(self, dataset):
        with open(output_file_name, mode='a+', encoding='utf-8-sig', newline='') as csvFile:

            writer = csv.DictWriter(
                csvFile, fieldnames=self.fieldnames, delimiter=',', quotechar='"')
            if os.stat(output_file_name).st_size == 0:
                writer.writeheader()
            writer.writerow({
                "Profile Link": dataset[0],
                "Name": dataset[1],
                "Designation": dataset[2],
                "Location": dataset[3],
                "Email": dataset[4]
            })

    def scrapeEmail(self, profile_link):
        api_link = "https://nubela.co/proxycurl/api/v2/linkedin"
        headers = {
            'Authorization': 'Bearer {}'.format(proxy_curl_api_key)
        }
        params = {
            'linkedin_profile_url': profile_link,
            'personal_email': 'include'
        }
        try:
            resp = s.get(api_link, headers=headers,
                         params=search_config).json()
        except:
            print("Failed to open {}".format(api_link))
            return None
        return resp.get('personal_email') if resp.get('personal_email') is not None or [] else []

    def paginateResults(self):
        global search_config
        global company_link
        headers = {
            'Authorization': 'Bearer {}'.format(proxy_curl_api_key)
        }
        api_link = "https://nubela.co/proxycurl/api/linkedin/company/employees/"
        if company_link.endswith('/'):
            company_link = company_link[:-1]
        search_config['url'] = company_link
        page_no = 1
        while True:
            print("Checking page: {}".format(page_no))
            try:
                resp = s.get(api_link, headers=headers,
                             params=search_config).json()
            except:
                print("Failed to open {}".format(api_link))
                continue
            results = resp.get('employees')
            if results is None:
                print("No results found! Check the raw API response below:")
                print(resp)
                break
            api_link = resp.get('next_page')
            for person_data in results:
                person_name = person_data.get('profile').get('full_name')
                profile_link = person_data.get('profile_url')
                designation = person_data.get(
                    'profile').get('headline')
                person_location = "{}, {}, {}".format(person_data.get('profile').get(
                    'city'), person_data.get('profile').get('state'), person_data.get('profile').get('country'))
                print("Profile Link: {}".format(profile_link))
                print("Name: {}".format(person_name))
                print("Designation: {}".format(designation))
                print("Location: {}".format(person_location))
                print("Collecting email address from profile ...")
                email = self.scrapeEmail(profile_link)
                if email is not None:
                    email = "; ".join(email)
                else:
                    email = ""
                print("Email: {}".format(email))
                print()
                dataset = [profile_link, person_name,
                           designation, person_location, email]
                self.saveData(dataset)
            if api_link is None:
                print("No more results found!")
                break
            print("Waiting for {} seconds".format(pagination_delay))
            sleep(pagination_delay)


if __name__ == "__main__":
    linkedin = LinkedIn()
    linkedin.paginateResults()

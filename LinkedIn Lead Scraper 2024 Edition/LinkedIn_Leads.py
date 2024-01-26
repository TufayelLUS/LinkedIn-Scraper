# Tested on: 26-01-2024
# Author: Tufayel Ahmed
# Github: https://www.github.com/TufayelLUS
# LinkedIn: https://www.linkedin.com/in/tufayel-ahmed-cse/
# Follow me on GitHub for more premium projects!
# This script collects all *COMPANY WISE* profiles listed in LinkedIn
# This version doesn't collect e-mail addresses as of now
import requests
import re
import csv
import os
from time import sleep


s = requests.Session()
company_link = "https://www.linkedin.com/company/unilever/"  # target company link
output_file_name = "leads.csv"  # output CSV excel file name
pagination_delay = 5  # delay in seconds before going to the next page
cookies = ''  # place cookie here


class LinkedIn:
    def __init__(self):
        self.fieldnames = ["Profile Link", "Name", "Designation", "Location"]

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
                "Location": dataset[3]
            })

    @classmethod
    def getCompanyID(self):
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }
        try:
            resp = requests.get(company_link, headers=headers).text
        except:
            print("Failed to open {}".format(company_link))
            return None
        try:
            companyID = re.findall(
                r'"objectUrn":"urn:li:organization:([\d]+)"', resp)[0]
        except:
            print("Company ID not found")
            return None
        return companyID

    def paginateResults(self, companyID):
        headers = {
            'Accept': 'application/vnd.linkedin.normalized+json+2.1',
            'Cookie': cookies,
            'Csrf-Token': re.findall(r'JSESSIONID="(.+?)"', cookies)[0],
            'Dnt': '1',
            'Referer': 'https://www.linkedin.com/search/results/people/?currentCompany=%5B%22' + companyID + '%22%5D&origin=COMPANY_PAGE_CANNED_SEARCH&page=2&sid=7Gd',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'X-Li-Lang': 'en_US',
            'X-Li-Page-Instance': 'urn:li:page:d_flagship3_search_srp_people_load_more;Ux/gXNk8TtujmdQaaFmrPA==',
            'X-Li-Track': '{"clientVersion":"1.13.9792","mpVersion":"1.13.9792","osName":"web","timezoneOffset":6,"timezone":"Asia/Dhaka","deviceFormFactor":"DESKTOP","mpName":"voyager-web","displayDensity":1.3125,"displayWidth":1920.1875,"displayHeight":1080.1875}',
            'X-Restli-Protocol-Version': '2.0.0',
        }
        for page_no in range(0, 1000, 10):
            print("Checking facet: {}/990".format(page_no))
            link = "https://www.linkedin.com/voyager/api/graphql?variables=(start:" + str(page_no) + ",origin:COMPANY_PAGE_CANNED_SEARCH,query:(flagshipSearchIntent:SEARCH_SRP,queryParameters:List((key:currentCompany,value:List(" + \
                companyID + \
                ")),(key:resultType,value:List(PEOPLE))),includeFiltersInResponse:false))&queryId=voyagerSearchDashClusters.e1f36c1a2618e5bb527c57bf0c7ebe9f"

            try:
                resp = s.get(link, headers=headers).json()
            except:
                print("Failed to open {}".format(link))
                continue
            results = resp.get('included')
            for person_data in results:
                if person_data.get('$type') == "com.linkedin.voyager.dash.search.EntityResultViewModel":
                    person_name = person_data.get('title').get('text')
                    profile_link = person_data.get('navigationUrl')
                    designation = person_data.get(
                        'primarySubtitle').get('text')
                    person_location = person_data.get(
                        'secondarySubtitle').get('text')
                    print("Profile Link: {}".format(profile_link))
                    print("Name: {}".format(person_name))
                    print("Designation: {}".format(designation))
                    print("Location: {}".format(person_location))
                    print()
                    dataset = [profile_link, person_name,
                               designation, person_location]
                    self.saveData(dataset)
            print("Waiting for {} seconds".format(pagination_delay))
            sleep(pagination_delay)


if __name__ == "__main__":
    companyID = LinkedIn.getCompanyID()
    if companyID is not None:
        linkedin = LinkedIn()
        linkedin.paginateResults(companyID)

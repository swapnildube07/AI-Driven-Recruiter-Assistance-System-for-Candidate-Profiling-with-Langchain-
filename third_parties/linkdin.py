import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkdin_profile(linkedin_profile_url: str,mock: bool = False):
    '''scrape  information from linkdin profiles,
      Manually scrape the information from linkedin Profile'''


    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/Swapnil077/2a76edf7cf44b9d86cbe96ca38ec8ec4/raw/f326736e0f7381f5c95969573956e6097c7c5778/Swapnil%2520JSON"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dic,
            timeout=10,
        )

    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
           and k not in ["people_also_viewed", "certifications"]
    }
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data


if __name__ == "__main__":
    print(
        scrape_linkdin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/swapnil077/",mock=True
        )
    )
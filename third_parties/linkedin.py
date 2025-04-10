import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrap_linkedin_profile(linkedin_profile_URL: str, mock: bool = False):
    """
    Scrap the information from the LinkedIn profile URL.
    Manually scraping the information from the LinkedIn profile URL.
    Args:
        Linkedin_profile_URL (str): The LinkedIn profile URL.
        mock (bool): If True, return mock data instead of scraping. Default is False.
    """
    if mock:
        linkedin_profile_URL = "https://gist.githubusercontent.com/GauravThakur189/6ea0b2bc3d3c80e9a83fb996932d2d3a/raw/776d2e74a9c569d40d0e073c174e4d48b169ab35/gauravSinghScrapin.json"
        response = requests.get(
            linkedin_profile_URL,
            timeout=10,
        )
        data = response.json().get("person")
        data = {
            k:v
            for k,v in data.items()
            if v not in ([],"","",None)
            and k not in ["certifications","languages","projects"]
        }
        return data
        
    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.getenv("SCRAPIN_API_KEY"),
            "linkedInUrl": linkedin_profile_URL,
        }
        response = requests.get(
            api_endpoint,
            params=params,
            timeout=10,
        )
        data = response.json().get("person")
        data = {
            k:v
            for k,v in data.items()
            if v not in ([],"","",None)
            and k not in ["certifications","languages","projects"]
        }
        return data

if __name__ == "__main__":
    Linkedin_profile_URL = "https://www.linkedin.com/in/gaurav-singh189/"
    print(scrap_linkedin_profile(Linkedin_profile_URL))

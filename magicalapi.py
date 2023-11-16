import requests
import os

class MagicalAPI:
    def __init__(self, api_key):
        """
        Initialize the MagicalAPI class with an API key.
        Args:
        - api_key (str): The API key for authentication.
        """
        self.api_key = api_key
        self.base_url = "https://gw.magicalapi.com"
    
    def set_api_key(self, api_key):
        """
        Set or update the API key.
        Args:
        - api_key (str): The new API key to be set.
        """
        self.api_key = api_key

    def get_linkedin_profile(self, profile_name):
        """
        Retrieve LinkedIn profile data.
        Args:
        - profile_name (str): The username of the LinkedIn profile to retrieve.
        
        Returns:
        - dict: A dictionary containing the LinkedIn profile data or an error message.
        """
        print(f"API Key: {self.api_key}")
        url = f"{self.base_url}/profile-data/"
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        payload = {"profile_name": profile_name}

        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Response: {response.json()}")
            return {"error": f"Request failed with status code {response.status_code}"}


    def get_company_data(self, company_name):
        """
        Retrieve company data.
        Args:
        - company_name (str): The name of the company to retrieve data for.
        
        Returns:
        - dict: A dictionary containing the company data or an error message.
        """
        url = f"{self.base_url}/company-data/"
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        payload = {"company_name": company_name}

        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Request failed with status code {response.status_code}"}

# get the api key from environmental variables.  MAGICAL_API_KEY
api_key = os.environ.get("MAGICAL_API_KEY")
print(api_key)
api = MagicalAPI(api_key)
linkedin_data = api.get_linkedin_profile("johncoleeng")
print(linkedin_data)

company_data = api.get_company_data("Calculated Leap Ventures")
print(company_data)
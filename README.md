# About
This is an unofficial python API for Magical API.  Learn more about Magical API here.  

Learn more about [the API documentation here.](https://docs.magicalapi.com/)

# Installation
Set the magical api key in the environmental variable. 

```export MAGICAL_API_KEY="YOUR_API_KEY"```

## Virtual Environment
```
python3.10 -m venv myvenv
source ./myvenv/bin/activate
pip install -r requirements.txt
```

# Example Usage

```
api = MagicalAPI("YOUR_API_KEY")
linkedin_data = api.get_linkedin_profile("johncoleeng")
print(linkedin_data)

company_data = api.get_company_data("Calculated Leap Ventures")
print(company_data)
```
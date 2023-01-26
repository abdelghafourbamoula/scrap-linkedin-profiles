from linkedin_api import Linkedin
import json
from tqdm import tqdm
from LOGIN import USERNAME,PASSWORD

# create an instance of the API client
api = Linkedin(USERNAME,PASSWORD)
# search for profiles based on a keyword
search_results = api.search_people(keywords=['data engineer','data scientist', 'big data engineer'], regions='morocco', industries=['data science', 'big data'], limit=150)
print(len(search_results),'Profile Founded !')

target_profiles = list()

for item in tqdm(search_results, desc='Extracting', total=150):

    profile = api.get_profile(item.get('urn_id'))
    profile_dict = {}
    profile_dict['profile_id'] = profile.get('profile_id')
    profile_dict['description'] = profile.get('headline')
    profile_dict['lastName'] = profile.get('lastName')
    profile_dict['firstName'] = profile.get('firstName')
    profile_dict['industry'] = profile.get('industryName')
    profile_dict['student'] = profile.get('student')
    profile_dict['birthDate'] = {'month':profile.get('birthDate')['month'], 'day':profile.get('birthDate')['day']} if profile.get('birthDate') else None
    profile_dict['pictureUrl'] = profile.get('displayPictureUrl')
    profile_dict['location'] = {
        'locationName':profile.get('geoLocationName'),
        'country':profile.get('geoCountryName'),
        'countryCode':profile.get('location').get('basicLocation')['countryCode'].upper()
    }
    profile_dict['skills'] = [skill['name'] for skill in profile.get('skills')]
    profile_dict['education'] = [
        {
            'schoolName': school.get('schoolName'),
            'field': school.get('fieldOfStudy'),
            'degree': school.get('degreeName'),
            'period': school.get('timePeriod')
        }
        for school in profile.get('education')
    ]
    profile_dict['experience'] = [
        {
            'title': experience.get('title'),
            'companyName': experience.get('companyName'),
            'location': experience.get('geoLocationName'),
            'period':experience.get('timePeriod'),
        }
        for experience in profile.get('experience')
    ]

    target_profiles.append(profile_dict)

print(len(target_profiles),"extracted profile ...")

with open('linkedin_profiles.json','w') as json_file:
    json.dump(target_profiles, json_file)

print(json_file," saved ...")

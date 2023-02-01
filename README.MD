### Scrap targeting linkedin profiles using linkedin-api an export them to json format (mongodb collection)

---
requirements for `python 3.9`
`linkedin-api` `tqdm` (`pandas`)

the linked in `USERNAME` and `PASSWORD` saved in a python file `LOGIN.py`

#### the folowed format

```
{
    profile_id,
    headline,
    lastName,
    firstName,
    industryName,
    is student,
    location: {geoCountryName, geoLocationName, location.basicLocation.countryCode},
    birthDate{},
    displayPictureUrl,
    skills: [skills.name],
    education [{
        school: {schoolName, active, trackingId},
        fieldOfStudy,
        degreeName,
        timePeriod: {endDate, startDate}
    }],
    experience[{
        geoLocationName
        companyName
        timePeriod:{startDate{}, endDate{}},
        title,
    }],
}
```

![python](https://img.shields.io/badge/python-grey?&logo=python)
![jupyter](https://img.shields.io/badge/jupyter-grey?&logo=jupyter)
![jupyter](https://img.shields.io/badge/pycharm-grey?&logo=pycharm)
![jupyter](https://img.shields.io/badge/linkedin-api-grey?&logo=linkedin)

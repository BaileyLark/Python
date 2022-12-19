import json

dict = {"key": 12, "hi": 8}

people_string = '''
{
    "people":
    [
        {
            "name": "John Smith", 
            "phone": "665-442-4123",
            "email": ["johnsmith@email1", "johnsmith@email2"],
            "has_license": false
        },
        {
            "name": "Sarah Smith", 
            "phone": "595-343-1284",
            "email": null,
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string) # converts it into object

for person in data['people']:
    print(person['name'])

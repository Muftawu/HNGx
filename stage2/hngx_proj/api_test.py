import requests
from app.utils import disp
from typing import Union

# base_url = "http://127.0.0.1:8000/api"
base_url = "https://hngx-production-6712.up.railway.app/api"

def get_all_persons():
    url = base_url + "/all_persons"
    disp(url)
    return requests.get(url).text

def get_person(query: Union[str, int]):
    url = base_url + f"/get_person/{query}/"
    disp(url)
    return requests.get(url).text

def create_person(username):
    url = base_url + "/create_person/"
    disp(url)
    response = requests.post(url, {"username":username})
    return response.text

def delete_person(query: Union[str, int]):
    url = base_url+f"/delete/{query}"
    disp(url)
    response = requests.delete(url)
    return response.text 

def update_person(old_data: Union[str, int], new_data: Union[str, int]):
    url = base_url + "/update/"
    disp(url)
    response = requests.post(url, {"old_data": old_data, "new_data": new_data})
    return response.text 

if __name__ == "__main__":
    disp(get_all_persons())
    # disp(get_person("liam dunbar"))
    # disp(get_person(8))
    # disp(create_person("Avonor Philip"))
    # disp(create_person("Ernestina Fosu"))
    # disp(create_person("liam dunbar"))
    # disp(delete_person("Theon Grayjoy"))
    # disp(update_person("liam dunbar", "Theon Grayjoy"))


'''
Completed tests using request library
 - ✅ Get all person details 
 - ✅ Get specific person detials 
 - ✅ Create new person 
 - ✅ Delete person 
 - ✅ Update person details  
'''

# everything works well with the python request library
# for postman 
    # - getting all persons works 
    # - getting specific persons
    # - create person
    # - update a person
    # - delete a person
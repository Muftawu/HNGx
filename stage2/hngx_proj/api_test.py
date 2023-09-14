import requests
from app.utils import disp
from typing import Union

# base_url = "http://127.0.0.1:8000/api"
base_url = "https://hngx-production-6712.up.railway.app"

def get_all_persons():
    return requests.get(base_url + "/all_persons").text

def get_person(query: Union[str, int]):
    return requests.get(base_url + f"/get_person/{query}/").text

def create_person(username):
    response = requests.post(base_url+"/create_person/", {"username":username})
    return response.text

def delete_person(query: Union[str, int]):
    response = requests.delete(base_url+f"/delete/{query}")
    return response.text 

def update_person(old_data: Union[str, int], new_data: Union[str, int]):
    response = requests.post(base_url+"/update/", {"old_data": old_data, "new_data": new_data})
    return response.text 

if __name__ == "__main__":
    # disp(get_all_persons())
    # disp(get_person("Mohammed Yiwere"))
    disp(create_person("Mohammed Yiwere"))
    disp(create_person("Avonor Philip"))
    disp(create_person("Ernestina Fosu"))
    disp(create_person("Correy Schafer"))
    # disp(delete_person("Avonor Philip"))
    # disp(update_person("Muftawu Mohammed", "Suleimana Adams"))


'''
Completed tests
 - ✅ Get all person details 
 - ✅ Get specific person detials 
 - ✅ Create new person 
 - ✅ Delete person 
 - ✅ Update person details  
'''
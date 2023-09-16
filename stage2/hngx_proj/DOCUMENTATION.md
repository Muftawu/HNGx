# API STRUCTURE 

## ALL API ENDPOINTS 

    | endpoint                         |           Function              | 
    |----------------------------------|---------------------------------|
    | {domain}/api/create_person       | create new person               | 
    | {domain}/api/all_persons         | get all available person        | 
    | {domain}/api/get_person/user_id  | get specific person details     | 
    | {domain}/api/update/             | update specific person details  | 
    | {domain}/api/delete/user_id/     | delete a specific person        | 
   
## deployed endpoint = https://hngx-production-6712.up.railway.app/api/

## FORMAT FOR REQUESTS AND RESPONSES
    - All request and responses are in JSON formats
    - Successful request return a "200 OK HTTP RESPONSE"
    - Unsuccessful reqests return a "401 BAD REQUEST HTTP RESPONSE"
    - Also all 'person' objects have a created time and a modified time


## SAMPLE USAGE OF API USING PYTHON REQUESTS LIBRARY

   ### CREATING NEW USER/PERSON 
        HTTP METHOD = POST
        PARAMETERS = username
        - request = [requests.post("/api/create_person/", {"username":username})]
        - response = {"id":7,"name":"Mohammed Yiwere","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:18:46.497450Z"}
    
   ### GETTING PERSON DETAILS  
   where query can be either a person_id(integer) or person fullname(string)
        HTTP METHOD = GET
        PARAMETERS = username or user_id 
        
        - request = [requests.get("api/get_person/{query}/").text]
        - response = {"id":7,"name":"Mohammed Yiwere","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:18:46.497450Z"}

   ### GETTING ALL PERSONS
        HTTP METHOD = GET
        PARAMETERS = no parameters
        - request = [requests.get("api/all_persons/").text]
        - response = [{"id":3,"name":"Hafiz Osman","created":"2023-09-13T16:38:55.069357Z","updated":"2023-09-13T16:38:55.069357Z"},{"id":6,"name":"Avonor Philip","created":"2023-09-13T20:05:26.784502Z","updated":"2023-09-13T20:11:42.972145Z"},{"id":7,"name":"Mohammed Yiwere","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:18:46.497450Z"}]

   ### UPDATING PERSONS 
        HTTP METHOD = POST
        PARAMETERS = old_data, new_data
        where old_data = current name in database and new_data = new name to be inserted
        - request = [requests.post("api/update/", {"old_data": old_data, "new_data": new_data})]
        - response = {"info":"update successful","data":{"id":7,"name":"Suleimana Adams","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:26:24.497790Z"}}

   ### DELETING A PERSON
        HTTP METHOD = DELETE
        PARAMETERS = username or user_id
        where query can be either a person_id(integer) or person fullname(string)
        - request = [requests.delete("api/delete/{query}")]
        - response = {"Success":"Avonor Philip deleted successfully"}
# API STRUCTURE 

## ALL API ENDPOINTS 

    | endpoint                 |           Function              | 
    |--------------------------|---------------------------------|
    | /api/create_person       | create new person               | 
    | /api/all_persons         | get all available person        | 
    | /api/get_person/user_id  | get specific person details     | 
    | /api/update/             | update specific person details  | 
    | /api/delete/user_id/     | delete a specific person        | 
   

## FORMAT FOR REQUESTS AND RESPONSES
    - All request and responses are in JSON formats
    - Successful request return a "200 OK HTTP RESPONSE"
    - Unsuccessful reqests return a "401 BAD REQUEST HTTP RESPONSE"
    - Also all 'person' objects have a created time and a modified time


## SAMPLE USAGE OF API USING PYTHON REQUESTS LIBRARY

   - CREATING NEW USER/PERSON - POST method with parameter username
    [requests.post("/api/create_person/", {"username":username})]

    response = {"id":7,"name":"Mohammed Yiwere","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:18:46.497450Z"}
    
   - GETTING PERSON DETAILS - GET method with parameter query
   where query can be either a person_id(integer) or person fullname(string)
   [requests.get("api/get_person/{query}/").text]

   response = {"id":7,"name":"Mohammed Yiwere","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:18:46.497450Z"}

   - GETTING ALL PERSONS - GET METHOD [optional]
   [requests.get("api/all_persons/").text]

    response = [{"id":3,"name":"Hafiz Osman","created":"2023-09-13T16:38:55.069357Z","updated":"2023-09-13T16:38:55.069357Z"},{"id":6,"name":"Avonor Philip","created":"2023-09-13T20:05:26.784502Z","updated":"2023-09-13T20:11:42.972145Z"},{"id":7,"name":"Mohammed Yiwere","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:18:46.497450Z"}]

   - UPDATING PERSONS - POST method with parameters new_data and old_data
   where old_data = current name in database and new_data = new name to be inserted
   [requests.post("api/update/", {"old_data": old_data, "new_data": new_data})]

   response = {"info":"update successful","data":{"id":7,"name":"Suleimana Adams","created":"2023-09-13T22:18:46.497450Z","updated":"2023-09-13T22:26:24.497790Z"}}

   - DELETING A PERSON - DELETE method with parameter query
   where query can be either a person_id(integer) or person fullname(string)
   [requests.delete("api/delete/{query}")]

   response = {"Success":"Avonor Philip deleted successfully"}
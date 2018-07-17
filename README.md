# SimpleTracker

A Python server that provides a API REST for time tracking.

## Requirements

- python 3.6
- sqlite3
 

## Local installation

Install the python module dependencies:

`$ pip3 install -r requirements.txt`


## Running

In a terminal, type the following commands:

`$ export FLASK_APP=server.py`

`$ python -m flask run`

## Working with the API REST

### Add a time entry

- URL:  /worktime

- Method: POST

- URL params: None

- Data params:

	- startDate: start timestamp with format YYYY-MM-DDTHH:mm	 
	- endDate: end timestamp with format YYYY-MM-DDTHH:mm
	- category: type of entry
	- description: description of the entry
	
- Success response:

	- Code: 200
	- Content: { "id": id } Identifier of the new entry
	
- Error responses:
	- Code: 400	
	  Content: { "msg": "Incorrect params"}
	- Code 500
  	  Content: {"msg": "Entry could not be inserted" }
	

- Sample call:

`$ curl http://127.0.0.1:5000/worktime -X POST -d "startDate=2018-01-01T10:30&endDate=2018-01-01T11:30&category=working&description=Working in my time tracker project"`

   Response:

{
  "id": 1
}`

### Retrieving a time entry

- URL:  /worktime/id

- Method: GET

- URL params: None

- Data params: None
	
- Success response:

	- Code: 200
	- Content: 
		{
		  "category": "category of the entry", 
		  "description": "description of the entry", 
		  "end_date": "YYYY-MM-DDTHH:mm", 
		  "start_date": "YYYY-MM-DDTHH:mm",
		   "id": id
		}

	
- Error responses:
	- Code: 404
	  Content: { "msg": "Entry not found"}
	- Code 500
  	  Content: {"msg": "Entry could not be retrieved" }
	

- Sample call:

`$  curl http://127.0.0.1:5000/worktime/1`

Response:

`{
  "category": "working", 
  "description": "Working in my time tracker project", 
  "end_date": "2018-01-01T11:30:00", 
  "start_date": "2018-01-01T10:30:00",
   "id": 1
}`


### Retrieving time entries between dates

- URL:  /worktime

- Method: GET

- URL params: 

	- startDate: start timestamp with format YYYY-MM-DDTHH:mm 
	- endDate: end timestamp with format YYYY-MM-DDTHH:mm


- Data params: None

	
- Success response:

	- Code: 200
	- Content:
		[{
			   "category": "category of the entry", 
			   "description": "description of the entry", 
 			  "end_date": "YYYY-MM-DDTHH:mm", 
			  "start_date": "YYYY-MM-DDTHH:mm"
			  "id": id
			}, ...]
	
- Error responses:
	- Code: 400	
	  Content: { "msg": "Incorrect params"}
	- Code 500
  	  Content: {"msg": "Entries could not be retrieved" }


- Sample call:

`$ curl "http://127.0.0.1:5000/worktime?startDate=2018-01-01T10:30&endDate=2018-01-01T11:30"`

Response:

`{
  "category": "working", 
  "description": "Working in my time tracker project", 
  "end_date": "2018-01-01T11:30:00", 
  "start_date": "2018-01-01T10:30:00",
  "id": 1
}`



### Updating a time entry

- URL:  /worktime/id

- Method: PUT

- URL params: None

- Data params:

	- startDate: start timestamp with format YYYY-MM-DDTHH:mm	 
	- endDate: end timestamp with format YYYY-MM-DDTHH:mm
	- category: type of entry
	- description: description of the entry
	
- Success response:

	- Code: 200
	- Content: { "id": id } 
	
- Error responses:
	- Code: 400	
	  Content: { "msg": "Incorrect params"}
	- Code: 404
	  Content: { "msg": "Entry not found"}
	- Code 500
  	  Content: {"msg": "Entry could not be updated" }
	

- Sample call:

`$ curl http://127.0.0.1:5000/worktime/1 -X PUT -d "startDate=2018-01-01T11:30&endDate=2018-01-01T12:30&category=studying&description=Exams"`

   Response:

`{
  "id": 1
}`


### Deleting a time entry

- URL:  /worktime/id

- Method: DELETE

- URL params: None

- Data params: None

- Success response:

	- Code: 200
	- Content: { "id": id } 
	
- Error responses:
	- Code: 400	
	  Content: { "msg": "Incorrect params"}
	- Code: 404
	  Content: { "msg": "Entry not found"}
	- Code 500
  	  Content: {"msg": "Entry could not be removed" }
	

- Sample call:

`$ curl http://localhost:5000/worktime/1 -X DELETE`

   Response:

{
  "id": 1
}`


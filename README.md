# Morr-Assignment

## For Better experience use POSTMAN for testing API.

### Prerequisite to use the api:

#### 1) Python 3.6.9

#### 2) Django 3.1.5

#### 3) Django REST Framework

### Features Implemented in the API:

#### 1) CRUD operation for a contact book app

#### 2) Each contact has a unique email address

#### 3) APIs supports adding/editing/deleting contacts

### Bonus Features Implemented:

#### 1) Searching contacts by name and email address

#### 2) Search supports pagination and returns 10 items by default per invocation

#### 3) The code should scale-out for millions of contacts per contact book

### API url endpoint:

#### 1) "/api_get/" --> Returns all contacts in JSON format (Request Method - GET)

#### 2) "/api_get/<id>" --> Returns the detail of contact of the given id (Request Method - GET)

#### 3) "/api_add/" --> Creates a new contact in database (Request Method - POST)

#### 4) "/api_delete/<id>" --> Deletes the contact of the given id (Request Method - DELETE)

#### 5) "/api_update/<id>" --> Updates the contact details of the given id contact (Request Method - PUT)

#### 6) "/api_search/" --> Return a paginated list of contacts according to the search (Request Method - GET)

### ** Directions to use API **

#### 1) For updating record you should submit a form.

#### 2) For searching a record you should submit a form, specifying search details.

To Run please run the follwing command after running the docker
docker-compose build
docker-compose up

to run tests:-
python manage.py test

to run custom command
python manage.py print_task



Task Implemented :-


# Create a Python/Django project named "selteq_task".

# Implement authentication and authorization using JWT to secure endpoints and manage user access. Token should expire after 5 minutes

# Develop a Post API endpoint that stores a "title" of task and "duration" of task and creates the record for logged-in user in the database alongwith timestamps.

# Create a Get API to Get the list of created tasks of the logged-in user. It should only return last 4 tasks of the logged in user (must user filter.all() to get only last 4 tasks).

# Create Retrieve endpoint to retrieve a record by the logged-in user (must use raw SQL query for this endpoint).

# Create Update endpoint such that only the task "title" can be update. "duration" cannot be updated (must use raw SQL query for this endpoint).

# Create Delete endpoint such that the logged-in user can delete only those tasks that he created.

# test cases for all these endpoint

# Create a custom command that prints all the tasks in database one by one after every 10 seconds (not using print())

#  Utilize Celery in conjunction with Redis to manage.

# Implement scheduled tasks using Celery that will print the task "title", "duration" and timestamps of user-added tasks(added by user with id 1) every one minute.

# Configure Docker to run the Redis service and the Django application.




API endpoints:- 

""""
# Create User

POST:- http://localhost:8000/user/create/ 

Eg:- 

data = {
    "username": "john_do4e",    
    "password": "password123"
}

response = requests.post(url="http://localhost:8000/user/create/" , data=data)

""""


""""
# User Login

POST:-  http://localhost:8000/login/

Eg:- 

data = {
    "username": "john_do4e",
    
    "password": "password123"
}

response = requests.post(url="http://localhost:8000/login/" , data=data)

return get Token

""""


""""

# Refresh Token

POST:- http://localhost:8000/token/refresh/

Eg:- 


data = {"refresh": token}

response = requests.post(url="http://localhost:8000/token/refresh/" ,data= data)

""""


""""
# Get Token

POST:- http://localhost:8000/token/

Eg:- 

data = {
    "username": "john_do4e",
    
    "password": "password123"
}

response = requests.post(url="http://localhost:8000/token/" , data=data)

""""


""""
# Create Task 

POST:- http://localhost:8000/task/create/

Eg:-

data= {
    "title": "Task 555",
    "duration": 40

}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.post(url="http://localhost:8000/task/create/" , headers = headers ,json=data)

""""


""""
# Get List of Tasks

GET:- http://localhost:8000/task/list/

Eg:- 

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get(url="http://localhost:8000/task/list/" , headers =  headers )

""""


""""

# Get task

GET:- http://localhost:8000/task/1

Eg:- 

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.get(url="http://localhost:8000/task/list/" , headers =  headers )

""""


""""

# Delete Task


Delete:- http://localhost:8000/task/1

Eg:- 

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.delete(url="http://localhost:8000/task/list/" , headers =  headers )

""""


""""

# Update Task

PUT:- http://localhost:8000/task/1

Eg:- 

data= {
    "title": "Task updated",
    

}

headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

response = requests.put(url="http://localhost:8000/task/list/" , headers =  headers, json=data)

""""

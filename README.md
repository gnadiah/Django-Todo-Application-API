# Python Django Todo Application API

## Project Plan

- [x] Create a Todo Application API with default django framework (API v1.0)
- [ ] Create a Todo Application API with restful django framework (API v2.0)
- [ ] Add authentication for Todo Application API (API v2.1)
- [ ] Create SSO login for Todo Application API (API v2.2)
- [ ] Multiple user in one Todo Template (API v3.0)

## Requirements

### Python Version

- Python >= 3.8.10

### Operating System

- Ubuntu >= 21.10
- Debian >= 9.0
- Kali Linux >= 2020.1

## Application Setup

### File Setup

- Create .env file at root directory

- Create SECRET_KEY variable in .env file or use this command

`echo SECRET_KEY=<your-secret-key> > .env`

```bash
echo SECRET_KEY=SUPER-ULTIMATE-SECRET-KEY > .env
```

---

### Package Setup

```bash
sudo apt install python3-pip
sudo pip3 install virtualenv
```

---

### Environment Setup

- Create virtual environment

```bash
virtualenv venv
```

- Enter your virtual environment

```bash
source venv/bin/activate
```

- Install python requirements package

```bash
pip install -r requirements.txt
```

---

### Database Setup

- Make migrations database

```bash
python manage.py makemigrations
```

- Choose app database to make makemigrations

`python manage.py makemigrations <API-VERSION>`

```bash
python manage.py makemigrations api_v1_0
```

- Migrate database

```bash
python manage.py migrate
```

## Application Start Up Command

- Run server at default port (port: 8000)
  
```bash
python manage.py runserver
```

- Run server at specified port (port: 8000, 5000, 3000, ...)

`python manage.py runserver <YOUR-PORT>`

```bash
python manage.py runserver 8000
```

```bash
python manage.py runserver 5000
```

```bash
python manage.py runserver 3000
```

## API Documentation

`If you use API without version, default API will be latest version`

### Latest API Documentation (v1.0)

#### Get all task

- API endpoint: `/api/v1.0/getTask/`
- Description: Get all task
- Method: `GET`
- Request data: `None`
- Response data:

```json
{
    "message": "Task got successfully",
    "task": 
        [
            {
                "id": "<TASK-ID>",
                "title": "<TASK-TITLE>",
                "content": "<TASK-CONTENT>",
                "created_at": "<TASK-CREATED-AT>",
                "updated_at": "<TASK-UPDATED-AT>"
            },
            {
                "id": "<TASK-ID>",
                "title": "<TASK-TITLE>",
                "content": "<TASK-CONTENT>",
                "created_at": "<TASK-CREATED-AT>",
                "updated_at": "<TASK-UPDATED-AT>"
            },
            ...
        ]
}
```

---

#### Get specific task

- API endpoint: `/api/v1.0/getSpecificTask/<TASK-ID>`
- Description: Get specific task
- Method: `GET`
- Request data: `None`
- Response data:

```json
{
    "message": "Task got successfully",
    "task":
        {
            "id": "<TASK-ID>",
            "title": "<TASK-TITLE>",
            "content": "<TASK-CONTENT>",
            "created_at": "<TASK-CREATED-AT>",
            "updated_at": "<TASK-UPDATED-AT>"
        }
}
```

---

#### Create new task

- API endpoint: `/api/v1.0/createTask/`
- Description: Create a new task
- Method: `POST`
- Request Data:

```json
{
    "title": "<TASK-TITLE>",
    "content": "<TASK-CONTENT>"
}
```

- Response data:

```json
{
    "message": "Task created successfully",
    "task": 
        {
            "id": "<TASK-ID>",
            "title": "<TASK-TITLE>",
            "content": "<TASK-CONTENT>",
            "created_at": "<TASK-CREATED-AT>",
            "updated_at": "<TASK-UPDATED-AT>"
        }
}
```

---

#### Edit task

- API endpoint: `/api/v1.0/editTask/<TASK-ID>/`
- Description: Edit task
- Method: `PATCH`
- Request data:

```json
{
    "title": "<TASK-TITLE>", // If you want to change title, field it
    "content": "<TASK-CONTENT>" // If you want to change content, field it
}
```

- Response data:

```json
{
    "message": "Task edited successfully",
    "task": 
        {
            "id": "<TASK-ID>",
            "title": "<NEW-TASK-TITLE>",
            "content": "<NEW-TASK-CONTENT>",
            "created_at": "<TASK-CREATED-AT>",
            "updated_at": "<TASK-UPDATED-AT>"
        }
}
```

---

#### Delete task

- API endpoint: `/api/v1.0/deleteTask/<TASK-ID>/`
- Description: Edit task
- Method: `PATCH`
- Request data: `None`
- Response data:

```json
{
    "message": "Task deleted successfully"
}
```

## API Creator

### Nguyen Hai Dang (ndangmods)

- [Facebook](https://www.facebook.com/ndangmods)
- [Twitter](https://twitter.com/ndangmods)
- [Instagram](https://instagram.com/dangn_ndang)
- [GitLab](https://gitlab.com/ndangmods)
- [GitHub](https://github.com/ndangmods)

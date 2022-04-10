# Python Django Todo Application API

## Project Plan

- [x] Create a Todo Application API with default django framework
- [ ] Create a Todo Application API with restful django framework
- [ ] Add authentication for Todo Application API
- [ ] Create SSO login for Todo Application API
- [ ] Multiple user in one Todo Template

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

```bash
echo SECRET_KEY=<your-secret-key> > .env
```

### Package Setup

```bash
sudo apt install python3-pip
sudo pip3 install virtualenv
```

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

### Database Setup

- Make migrations database

```bash
python manage.py makemigrations
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

```bash
python manage.py runserver <YOUR-PORT>
```

```bash
python manage.py runserver 8000
```

```bash
python manage.py runserver 5000
```

```bash
python manage.py runserver 3000
```

## API Creator

### Nguyen Hai Dang (ndangmods)

- [Facebook](https://www.facebook.com/ndangmods)
- [Twitter](https://twitter.com/ndangmods)
- [Instagram](https://instagram.com/dangn_ndang)
- [GitLab](https://gitlab.com/ndangmods)
- [GitHub](https://github.com/ndangmods)

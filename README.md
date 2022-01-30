
# Online Voting Created Using Django 
This Online Voting System Was Developed With Django(Python Framework).


If you like this project, then ADD a STAR ⭐️  to this project 👆

This Online Voting System is a web-based application built using Django can serve as the automated voting system for organizations and/or institutions. 
The system works like the common election manual system of voting whereas the system must be populated by the list of the candidates, and events.
The Online voting system can help a certain event organization or school to minimize the voting time duration because aside providing the voters an online platform to vote, 
the system will automatically count the votes for each candidate. The system has 2 sides of the user interface which are the administrator and voters side. The admin user 
is in charge to populate and manage the data of the system and the voter side which is where the voters will choose their candidates and submit their votes.


## Features:

- [x] Single votes in single event
- [x] Changeable order of positions to show in the ballot
- [x] CRUD candidates
- [x] CRUD positions
- [x] Email verification
- [x] Reset Password

### A. Admin Users Can

1. See Overall Summary of Votes
2. Reset Votes
3. Manage Candidates (CRUD)
4. Manage Events (CRUD)

### B. Voters Can
1. Register
2. Login
3. Verify with OTP (This can be overwritten in `settings.py` file)
4. Votes for their favourite candidates


## Support Developer
1. Add a Star 🌟  to this 👆 Repository
2. Follow on Github



### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]



### Installation
**1. Create a Folder where you want to save the project**

**2. Clone this project**
```
$  git clone https://github.com/roshan082/election_system.git
```

Then, Enter the project
```
$  cd election_system
```

**3. Install Requirements from 'requirements.txt'**
```python
$  pip3 install -r requirements.txt
```

**4. Run migrations and migrate**
```python manage.py makemigrations```
```python manage.py migrate```

**5. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

Command for Linux:
```python
$ python3 manage.py runserver
```

**6. Login Credentials**

Create Super User (HOD)
Command for PC:
```
$  python manage.py createsuperuser
```

Command for Mac:
```
$  python3 manage.py createsuperuser
```

Command for Linux:
```
$  python3 manage.py createsuperuser
```



Then Add Email and Password

**or Use Default Credentials**

*For HOD /SuperAdmin*
Email: admin@admin.com
Password: admin

*For Staff*
Email: staff@staff.com
Password: staff

*For Student*
Email: student@student.com
Password: student


## How the system works
Administrator is required to have created candidates. 
Before creating candidates, the admin must have create Events
After doing this, the voters can vote (provided that they are registered and verified)

## How do voters get verified ?
OTP is sent to voter's email address.

## Can OTP verification be bypassed ?
Yeah, sure.
Open `settings.py` and toggle `SEND_OTP` to  `False`
Then, wait till server restarts


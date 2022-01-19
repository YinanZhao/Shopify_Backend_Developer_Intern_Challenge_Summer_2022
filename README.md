# Shopify Backend Developer Intern
> The task is to build an inventory tracking web application for a logistics company. More information can be found at [Shopify Backend Developer Intern 
Challenge - Summer 2022](https://docs.google.com/document/d/1z9LZ_kZBUbg-O2MhZVVSqTmvDko5IJWHtuFmIu_Xg1A/edit#)
### Task description:
> The task includes a basic Inventory app with CRUD functionality, an additional functionality of create locations and assigning inventory so specific ones

## Demo:
Home Page:
![Alt text](images/Demo_Home_Page.png?raw=true)

Locations:
![Alt text](images/Demo_Locations.png?raw=true)

Modify or delete an item:
![Alt text](images/Demo_Modify_Delete_Item.png?raw=true)

## To run it:
Clone repository and go to it
```
# Clone the repository using
git clone https://github.com/YinanZhao/Shopify_Backend_Developer_Intern_Challenge_Summer_2022.git

# Open and go to project path location using Terminal/Command line
cd this-project/...
```

### 1. MacOS
```
# Create Python virtual environment, with name venv
virtualenv venv

# Activate the Python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt

```
### 2. Linux
```
# Create Python virtual environment, with name venv
python3 -m venv venv

# Activate the Python virtual environment
source venv/bin/activate

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```
### 2. Windows
```
# Create python virtual environment
conda create --name venv python=3.8

# Activate the python virtual environment
conda activate venv

# Install the requirements for the project into the virtual environment
pip install -r requirements.txt
```

## Run the server in development mode
Go one more layer to get access to manage.py
```
cd inventorytracker
```
Run the server
```
python manage.py runserver
```
Local API calls can be made at: http://127.0.0.1:8000/

## Testing
To test different pages and their APIs
```
python manage.py test
```

## Database migrations

For creating migrations, run the following commands: 

```
python manage.py makemigrations
```
```
python manage.py db migrate
```




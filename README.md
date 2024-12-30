# Secure Password Manager
A web-based password manager built with Flask that allows users to securely store and manage their passwords. Features temporary hosting capabilities through ngrok for development and testing.

## Features
- Secure password storage with encryption
- Add, view, and delete passwords
- Show/hide password 
- Temporary public access via ngrok tunnel

## Security Features
- Passwords are encrypted using Fernet symmetric encryption
- User passwords are hashed using SHA-256
- Session management with Flask-Login
- Secure key storage

## Installation

1. Clone the repository:
```bash
git clone <https://github.com/MRXz194/password_manager>
cd password-manager
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Set up your environment:
```bash
# check the file .env.example for details

```

5. Create ngrok configuration:
```bash
version: "2"
authtoken: your-ngrok-authtoken-here
tunnels:
  password-manager:
    proto: http
    addr: 8080
```

## Running the Appplication
- you can run app.bat to run the app
- you can use run.ngrok.bat to run ngrok s


## Security Notes

### Important Security Considerations

1. No commit sensitive files:
   - `.env` env file
   - `*.db` database files
   - `*.key` encryption key files
   - `ngrok.yml` with your authtoken

2. Generate secret keys:
   - Use the provided command to generate a secure SECRET_KEY

3. Development & Production:
   - The current setup is for development/testing only
   - I use ngrok for temporary public access


## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Login
- cryptography
- python-dotenv
- Werkzeug

you can use vercal instead of ngrok to host public this web based :333 meow 





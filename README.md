# Secure Password Manager
A web-based password manager built with Flask that allows users to securely store and manage their passwords. Features temporary hosting capabilities through ngrok for development and testing.

## Features
- User registration and authentication
- Secure password storage with encryption
- Add, view, and delete passwords
- Show/hide password functionality
- Modern and responsive UI
- Flash messages for user feedback
- Temporary public access via ngrok tunnel

## Security Features

- Passwords are encrypted using Fernet symmetric encryption
- User passwords are hashed using SHA-256
- Session management with Flask-Login
- Secure password viewing with toggle functionality
- Environment-based configuration
- Secure key storage

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd password-manager
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux
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

1. Never commit sensitive files to version control:
   - `.env` file containing environment variables
   - `*.db` database files
   - `*.key` encryption key files
   - `ngrok.yml` with your authtoken

2. Generate strong secret keys:
   - Use the provided command to generate a secure SECRET_KEY
   - Never reuse encryption keys across installations
   - Keep your encryption key file secure

3. Development vs Production:
   - The current setup is for development/testing only
   - I use ngrok for temporary public access


## Dependencies

- Flask
- Flask-SQLAlchemy
- Flask-Login
- cryptography
- python-dotenv
- Werkzeug





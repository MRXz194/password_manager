
A web-based password manager built with Flask . Features temporary hosting capabilities through ngrok for development and testing.

- Secure password storage with encryption
- Temporary public access via ngrok tunnel

## Security Features
-  Fernet symmetric encryption
- User passwords are hashed using SHA-256
- Secure key storage

## Installation

1. Clone :
```bash
git clone <https://github.com/MRXz194/password_manager>
cd password-manager
```

2. Create env
```bash
python -m venv venv
venv\Scripts\activate  
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Set up env:
```bash
# check the file .env.example for details

```

5. ngrok config:
```bash
version: "2"
authtoken: ngrok-authtoken-here
tunnels:
  password-manager:
    proto: http
    addr: 8080
```

## Run the app
- you can run app.bat to run the app
- you can use run.ngrok.bat to run ngrok s




### Important Considerations

1. 
   - `.env` env file
   - `*.db` database files
   - `*.key` encryption key files
   - `ngrok.yml` with your authtoken

2. Generate secret keys:
   - Use the provided command to generate a secure SECRET_KEY
3. Development & Production:
   - The current setup is for development/testing only
   - I use ngrok for temporary public access


you can use vercal instead of ngrok to host public this web based :333 meow 





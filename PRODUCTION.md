# Production Deployment Guide

###  Setup
```bash
mkdir /var/www/password_manager
cd /var/www/password_manager
git clone <your-repo-url> .

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

## Maintenance
1. Regular updates:
   ```bash
   pip install --upgrade -r requirements.txt
   ```




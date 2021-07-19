# samagra_odk_data_automation

## Deployment steps:
git clone https://github.com/piyush-singhal/samagra_odk_data_automation.git
pip3 install -r requirements.txt

Copy `sample.env` to .env and update the credentials for production

gunicorn3 --workers=3 -b :8080 application:api

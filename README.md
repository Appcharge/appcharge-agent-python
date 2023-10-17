# Python mock publisher webhooks template
First of all you need to set up all environment variables (.env.sample as an example).

### How to run manually (python3 required)
pip3 install -r requirements.txt
python3 start.py

### How to build docker image
docker build -t appcharge/webhook-flask .

### How to run the container locally
docker run -p 8000:8000 appcharge/webhook-flask

### Where to get the key
Go to the admin panel, open the integration tab, if you are using signature authentication - copy the key from the primary key field, if you are using encryption, take the key from the primary key field and the IV from the secondary key field.

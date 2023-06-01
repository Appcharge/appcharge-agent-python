# Python mock publisher webhooks template

### How to run manually (python3 required)
pip3 install -r requirements.txt
IV='[IV GOES HERE]' KEY='[KEY GOES HERE]' APP_SECRET=[FACEBOOK APP SECRET] python3 start.py

### How to build docker image
docker build -t appcharge/webhook-flask .

### How to run the container locally
docker run --rm -it -e KEY='[KEY GOES HERE]' -e IV='[IV GOES HERE]' -e APP_SECRET='[FACEBOOK APP SECRET]' -p8080:8080 appcharge/webhook-flask

### Where to get the key
Go to the admin panel, open the integration tab, if you are using signature authentication - copy the key from the primary key field, if you are using encryption, take the key from the primary key field and the IV from the secondary key field.
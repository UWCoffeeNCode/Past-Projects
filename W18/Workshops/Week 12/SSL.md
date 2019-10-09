First, you have to answer a challenge to get a certificate and key from Lets Encrypt

```
git clone https://github.com/letsencrypt/letsencrypt
cd letsencrypt/
./letsencrypt-auto certonly --manual --email zejacobi@gmail.com -d deltagreen.zachjacobi.com
```

This will require you to have a file at a certain URL. Note that this file and its URL are by definition not secret and don't need to be in your .gitignore.

For example they may want:

http://deltagreen.zachjacobi.com/.well-known/acme-challenge/k9s7WeOPg3HdSjwlAqEVRxnezsGGe-CFOwPfOcU3VgU

To host:

k9s7WeOPg3HdSjwlAqEVRxnezsGGe-CFOwPfOcU3VgU.QBkCfzPq0mKXIJSktgl4_b7psKazh3MSZ8juWnZbJbg

I've normally done this by modifying my API to host this file. 

`LetsEncryptConfig.py`:
```python
ROOT = '/.well-known/acme-challenge'
ENDPOINT = '/k9s7WeOPg3HdSjwlAqEVRxnezsGGe-CFOwPfOcU3VgU'
RESPONSE = 'k9s7WeOPg3HdSjwlAqEVRxnezsGGe-CFOwPfOcU3VgU.QBkCfzPq0mKXIJSktgl4_b7psKazh3MSZ8juWnZbJbg'

```

`API/LetsEncrypt.py`:
```python
from flask import Blueprint

from LetsEncryptConfig import ENDPOINT, RESPONSE

Challenge = Blueprint('challenge', __name__)


@Challenge.route(ENDPOINT, methods=['GET'])
def answer_acme_challenge():
    return RESPONSE, 200
```

`server.py`:
```python
from flask import Flask
from API.LetsEncrypt import Challenge
from LetsEncryptConfig import ROOT

app = Flask(__name__)

app.register_blueprint(Challenge, url_prefix=ROOT)
host = '0.0.0.0'
port = 80

if __name__ == "__main__":
    app.run(host, port=port, debug=False)
```

What I normally do is get to the point where I'm being challenged, pull new code, then answer affirmative to the dialogue in the Let's Encrypt program.

Lets Encrypt will then create for you a Key and Certificate.

```
- Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/deltagreen.zachjacobi.com/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/deltagreen.zachjacobi.com/privkey.pem
   Your cert will expire on 2018-06-12. To obtain a new or tweaked
   version of this certificate in the future, simply run
   letsencrypt-auto again. To non-interactively renew *all* of your
   certificates, run "letsencrypt-auto renew"
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
```

If you need a local key and cert, run:

`openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365`

Open your .gitignore and add on two lines at the end:
```.ignore
key.pem
cert.pem
```

NEVER, EVER COMMIT A KEY OR CERT TO A PUBLIC DIRECTORY.

BAD THINGS CAN HAPPEN.


Anyway, over on your server, you want to run the following commands to move the key and cert to the expected location:
```bash
cp -L /etc/letsencrypt/live/deltagreen.zachjacobi.com/fullchain.pem ./cert.pem
cp -L /etc/letsencrypt/live/deltagreen.zachjacobi.com/privkey.pem ./key.pem
```

It is _very_ easy to make Flask run HTTP. Just edit the server like so:

`server.py`:
```python
    context = ('cert.pem', 'key.pem')
    port = 443
    app.run(host, port=port, debug=False, ssl_context=context)
```

You can see this in action:
https://deltagreen.zachjacobi.com/

This text is CC-BY-SA (C) 2018 Zachary Jacobi

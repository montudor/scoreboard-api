# Simple Scoreboard API

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/for-robots.svg)](https://forthebadge.com)

Just a small basic API built with the [Django REST Framework](https://www.django-rest-framework.org)
to save scores from my Tetris clone.

## Development

In order to prepare the development environment on your local machine you must run the following commands.
It may be wise to do this in a Python virtual environment.
```
pip install -r requirements.txt
python manage.py migrate
```

Then, to launch the API at [localhost:8000](http://localhost:8000), run this command:
```
python manage.py runserver
```

## Production

### Setting up the environment

In order to deploy this API in production, you must ensure you have Docker and Docker Compose installed on the server.
You should also remember to change the SECRET_KEY by, first, creating the following `docker-compose.override.yml` file.
```yml
version: "3.8"

services:
  web:
    env_file:
      .env
```

then putting the secrets in a `.env` file, like so:
```
SECRET_KEY=<SECRET>
```

### How do I generate a secret key?

You can do this on your local development machine by first executing the following command.
```
python manage.py shell
```

Then typing the following lines:
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

This will output a new secret key directly below.

### Final steps

Finally, run the following commands:

```
make up
make migrate
make collectstatic
```

This will expose the API at port 8000. At this point you want to configure nginx to reverse proxy to that port.
Here is an example configuration for nginx:

```nginx
server {
    server_name <SERVER NAME>;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_pass http://localhost:8000;
    }

    location /static {
        root /path/to/app/static;
    }

    listen [::]:443 ssl ipv6only=on; # managed by Certbot
    listen 443 ssl; # managed by Certbot
    ssl_certificate /etc/letsencrypt/live/<SERVER NAME>/fullchain.pem; # managed by Certbot
    ssl_certificate_key /etc/letsencrypt/live/<SERVER NAME>/privkey.pem; # managed by Certbot
    include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
    ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}
```

# Affinda resthook client example

## Setup website

### Download python

[https://www.python.org/downloads/](https://www.python.org/downloads/)

### Install dependencies

Run this inside the folder of this repo.

```shell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Migrate database

```shell
python manage.py migrate
```

### Run server

```shel
python manage.py runserver
```

Now you can visit the website at [http://localhost:8000](http://localhost:8000)

## Setup ngrok

### Download ngrok

[https://ngrok.com/download](https://ngrok.com/download)

### For linux

```shell
ngrok http 8000
```

### For windows

Go to ngrok's installation folder

```shell
ngrok.exe http 8000
```

## Setup api key, webhook key

Go to `affinda_resthook_client/views.py` and update the `api_key` and `sig_key` variables accordingly.

## Create webhook subscription

Use the URL provided by ngrok in the last step to set up the webhook subscription.

For example:

If the URL provided by ngrok is `https://<some-ngrok-url>`

Then the URL to use as `targetUrl` is `https://<some-ngrok-url>/receive/`

Now you should be ready to start receiving webhooks.

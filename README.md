# YT2MP3 (YouTube to MP3)

## Description
- A Django application that converts Youtube videos to mp3 format.
- Downloads the highest possible bitrate.

### Setting up the app

**1. Create a virtual environment and activate**

shell
```
$ python -m venv venv
$ source venv/bin/activate
```

**2. Install dependencies**

shell
```
(venv) $ python -m pip install -r requirements.txt

-- or --

(venv) $ pip install -r requirements.txt
```

**3. Install Redis as Celery Broker and Database Back End**

Ubuntu/Debian
```
(venv) $ curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

(venv) $ echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

(venv) $ sudo apt update
(venv) $ sudo apt install redis
```

Start redis server, open a new shell process
```
$ redis-server
```

> Refer to the installation guide at redis [docs](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)

**3. Task Queue**
> Note: Celery needs a message broker to communicate with programs that send tasks to the task queue.
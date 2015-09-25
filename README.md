## Prerequisites

Install Flask:

```
$ pip install --user Flask
```

## Usage

Run `server.py` with Python:

```
# python server.py
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
```

The server is now available at [127.0.0.1:8080](http://127.0.0.1:8080/).

![](https://raw.githubusercontent.com/earldouglas/hello-python-web/7b8372497416ab95378f6cdc5f01683ea9e92f23/readme/screenshot.png)

## Usage with Docker

Create a Docker image with `docker build`:

```
$ docker build -t hello-python-web .
```

Inspect the Docker image with `docker images`:

```
$ docker images
REPOSITORY        TAG     IMAGE ID      CREATED        VIRTUAL SIZE
hello-python-web  latest  7684dc73147e  3 minutes ago  731.7 MB
debian            sid     e7d52d7d94ef  2 weeks ago    126.5 MB
```

Run *hello-python-web* with `docker run`:

```
$ docker run -p 8080:8080 hello-python-web
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

The server is now available at [127.0.0.1:8080](http://127.0.0.1:8080/).

```
$ curl -i -s localhost:8080
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 13
Server: Werkzeug/0.10.4 Python/2.7.10
Date: Fri, 25 Sep 2015 00:12:38 GMT

Hello, world!
```

Tag the Docker image with `docker tag`:

```
$ docker tag 7684dc73147e earldouglas/hello-python-web:1.0.0
```

Inspect the Docker tag with `docker images`:

```
$ docker images
REPOSITORY                    TAG     IMAGE ID      CREATED         VIRTUAL SIZE
hello-python-web              latest  7684dc73147e  24 minutes ago  731.7 MB
earldouglas/hello-python-web  1.0.0   7684dc73147e  24 minutes ago  731.7 MB
debian                        sid     e7d52d7d94ef  2 weeks ago     126.5 MB
```

If necessary, sign in to Docker with `docker login`:

```
$ docker login
```

Publish the Docker image with `docker push`:

```
$ docker push earldouglas/hello-python-web
```

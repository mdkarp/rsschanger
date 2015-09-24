FROM debian:sid

RUN apt-get -y update
RUN apt-get install -y python python-pip

RUN pip install Flask

COPY . /hello-python-web

EXPOSE 80

CMD ["python", "/hello-python-web/server.py"]

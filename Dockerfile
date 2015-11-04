FROM python:2.7

COPY . /hello-python-web

RUN pip install -r /hello-python-web/requirements.txt

CMD ["python", "/hello-python-web/server.py"]

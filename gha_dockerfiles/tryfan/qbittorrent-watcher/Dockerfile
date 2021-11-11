FROM python:3-alpine3.10
COPY requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /code
ADD watcher.py /code/
ADD config.* /code/
CMD [ "python", "watcher.py" ]

FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN mkdir /srv/logs
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/
EXPOSE 8000
ENTRYPOINT ["/code/docker_entrypoint.sh"]

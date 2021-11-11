FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN cd /code && pip3 install -r requirements.txt

RUN cd /code && python3 setup.py install

RUN cd /code/wsgi/openshift/ && \
    python3 manage.py migrate --noinput && \
    python3 manage.py migrate --noinput --run-syncdb
#    python3 manage.py createsuperuser

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3", "/code/wsgi/openshift/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]

FROM python:2.7-slim
ENV BOOTSTRAP_DEBUG=false BOOTSTRAP_USERNAME=admin BOOTSTRAP_PASSWORD=secret BOOTSTRAP_URL="http://localhost:5000"
COPY requirements.txt /requirements.txt
COPY gunicorn_config.py /gunicorn_config.py
COPY bootstrap.py /bootstrap.py
RUN pip install -r /requirements.txt && \
    rm /requirements.txt && \
    pip install gunicorn futures
CMD gunicorn -c gunicorn_config.py bootstrap:app
EXPOSE 5000
VOLUME ["/munki_repo"]

FROM tiangolo/uwsgi-nginx-flask:flask

COPY static /app/callaborate/static
COPY templates /app/callaborate/templates
COPY app_settings.py.example /app/callaborate/app_settings.py.example
COPY setup.py /app/callaborate/setup.py
COPY callaborate /app/callaborate/callaborate
COPY tropo_call_script.py /app/callaborate/tropo_call_script.py
COPY main.py /app/main.py

RUN cd /app/callaborate && \
    python setup.py install && \
    mkdir -p /app/config/log

ENV APP_SETTINGS /app/config/app_settings.py

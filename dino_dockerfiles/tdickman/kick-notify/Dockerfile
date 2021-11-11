FROM        python:2-onbuild
COPY        . /kick-notify
ENV         PYTHONPATH /kick-notify
RUN         pip install -r /kick-notify/requirements.txt
ENTRYPOINT  ["python", "/kick-notify/kicknotify/run.py"]

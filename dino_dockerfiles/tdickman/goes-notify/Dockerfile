FROM        python:2-onbuild
COPY        . /goes-notify
ENV         PYTHONPATH /goes-notify
RUN         pip install -r /goes-notify/requirements.txt
ENTRYPOINT  ["python", "/goes-notify/goesnotify/run.py"]

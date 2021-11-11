FROM        python:3-onbuild
COPY        . /jetcom-crawl
ENV         PYTHONPATH /jetcom-crawl
RUN         pip3 install -r /jetcom-crawl/requirements.txt
ENTRYPOINT  ["python3", "/jetcom-crawl/jetcomcrawl/run.py"]

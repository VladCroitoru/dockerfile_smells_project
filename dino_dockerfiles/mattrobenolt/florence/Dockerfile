FROM python:2.7-alpine

RUN pip install --no-cache-dir click==6.6
COPY main.py /usr/local/bin/florence

ENTRYPOINT ["/usr/local/bin/florence"]
CMD ["--help"]

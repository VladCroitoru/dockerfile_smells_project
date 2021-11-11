FROM python:3.8-buster

ADD setup.sh .
RUN \
  mkdir -p /data /workspace && \
  /bin/bash setup.sh
ADD run-pollination.py /data
ENTRYPOINT [ "python3", "/data/run-pollination.py" ]

from python:alpine

RUN pip install requests
COPY src/ /opt/resource/python
ENV PYTHONPATH=${PYTHONPATH}:/opt/resource/python
RUN cd /opt/resource/python && python -m unittest

COPY cmd/check /opt/resource/check
COPY cmd/in /opt/resource/in
COPY cmd/out /opt/resource/out
RUN chmod +x /opt/resource/check /opt/resource/in /opt/resource/out

FROM python:3
ENV LANG C.UTF-8
ADD requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && rm -rf /tmp/requirements.txt

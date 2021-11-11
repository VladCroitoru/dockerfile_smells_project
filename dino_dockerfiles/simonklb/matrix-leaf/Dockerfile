FROM python:3.5-alpine

ADD setup.py /matrix-leaf/setup.py
ADD VERSION /matrix-leaf/VERSION
ADD requirements.txt /matrix-leaf/requirements.txt
ADD leaf /matrix-leaf/leaf

RUN apk update && apk add git
RUN pip install -r /matrix-leaf/requirements.txt
RUN pip install /matrix-leaf
RUN pip check

# Create the debug.log file so that it can be mounted on the host
RUN touch debug.log

ENTRYPOINT ["matrix-leaf"]

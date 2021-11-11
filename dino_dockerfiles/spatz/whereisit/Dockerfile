FROM python:slim

RUN mkdir /usr/src/whereisit
COPY setup.py /usr/src/whereisit
COPY whereisit /usr/src/whereisit/whereisit
RUN pip install --no-cache-dir -e /usr/src/whereisit
ENV PYTHONUNBUFFERED 1
CMD whereisit /etc/whereisit.toml

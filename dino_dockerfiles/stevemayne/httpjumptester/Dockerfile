FROM python:2.7
MAINTAINER Steve Mayne <contact@backupmachine.com>

# Install required packages and remove the apt packages cache when done.

RUN apt-get update && \
    apt-get install -qy \
	nano \
	python-pip  && \
  	rm -rf /var/lib/apt/lists/*

COPY src/ /code

RUN pip install -r /code/requirements.txt
RUN chmod +x /code/jump.py

ENV IDENTIFIER Unnamed
EXPOSE 8080

RUN groupadd -r jumper && useradd -r -g jumper jumper
RUN chown -R jumper.jumper /code
USER jumper

CMD ["/code/jump.py"]

FROM ubuntu:14.04
MAINTAINER Daniel Watkins <daniel@daniel-watkins.co.uk>

RUN apt-get update
RUN apt-get install -y python-pip python-dev
RUN pip install klaus

EXPOSE 8080

CMD ["/bin/bash", "-c", "klaus --host 0.0.0.0 /srv/git/*"]

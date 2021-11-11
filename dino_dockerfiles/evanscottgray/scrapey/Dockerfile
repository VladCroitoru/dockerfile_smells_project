# scrapey
#
# VERSION               0.0.1

FROM cmfatih/phantomjs
MAINTAINER Evan Gray <evan.gray@rackspace.com>

RUN apt-get update && apt-get install -y curl && curl https://bootstrap.pypa.io/get-pip.py | python -

ENTRYPOINT git clone https://github.com/evanscottgray/scrapey.git && \
               cd scrapey && \
               pip install -r requirements.txt && \
               python scrapey.py

EXPOSE 5000

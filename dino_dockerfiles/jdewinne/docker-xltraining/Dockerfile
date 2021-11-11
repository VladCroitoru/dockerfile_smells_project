FROM ubuntu:latest
MAINTAINER Joris De Winne <jdewinne@xebialabs.com>
RUN apt-get update
RUN apt-get install -y python-pip zip
RUN pip install jinja2
RUN pip install markdown

VOLUME /data
WORKDIR /data

CMD ["/data/generate_all_decks.sh"]

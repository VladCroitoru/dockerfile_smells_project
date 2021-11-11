FROM phusion/baseimage

MAINTAINER Alexander Gil

# spunkybot
RUN apt-get update && \
    apt-get -y install git python-dev build-essential libsqlite3-dev && \
    apt-get clean
RUN git clone https://github.com/SpunkyBot/spunkybot.git /opt/spunkybot
RUN cd /opt/spunkybot && git checkout 1.9.0
RUN chmod +x /opt/spunkybot/spunky.py

# move the database so its easily used with a docker volume.
RUN mkdir /opt/spunkybot/sqlite
RUN sed -i -e 's/data.sqlite/\/opt\/spunkybot\/sqlite\/data.sqlite/g' /opt/spunkybot/spunky.py

#
ENTRYPOINT ["/opt/spunkybot/spunky.py"]
CMD ["/root/spunkybot"]

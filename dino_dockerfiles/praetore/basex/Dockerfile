FROM java:8
MAINTAINER Darryl Amatsetam "d.amatsetam@gmail.com"

RUN useradd -u 5555 -ms /bin/bash basex

ENV HOME /home/basex

RUN curl http://files.basex.org/releases/8.4.2/BaseX842.zip -o /tmp/BaseX.zip && unzip /tmp/BaseX.zip -d /opt/ && chown -R basex /opt/basex

ENV PATH /opt/basex/bin:$PATH

# Attach a volume to BaseX data
RUN ln -s /opt/basex/data/ /data
VOLUME /data

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

EXPOSE 1984 8080

USER 5555

ENTRYPOINT ["/entrypoint.sh"]

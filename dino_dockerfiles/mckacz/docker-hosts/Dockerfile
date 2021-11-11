FROM jwilder/docker-gen
MAINTAINER Maciej Kaczmarek <maciej@kaczmarek.io>

ADD docker-gen.cfg /docker-gen.cfg
ADD hosts.template /hosts.template
ADD update-hosts.sh /update-hosts.sh

RUN chmod +x /update-hosts.sh

CMD ["-config", "/docker-gen.cfg"]

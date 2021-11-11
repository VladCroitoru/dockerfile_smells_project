FROM debian:jessie
WORKDIR /tmp

RUN adduser --disabled-password --gecos '' objectivefs
RUN mkdir -p /etc/objectivefs.env
RUN apt-get update -y && apt-get install fuse wget ca-certificates unzip ntpdate psmisc -y  
RUN wget https://objectivefs.com/user/download/abxaysebd/objectivefs_5.0_amd64.deb
RUN dpkg -i objectivefs_5.0_amd64.deb

##install dumb-init
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-init_1.2.0_amd64.deb
RUN dpkg -i dumb-init_*.deb

##install consul-template
RUN wget https://releases.hashicorp.com/consul-template/0.18.0-rc2/consul-template_0.18.0-rc2_linux_amd64.zip
RUN unzip consul-template_0.18.0-rc2_linux_amd64.zip
RUN cp consul-template /bin/consul-template
RUN chmod +x /bin/consul-template

##install jq
RUN wget https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
RUN cp jq-linux64 /bin/jq
RUN chmod +x /bin/jq

WORKDIR /
ADD templates /templates
ADD entrypoint.sh /bin/entrypoint
RUN chmod +x /bin/entrypoint
ADD objectivefs.sh /bin/objectivefs
RUN chmod +x /bin/objectivefs

RUN mkdir -p /volume
RUN mkdir -p /pids
VOLUME /volume
VOLUME /var/cache/objectivefs

ENTRYPOINT ["/bin/entrypoint"]
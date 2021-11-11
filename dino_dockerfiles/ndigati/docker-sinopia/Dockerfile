FROM factual/docker-base
MAINTAINER Nicholas Digati <nicholas@factual.com>

WORKDIR /home/

RUN	curl -sL https://deb.nodesource.com/setup_5.x | bash - && \
  apt-get update && \
  apt-get --no-install-recommends -y install nodejs \
    python3-pip && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  mkdir -p /etc/service/sinopia/ /etc/my_init.d/ /home/bucket

RUN npm install js-yaml sinopia && \
  pip3 install awscli

COPY variable_check.sh /home/variable_check.sh
COPY service_start.sh /etc/my_init.d/99_service_start.sh
COPY sinopia.sh /etc/service/sinopia/run

RUN chmod +x /home/variable_check.sh /etc/my_init.d/99_service_start.sh /etc/service/sinopia/run

EXPOSE 4873

CMD [ "/sbin/my_init" ]


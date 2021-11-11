FROM factual/docker-base
MAINTAINER Nicholas Digati <nicholas@factual.com>

WORKDIR /home/

RUN curl https://deb.nodesource.com/setup_7.x | bash - && \
  apt-get --no-install-recommends -y install nodejs python3-pip python3-setuptools && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
  mkdir -p /etc/service/sinopia/ /etc/my_init.d/ /home/bucket

RUN npm install js-yaml verdaccio && \
  pip3 install --upgrade pip && \
  pip3 install awscli

COPY variable_check.sh /home/variable_check.sh
COPY service_start.sh /etc/my_init.d/99_service_start.sh
COPY sinopia.sh /etc/service/sinopia/run

RUN chmod +x /home/variable_check.sh /etc/my_init.d/99_service_start.sh /etc/service/sinopia/run

EXPOSE 4873

CMD [ "/sbin/my_init" ]


FROM pasmod/base-jdk-8-gradle

WORKDIR /tmp/project
ADD . .

# build app
RUN gradle build

# install app
RUN gradle installDist

RUN mv build/install/knife/ /opt/knife
RUN mkdir -p /etc/service/knife
RUN mv scripts/docker/runit-service/run.sh /etc/service/knife/run
RUN chmod 755 /etc/service/knife/run

WORKDIR /opt/knife

EXPOSE 4567
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

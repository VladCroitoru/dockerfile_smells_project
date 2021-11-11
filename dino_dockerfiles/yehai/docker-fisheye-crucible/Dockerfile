FROM descoped/atlassian-base
MAINTAINER Ove Ranheim <oranheim@gmail.com>

# Install Fisheye and Crucible
ENV FISHEYE_VERSION 4.5.2
ENV CRUCIBLE_VERSION $FISHEYE_VERSION

ENV FISHEYE_HOME /opt/fisheye
ENV FISHEYE_INST /var/atlassian-home

ENV UID fisheye
ENV GID atlassian
ENV LANG C.UTF-8

RUN DEBIAN_FRONTEND=noninteractive apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -q -y unzip ssh-client git \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -r --create-home --home-dir $FISHEYE_HOME --groups $GID --shell /bin/bash $UID \
    && curl -Lk http://www.atlassian.com/software/fisheye/downloads/binary/fisheye-$FISHEYE_VERSION.zip -o /root/fisheye.zip \
    && curl -Lk http://www.atlassian.com/software/crucible/downloads/binary/crucible-$CRUCIBLE_VERSION.zip -o /root/crucible.zip \
    && unzip /root/fisheye.zip -d /opt/ \
    && rm /root/fisheye.zip \
    && unzip -o /root/crucible.zip -d /opt/ \
    && rm /root/crucible.zip \
    && mv /opt/fecru-$FISHEYE_VERSION/* $FISHEYE_HOME/ \
    && rm -f "${FISHEYE_HOME}/lib/atlassian-extras-*.*.jar" 

COPY ./${FISHEYE_VERSION}/*.jar "${FISHEYE_HOME}/lib/"
# Launching Fisheye
WORKDIR $FISHEYE_HOME
VOLUME ["$FISHEYE_INST"]

COPY entrypoint.bash /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 8060
CMD ["bin/fisheyectl.sh", "run"]

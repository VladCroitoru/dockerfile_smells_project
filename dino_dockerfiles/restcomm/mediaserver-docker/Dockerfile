FROM java:7-jdk
MAINTAINER gdubina@dataart.com

RUN apt-get update && \
    apt-get install -y net-tools xmlstarlet && \
    alias xml=xmlstarlet && ln -s /usr/bin/xmlstarlet /usr/bin/xml && \
    rm -rf /var/lib/apt/lists/*

ENV work_dir /opt/restcomm-media-server

RUN wget -O /tmp/restcomm-media-server.zip https://mobicents.ci.cloudbees.com/view/MediaServer/job/RestComm-MediaServer-4.x/lastSuccessfulBuild/artifact/bootstrap/target/restcomm-media-server.zip && \
    wget -O /tmp/media-version.txt https://mobicents.ci.cloudbees.com/view/MediaServer/job/RestComm-MediaServer-4.x/lastSuccessfulBuild/artifact/media-version.txt && \
    mkdir -p $work_dir/recordings && \
    unzip /tmp/restcomm-media-server.zip -d /opt && \
    chmod +x $work_dir/bin/run.sh && \
    rm /tmp/restcomm-media-server.zip && \
    mv /tmp/media-version.txt $work_dir

COPY scripts $work_dir

WORKDIR $work_dir

CMD ./run.sh
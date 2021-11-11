FROM ubuntu
RUN apt-get update && apt-get install -y openssl wget python-software-properties software-properties-common apt-transport-https ca-certificates curl
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
RUN add-apt-repository ppa:gluster/glusterfs-3.10
RUN apt-get update && apt-get install -y glusterfs-client glusterfs-common docker-ce
ADD run.sh .
ADD add-volume.sh /usr/bin
CMD [ "bash","run.sh" ]

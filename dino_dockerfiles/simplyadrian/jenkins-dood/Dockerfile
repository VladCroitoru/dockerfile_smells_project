# vim: ft=dockerfile
###############################################################################
# Jenkins with DooD (Docker outside of Docker)
# http://github.com/axltxl/docker-jenkins-dood
# Author: Alejandro Ricoveri <me@axltxl.xyz>
# Based on:
# * http://container-solutions.com/2015/03/running-docker-in-jenkins-in-docker
# * http://jpetazzo.github.io/2015/09/03/do-not-use-docker-in-docker-for-ci
###############################################################################

FROM jenkins/jenkins:2.175
MAINTAINER the internet

ENV PRODUCT test
ENV ROOT_BUCKET backups
ENV REGION us-east-1
ENV docker_version 18.06.1

# Install necessary packages
USER root
ADD ./git-lfs_1.4.4_amd64.deb /git-lfs_1.4.4_amd64.deb
RUN apt-get update &&\
    apt-get upgrade -y -o DPkg::Options::=--force-confold &&\
    apt-get install -qq -y --no-install-recommends --no-install-suggests \
                    apt-transport-https \
                    ca-certificates \
                    gnupg2 \
                    software-properties-common \
                    git \
                    zip \
                    sudo \
		    packer \
		    make &&\
    dpkg -i /git-lfs_1.4.4_amd64.deb &&\
    apt-get install -f &&\
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - &&\
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable" &&\
    apt-get update &&\
    apt-get install -qq -y --no-install-recommends --no-install-suggests \
		    docker-ce=${docker_version}~ce~3-0~debian \
		    python-pip \
		    python-virtualenv \
		    ansible &&\
    curl -fsSL -o terraform.zip https://releases.hashicorp.com/terraform/0.11.11/terraform_0.11.11_linux_amd64.zip &&\
    unzip terraform.zip -d /usr/local/bin/ &&\
    chmod +x /usr/local/bin/terraform &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

# install awscli
RUN pip install awscli boto3

# restore job
ADD restore.sh /restore.sh

# add executable bits to entrypoint script
RUN chmod +x /restore.sh

# add some default jobs that we want to ship with all jenkins servers
ADD jobs /usr/share/jenkins/ref/jobs

# fixup the backup job to be specific to the product we start with
ADD fixup_backup.sh /fixup_backup.sh

# add executable bits to entrypoint script
RUN chmod +x /fixup_backup.sh

#add entrypoint script into the container
ADD uidgid_volume_entry.sh /tmp/uidgid_volume_entry.sh
RUN chmod +x /tmp/uidgid_volume_entry.sh

USER jenkins
# add some plugins at boot time
COPY plugins.txt /usr/share/jenkins/plugins.txt
RUN cat /usr/share/jenkins/plugins.txt | /usr/local/bin/install-plugins.sh

# add github keys to known hosts
RUN mkdir "$JENKINS_HOME"/.ssh && ssh-keyscan -t rsa github.com >> "$JENKINS_HOME"/.ssh/known_hosts

USER root
ENTRYPOINT ["/tmp/uidgid_volume_entry.sh"]

#This drone-auth-ecr image contains AWS credentials and lives on a private docker registry
#It is pulled by drone to auth to ECR and pull an ECR image as a step in the pipeline
FROM debian:jessie

# AWS CLI needs the PYTHONIOENCODING environment varialbe to handle UTF-8 correctly:
ENV PYTHONIOENCODING=UTF-8
ENV PATH=/root/.local/bin:$PATH

## Copy AWS config, credentials should be automatically pulled from IAM role associated with drone instance
COPY config/config /root/.aws/config

#install the aws prereqs
RUN apt-get update \
    && apt-get install -y \
    python \
    python-pip 

#install aws cli
RUN pip install awscli --upgrade \
    && echo 'export PATH=/root/.local/bin:$PATH' >> /root/.bash_profile 

#install packages for docker
RUN set -x \
    && export APT_LISTCHANGES_FRONTEND=none \
    && apt-get -q -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install apt-transport-https \
    && apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
    && echo "deb https://apt.dockerproject.org/repo debian-jessie main" > /etc/apt/sources.list.d/docker.list \
    && apt-get update \
    && apt-get -q -y -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install docker-engine \
    && apt-get clean \
    && rm -Rf /var/lib/apt/lists/* 2>/dev/null \
    && service docker start 


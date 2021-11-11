FROM gitlab/gitlab-runner:latest

# Add docker bits (from https://github.com/docker-library/docker/blob/7ef1746a46a29d89bac9aca8d0788bd629eb00e6/1.10/Dockerfile)

ENV DOCKER_BUCKET get.docker.com
ENV DOCKER_VERSION 1.10.3
ENV DOCKER_SHA256 d0df512afa109006a450f41873634951e19ddabf8c7bd419caeb5a526032d86d

RUN curl -fSL "https://${DOCKER_BUCKET}/builds/Linux/x86_64/docker-$DOCKER_VERSION" -o /usr/local/bin/docker \
	&& echo "${DOCKER_SHA256}  /usr/local/bin/docker" | sha256sum -c - \
	&& chmod +x /usr/local/bin/docker

# Prepare the image.  Ansible 2.5 synchronize doesn't work with docker in our config
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update \
    && apt-get install -y -qq --no-install-recommends wget unzip python python-openssl python-setuptools make python-pip \
    && pip install ansible==2.4.3 && pip install --upgrade cryptography>=1.5 \
    && apt-get install -y -qq --no-install-recommends python3 \
    && apt-get clean
    
RUN curl -L https://releases.hashicorp.com/packer/1.2.3/packer_1.2.3_linux_amd64.zip > packer.zip \
   && unzip packer.zip \
   && mv packer /usr/local/bin \
   && rm packer.zip

# Custom changes
COPY entry_point.sh /
CMD ["run", "--user=gitlab-runner", "--working-directory=/home/gitlab-runner"]
ENTRYPOINT [ "/entry_point.sh" ]
# Leave the rest from gitlab-runner

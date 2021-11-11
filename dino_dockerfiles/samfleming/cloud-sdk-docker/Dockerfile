FROM google/cloud-sdk

RUN apt-get update && apt-get install -y -qq --no-install-recommends curl git unzip zlib1g-dev \
	&& curl -L -o /tmp/docker.tgz https://get.docker.com/builds/Linux/x86_64/docker-1.12.3.tgz \
    && tar -xz -C /tmp -f /tmp/docker.tgz \
	&& mv /tmp/docker/docker* /usr/bin/ \
	&& curl -L "https://github.com/docker/compose/releases/download/1.9.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/bin/docker-compose \
	&& chmod +x  /usr/bin/docker-compose \
	&& mkdir -p /var/www/html

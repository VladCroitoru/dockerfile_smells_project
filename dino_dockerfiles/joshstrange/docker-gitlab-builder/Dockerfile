FROM ubuntu:16.04

# Run the initial install step to get some stuff going.
RUN apt-get update \
	&& apt-get install -y php-cli php-mcrypt php-curl nodejs npm apt-transport-https ca-certificates \
	&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \
	&& php composer-setup.php -- --install-dir=/bin --filename=composer \
	&& php -r "unlink('composer-setup.php');" \
	&& ln -s /usr/bin/nodejs /usr/bin/node \
	&& npm install -g gulp bower \
	&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D \
	&& echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" > /etc/apt/sources.list.d/docker.list \
	&& apt-get update \
	&& apt-get install -y docker-engine

# Install some other PHP extensions.
RUN apt-get install -y php-mbstring php-dom php-zip

# Install the AWS CLI
RUN apt-get install -y unzip curl \
	&& curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip" \
	&& unzip awscli-bundle.zip \
	&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws

# Set the Docker host, because we're assuming we're using docker in docker.
ENV DOCKER_HOST "tcp://docker:2375"

# Expose Docker socket for Docker-in-Docker
VOLUME /var/run/docker.sock

FROM ubuntu:trusty
MAINTAINER romeOz <serggalka@gmail.com>

RUN	\
	# Update packages list, upgrade installed packages
	apt-get -y update && \
	apt-get -y upgrade && \
	apt-get install -y build-essential software-properties-common python-software-properties curl git-core libxml2-dev libxslt1-dev libfreetype6-dev python-pip python-apt python-dev && \
	pip install https://pypi.python.org/packages/source/a/ansible/ansible-1.9.1.tar.gz

# Add playbooks to the Docker image
ADD ./ /var/www/rock-basic/
WORKDIR /var/www/rock-basic/

# Install ansible-playbook
RUN ansible-playbook -v provisioning/docker.yml -i 'docker,' -c local

# Install supervisor
RUN apt-get install -y supervisor && mkdir -p /var/log/supervisory

ADD ./provisioning/supervisord.conf /etc/supervisor/conf.d/

EXPOSE 22 80

CMD ["/usr/bin/supervisord"]
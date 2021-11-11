FROM ubuntu:16.04
MAINTAINER Petr Besir Horacek <petr.horacek@legerete.cz>

RUN apt-get update && \
	apt-get install -y \
	software-properties-common \
	git \
	make \
	sudo \
	curl \
	docker.io \
	python-pkg-resources

RUN git config --global user.email "git-auto-deploy@example.com"
RUN git config --global user.name "Git Auto-Deploy"

RUN add-apt-repository ppa:olipo186/git-auto-deploy

RUN apt-get update

RUN apt-get install -y git-auto-deploy

RUN mkdir /var/ssh-deploy-keys


#Start
ADD start.sh ./start.sh
RUN chmod +x ./start.sh

#Set port
EXPOSE 8080

VOLUME ["/var/ssh-deploy-keys"]

#Start it
ENTRYPOINT ["/start.sh"]
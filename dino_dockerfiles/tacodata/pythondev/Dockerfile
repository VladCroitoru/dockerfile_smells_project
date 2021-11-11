FROM ubuntu:14.04

MAINTAINER Greg Fausak <greg@tacodata.com>

# the update is needed to get the sources.list set right, otherwise we
# won't find anything to get.
RUN apt-get update && apt-get -y install \
	build-essential \
	git \
	python-dev \
	python-pip

# when you run grip, do it in the directory with the README.md file
# in it.  simply type 'grip', then browse to port 5000 to see what the README.md
# file will look like when browsed after being checked in on github.
RUN pip install grip
EXPOSE 5000

# when using root/bash in this image as root i like to have
# vi based history from the command line
RUN /bin/echo 'set editing-mode vi' > /root/.inputrc

# set up a gfausak user
RUN useradd gfausak -m -g staff -s /bin/bash &&\
	usermod -a -G sudo gfausak &&\
	/bin/echo 'set editing-mode vi' > /home/gfausak/.inputrc &&\
	mkdir /home/gfausak/.ssh &&\
	mkdir /home/gfausak/git &&\
	ssh-keygen -t dsa -q -f /home/gfausak/.ssh/id_dsa -P '' &&\
	chown -R gfausak:staff /home/gfausak &&\
	chmod 700 /home/gfausak/.ssh

# git configuration for me, obviously, change for someone else :-)
RUN git config --global user.name "Greg Fausak" && \
	git config --global user.email greg@tacodata.com &&\
	git config --global core.editor vi &&\
	git config --global push.default simple

#WORKDIR /home/gfausak
#USER gfausak

CMD [ '/bin/bash' ]

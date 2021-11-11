## Setup Anypoint Studio in Docker

FROM ubuntu:14.04
MAINTAINER Brandon Grantham <brandon.grantham@mulesoft.com>

LABEL Description="MuleSoft Anypoint Studio"

## Set version for build
ARG STUDIO_VERSION=6.2.3-201703101604
#ENV STUDIO_VERSION -201703101604}

## Update Ubuntu in preparation for installing Anypoint Studio
RUN 	sed 's/main$/main universe/' -i /etc/apt/sources.list && \
    	apt-get update && apt-get install -y software-properties-common && \
    	add-apt-repository ppa:webupd8team/java -y && \
    	apt-get update && \
    	echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    	apt-get install -y oracle-java8-installer libxext-dev libxrender-dev libxtst-dev && \
    	apt-get clean && \
    	rm -rf /var/lib/apt/lists/* && \
    	rm -rf /tmp/*
		
# Setup the additional libraries
RUN 	apt-get update && apt-get install -y libgtk2.0-0 libcanberra-gtk-module \ 
		&& apt-get install maven -y

## Retrieve studio for Linux from S3 and uncompress
RUN 	wget https://mule-studio.s3.amazonaws.com/6.2.3-U3/AnypointStudio-for-linux-64bit-$STUDIO_VERSION.tar.gz -O /tmp/studio.tar.gz -q \ 
        && echo 'Installing Studio' \
	&& tar -zxf /tmp/studio.tar.gz -C /opt && \ 
	rm /tmp/studio.tar.gz
		
## Copy over the run studio file
ADD	run /usr/local/bin/studio

## Create the mule user and assign to the appropriate role
RUN    chmod +x /usr/local/bin/studio && \
       mkdir -p /home/mule && \
       echo "mule:x:1000:1000:mule,,,:/home/mule:/bin/bash" >> /etc/passwd && \
       echo "mule:x:1000:" >> /etc/group && \
       echo "mule ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/mule && \
       chmod 0440 /etc/sudoers.d/mule && \
       chown mule:mule -R /home/mule && \
       chown root:root /usr/bin/sudo && chmod 4755 /usr/bin/sudo

## Change to the mule user and create home
USER   mule
ENV    HOME /home/mule
WORKDIR /home/mule
ADD docker-entrypoint.sh /home/mule/
# RUN sudo chmod 775 /home/mule/docker-entrypoint.sh && sudo chown mule.mule /home/mule/docker-entrypoint.sh
ENTRYPOINT ["/home/mule/docker-entrypoint.sh"]
## Run the start command
CMD    /usr/local/bin/studio

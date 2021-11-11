# -----------------------------------------------------------------------					
# UBC IT - CTLC - Jupyter Hub Course API for Instructors
# Created By: Balaji Srinivasarao, Rahim Khoja, & Pan Luo
# docker build -t IMAGE_ID .
# ======================================================================							
# Container Choice
FROM debian:buster-slim																					
ENV LANG C.UTF-8																					
# TimeZone Settings
ENV TZ 'America/Vancouver'
RUN echo $TZ > /etc/timezone && \
apt-get update && apt-get install -y tzdata && \
rm /etc/localtime && \
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
dpkg-reconfigure -f noninteractive tzdata && \
apt-get clean
# Package Installation Command
RUN APT_INSTALL="apt-get install -y " && \																													
	apt-get update && \																				
# ======================================================================							
# Apt Packages																								
# ----------------------------------------------------------------------							
	SYSTEM_PACKAGES=noninteractive $APT_INSTALL \	
	        software-properties-common \
		build-essential \																			
		apt-utils \																					
		ca-certificates \																			
		wget \																						
		git \	
		curl \
		rsync \
		vim \
		python3 \																																					
		python3-pip \
		cron \
		zip \
		unzip \
		&& \																																										
# ======================================================================							
# Container Cleanup & Finalization																				
# ----------------------------------------------------------------------							
	ldconfig && \																					
	apt-get clean && \																				
	apt-get autoremove && \																			
	rm -rf /var/lib/apt/lists/* /tmp/* ~/*	
# ======================================================================							
# Application Specific Commands				
#
# ----------------------------------------------------------------------
							
EXPOSE 5000											
COPY usr/share/jupyter-canvas-api/api-server.py /usr/share/jupyter-canvas-api/api-server.py
COPY usr/share/jupyter-canvas-api/requirements.txt /usr/share/jupyter-canvas-api/requirements.txt
COPY usr/local/bin/hourly-rsync.sh /etc/cron.hourly/hourly-rsync
RUN mkdir /mnt/efs
RUN chmod +x /etc/cron.hourly/hourly-rsync
WORKDIR /usr/share/jupyter-canvas-api/
RUN pip3 install -r /usr/share/jupyter-canvas-api/requirements.txt
#CMD [ "python3","-u","/usr/share/jupyter-canvas-api/api-server.py"]
CMD /etc/init.d/cron start && python3 -u /usr/share/jupyter-canvas-api/api-server.py

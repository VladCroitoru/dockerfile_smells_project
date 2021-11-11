FROM mkenney/npm:node-7-debian

MAINTAINER Tim Rasim "rasim@imis.uni-luebeck.de"

# Prepare for mongo
RUN sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.4 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

# Update
RUN apt-get update

# Install software 
RUN apt-get install -y git mongodb-org

# Make ssh dir
RUN mkdir /root/.ssh/
RUN chown -R root:root /root/.ssh

# Create known_hosts
RUN touch /root/.ssh/known_hosts

# Remove host checking
RUN echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >> /root/.ssh/config

# Clone the conf files into the docker container
RUN git clone https://github.com/neogucky/energy-grid-api /home/energy-grid-api

# Install deployd-cli globaly 
RUN npm install deployd-cli -g

# Install local deployd module
WORKDIR /home/energy-grid-api/
RUN npm install deployd

# Prepare mongodb folder
RUN mkdir -p /data/db

# WORKARROUND: create module to copy node_module folder to our project
RUN dpd create dummy
RUN cp dummy/node_modules/ netz-daten-strom/node_modules -R

# Start deployd
EXPOSE 2403
WORKDIR /home/energy-grid-api/netz-daten-strom/
CMD ["sh", "/home/energy-grid-api/netz-daten-strom/updateAndStart.sh"]

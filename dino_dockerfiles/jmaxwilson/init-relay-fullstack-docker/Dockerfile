FROM node:latest
WORKDIR /usr/src/app 

# Install yeoman and the relay-fullstack generator
RUN npm install -g yo generator-relay-fullstack

# Add a yeoman user because yeoman doesn't like to run under root
RUN adduser --disabled-password --gecos "" --shell /bin/bash yeoman; echo "yeoman ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
ENV HOME /home/yeoman

# Create a Dockerfile file in /home/yeoman that can be copied into new projects
RUN echo "FROM node:latest\n\nWORKDIR /usr/src/app\n\nEXPOSE 3000 8000\nCMD [ \"yarn\", \"start\" ]" > /home/yeoman/Dockerfile
RUN chown yeoman:yeoman /home/yeoman/Dockerfile

# Create a docker-compose.yml file in /home/yeoman that can be copied into new projects to run them
RUN echo "version: '2'\nservices:\n\n  relayapp:\n    build: .\n    volumes:\n      - \$PWD:/usr/src/app\n    ports:\n      - \"3000:3000\"\n      - \"8000:8000\"" > /home/yeoman/docker-compose.yml
RUN chown yeoman:yeoman /home/yeoman/docker-compose.yml

# Create a shell script that will copy the Dockerfile and docker-compose.yml into the new project and run yeoman to generate the relay-fullstack code
RUN echo "#!/bin/bash\n\ncp ~/Dockerfile /usr/src/app\ncp ~/docker-compose.yml /usr/src/app\nyo relay-fullstack\n" > /home/yeoman/init-relay-fullstack.sh
RUN chown yeoman:yeoman /home/yeoman/init-relay-fullstack.sh
RUN chmod 700 /home/yeoman/init-relay-fullstack.sh

# Make sure that we run as the yeoman user
USER yeoman

# when we run the container execute the shell script we created
CMD ["/home/yeoman/init-relay-fullstack.sh"]

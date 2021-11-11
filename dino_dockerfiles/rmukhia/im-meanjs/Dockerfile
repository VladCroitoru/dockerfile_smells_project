FROM node:0.12.9-wheezy

# Update and install essential packages
#RUN apt-get update && apt-get install -y apt-utils && apt-get install -y curl build-essential git dos2unix ruby 

# Node.js and mongodb requirements
#RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -a 
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com --recv EA312927 && echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list && apt-get update && apt-get install -y ruby mongodb-org-server && gem install sass && useradd -ms /bin/bash dev && mkdir -p /data/db && chown dev:dev /data/db

# Update again, and install Node.js and mongodb and sass gem. Create dev user. Set up mongodb log permissions and parameters.
#RUN apt-get update && apt-get install -y ruby mongodb-org-server && gem install sass && useradd -ms /bin/bash dev && mkdir -p /data/db && chown dev:dev /data/db

# Set up dev
USER dev
WORKDIR /home/dev
ENV PATH=~/.npm-global/bin:$PATH
# Create directories, set npm configurations, install bower, grunt, yo and generator-meanjs. 
RUN mkdir ~/.npm-global && mkdir ~/logs && npm config set prefix '~/.npm-global' && npm install -g bower grunt-cli yo@1.3.3  generator-meanjs@0.1.12 &&  mkdir ~/config
COPY configurations/mongod.conf /home/dev/config/mongod.conf

# Expose MEANJS http port
EXPOSE 3000 3000
# Expose livereload.js port
EXPOSE 35729 35729

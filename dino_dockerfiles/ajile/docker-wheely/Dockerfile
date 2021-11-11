# Docker version 1.4.x, build d84a070
#
#   To build: sudo docker build --force-rm=true -t visualjeff/ember-cli:0.2.X .
#   To tag: sudo docker tag CONTAINERID visualjeff/ember-cli:latest
#   To run: sudo docker run -t -i -p 4200:4200 -p 35729:35729 visualjeff/ember-cli:latest /bin/bash
FROM    debian:latest

# Update and install basics
RUN apt-get update && apt-get install -y git curl nano vim tmux tar bzip2 gawk
RUN apt-get install -y build-essential checkinstall
RUN apt-get install -y expect

# Install Ruby
RUN apt-get install -y rubygems build-essential
RUN gem install sass
RUN sass -v

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs

# Install NVM
RUN git clone https://github.com/creationix/nvm.git /.nvm
RUN echo ". /.nvm/nvm.sh" >> /etc/bash.bashrc
RUN /bin/bash -c '. /.nvm/nvm.sh && \
    nvm install v3.0.0 && \
    nvm use v3.0.0 && \
    nvm alias default v3.0.0'

#Install ember-cli
RUN npm install -g ember-cli@1.13.8 phantomjs bower grunt grunt-cli broccoli-cli

# ADD setupVim.sh /root/setupVim.sh
# RUN chmod +x /root/setupVim.sh

#Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

#Expose ports
EXPOSE 4200 4300 35729

# Define default command.
WORKDIR /root
CMD ["bash"]

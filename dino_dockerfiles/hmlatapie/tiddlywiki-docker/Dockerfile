FROM node:latest

RUN apt-get update

# Install npm
#RUN apt-get install -y software-properties-common curl
#RUN curl -sL https://deb.nodesource.com/setup_7.9.0 | bash -
#RUN apt-get install -y nodejs

# Install tiddlywiki
RUN npm install -g tiddlywiki@5.1.15

# Setup wiki volume
VOLUME /var/lib/tiddlywiki
WORKDIR /var/lib/tiddlywiki

# Add init-and-run script
ADD init-and-run-wiki /usr/local/bin/init-and-run-wiki

# Meta
CMD ["/usr/local/bin/init-and-run-wiki"]
EXPOSE 8080

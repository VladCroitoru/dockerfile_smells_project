FROM jenkins:latest

MAINTAINER Mirko Haaser <kontakt@mirko-haaser.de>

# Install Heroku CLI toolbelt
USER root
RUN cd /tmp
RUN wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz
RUN ls -la
RUN tar -xvzf heroku-linux-amd64.tar.gz 
RUN mv heroku /usr/local/lib/
RUN ln -s /usr/local/lib/heroku/bin/heroku /usr/local/bin/heroku
RUN rm heroku-linux-amd64.tar.gz

# Switch to jenkins user
USER jenkins
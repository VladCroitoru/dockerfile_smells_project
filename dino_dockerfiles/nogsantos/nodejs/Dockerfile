FROM nogsantos/ubuntu
# MAINTAINER Fabricio Nogueira nogsantos@gmail.com
# build-essential to compile and install native addons from npm.
RUN wget -qO- https://deb.nodesource.com/setup_7.x | bash - \    
    && DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential nodejs \
    && apt-get install -y sendmail \
    && rm -rf /var/lib/apt/lists/*

# Config sendmail
WORKDIR /etc/mail
COPY ./sendmail.mc /etc/mail/sendmail.mc
RUN m4 sendmail.mc > sendmail.cf && \
 echo "Connect:172 RELAY" >> access && \
 echo "Connect:10 RELAY" >> access && \
 make    

EXPOSE 25
CMD /usr/lib/sendmail -bD -X /proc/self/fd/1

# Defining the APP Work dir 
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Set some envs
ENV NPM_CONFIG_LOGLEVEL=info \
    NODE_VERSION=7.3.0
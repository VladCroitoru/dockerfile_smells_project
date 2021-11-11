FROM xdevelsistemas/debian-env:latest


#install awscli
RUN apt-get update && \
    apt-get install -y python-pip groff && \
    pip install awscli


#install node
RUN apt-get update && \
    apt-get install -y curl && \
    curl -sL https://deb.nodesource.com/setup | bash - && \
    apt-get install -y nodejs

# Setup
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF

# Add the repository
RUN echo "deb http://repos.mesosphere.io/debian wheezy main" | \
   tee /etc/apt/sources.list.d/mesosphere.list \
   &&  apt-get -y update




#install phantomjs
RUN node -v \
    && npm install -g phantomjs \
       && npm install -g casperjs

#ENV AWS_ACCESS_KEY_ID
#ENV AWS_SECRET_ACCESS_KEY
#ENV AWS_DEFAULT_REGION
ADD worker.py .

CMD ["/usr/bin/python","worker.py"]

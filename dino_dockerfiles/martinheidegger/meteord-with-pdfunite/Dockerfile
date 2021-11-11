FROM meteorhacks/meteord:base
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10
RUN echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list
RUN apt-get update
RUN apt-get install -y poppler-utils imagemagick
RUN apt-get install -y mongodb-org-tools
RUN apt-get install --reinstall tzdata
RUN echo Asia/Tokyo > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata

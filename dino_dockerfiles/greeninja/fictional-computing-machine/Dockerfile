FROM ubuntu:latest
RUN apt update && \
    apt install -y mysql-client ruby ruby-dev gcc make automake libxml2 libmysqlclient-dev libsqlite3-dev openjdk-8-jdk ruby-execjs patch git && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /home
# Add a new layer to make builds quicker
ADD Gemfile /home/Gemfile
RUN gem install bundler && \
    /usr/local/bin/bundle install
ADD . /home
RUN chown 1000190000:1000190000 /home -R

EXPOSE 8080

ENTRYPOINT ["/home/docker-entrypoint.sh"]

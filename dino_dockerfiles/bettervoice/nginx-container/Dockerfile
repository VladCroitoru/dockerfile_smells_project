# Ubuntu BetterVoice Client.

FROM ubuntu:14.04
MAINTAINER Thomas Quintana <thomas@bettervoice.com>

# Initialize the package manager.
RUN apt-get update -y && apt-get install -y libffi-dev libpcre3-dev libssl-dev nginx python python-dev python-pip wget
RUN pip install Jinja2

# Build from source.
RUN wget http://nginx.org/download/nginx-1.7.10.tar.gz -O /usr/src/nginx-1.7.10.tar.gz
WORKDIR /usr/src
RUN tar -xzvf nginx-1.7.10.tar.gz
WORKDIR nginx-1.7.10
RUN ./configure
RUN make && make install

# Add the nginx bootstrap script.
ADD bin/start-nginx /usr/bin/start-nginx
RUN chmod +x /usr/bin/start-nginx
ADD config/default.template /usr/share/nginx/default.template

# Open the container up to the world.
EXPOSE 80/tcp
EXPOSE 443/tcp

# Start the container.
CMD start-nginx

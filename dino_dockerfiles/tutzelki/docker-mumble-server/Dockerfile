FROM ubuntu:14.04

MAINTAINER Sebastian Schroeder <tutzelki@web.de>

RUN apt-get update
RUN apt-get install -y mumble-server && apt-get clean -y

# Add the start script
ADD start.sh /tmp/start.sh
RUN chmod 700 /tmp/start.sh

VOLUME ["/data"]

EXPOSE 64738

CMD ["/tmp/start.sh"]

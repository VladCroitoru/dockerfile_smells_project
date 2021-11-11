FROM nginx
MAINTAINER Octoblu, Inc. <docker@octoblu.com>

# This weirdness is to fix the build on hub.docker.com because
# COPY run.sh /run.sh fails for whatever reason
COPY . /etc/nginx/
RUN mv /etc/nginx/run.sh /run.sh

CMD ["./run.sh"]

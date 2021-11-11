# Instructions from the blog post at http://blog.bittorrent.com/2013/10/22/sync-hacks-deploy-bittorrent-sync-with-docker/
FROM ubuntu:12.10
MAINTAINER Solomon Hykes <solomon@docker.com>
RUN apt-get update && apt-get install -y curl
RUN curl -o /usr/bin/btsync.tar.gz http://download-lb.utorrent.com/endpoint/btsync/os/linux-x64/track/stable
RUN cd /usr/bin && tar -xzvf btsync.tar.gz && rm btsync.tar.gz
RUN mkdir -p /btsync/.sync
EXPOSE 8888
EXPOSE 55555
ENTRYPOINT ["btsync"]
# Default arguments:
CMD ["--config", "/btsync/btsync.conf", "--nodaemon"]
ADD btsync.conf /btsync/btsync.conf

FROM haproxy:latest
MAINTAINER  Neil Watson <neil@watson-wilson.ca>
COPY haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg
EXPOSE 80

ENTRYPOINT [ "haproxy", "-db", "-V", "-f", "/usr/local/etc/haproxy/haproxy.cfg" ]

# Howto:

# Build with  docker build -t my_haproxy .

# View with   docker images

# Run with, where host port 80 is mapped to conatiner port 80, exposed by
# Docker file
# docker run -i --cap-drop=all --cap-add=chown --cap-add=net_bind_service --cap-add=setgid --detatch --restart=unless-stopped ---publish 80:80 --name my_haproxy -t my_haproxy

# Stop with
# docker stop $(docker ps |awk '$2 ~ /^my_haproxy/ { print $1 }')

# start with
# docker start $(docker ps |awk '$2 ~ /^my_haproxy/ { print $1 }')

# Delete container
# docker rm $(docker ps -a |awk '$2 ~ /^my_haproxy/ { print $1 }')

# Delete build image with 
# docker rmi $(docker images |awk '$1 ~ /^my_haproxy$/ { print $3 }')


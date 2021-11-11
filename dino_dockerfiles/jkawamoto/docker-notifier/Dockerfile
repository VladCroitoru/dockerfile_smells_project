FROM ubuntu:latest
MAINTAINER Junpei Kawamoto <kawamoto.junpei@gmail.com>

# Install packages
RUN apt-get update && apt-get install -y python-pip
RUN pip install --upgrade requests

# Copy scripts
ADD bin /root/

# Set the entrypoint
ENTRYPOINT ["/root/notifier.py"]
CMD [""]


# Container image that runs your code
FROM debian

# Copies your code file from your action repository to the filesystem path `/` of the container
COPY filters.sh /filters.sh
RUN apt-get update && apt-get install -y wget
RUN apt-get update && apt-get install -y python3 && apt-get install -y git python3-pip
RUN wget -O gh https://github.com/cli/cli/releases/download/v2.2.0/gh_2.2.0_linux_amd64.deb
RUN dpkg -i gh
# Code file to execute when the docker container starts up (`entrypoint.sh`)
RUN chmod 777 /filters.sh
ENTRYPOINT ["/bin/bash","/filters.sh"]

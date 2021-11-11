# Container image
FROM christophkirsch/texlive:latest

# Copy entrypoint.sh to docker container
COPY entrypoint.sh /entrypoint.sh

# Code file to execute when the docker container starts up
ENTRYPOINT ["/entrypoint.sh"]
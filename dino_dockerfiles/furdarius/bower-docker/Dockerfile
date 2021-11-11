# Bower Docker Container
# Base Dockerfile: furdarius/npm-docker
FROM furdarius/npm-docker

MAINTAINER furdarius <getlag@yandex.com>

# Install bower:
RUN npm install --global bower && \
	echo '{ "allow_root": true }' > /root/.bowerrc 

# Set up the application directory
VOLUME ["/app"]
WORKDIR /app

# Define default command.
ENTRYPOINT ["bower"]
CMD ["install"]
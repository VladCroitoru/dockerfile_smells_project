FROM node:latest
MAINTAINER sid "asidhu1@gmail.com"

# Installing graphicsmagick
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
			graphicsmagick \
		&& rm -rf /var/lib/apt/lists/*

CMD ["gm", "-version"]

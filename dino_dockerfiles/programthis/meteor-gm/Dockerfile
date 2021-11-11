FROM abernix/meteord:node-12-base

RUN apt-get update && apt-get install -y \
	graphicsmagick \
	graphicsmagick-imagemagick-compat \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*
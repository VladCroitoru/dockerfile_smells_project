# You should always specify a full version here to ensure all of your developers
# are running the same version of Node.
FROM node:7.8.0

# The base node image sets a very verbose log level.
ENV NPM_CONFIG_LOGLEVEL warn

# Copy all local files into the image.
RUN  git clone https://github.com/TampereTC/tre-smartcity-frontEnd && \
	 cd tre-smartcity-frontEnd

WORKDIR tre-smartcity-frontEnd
RUN npm install
VOLUME ["tre-smartcity-frontEnd"]
EXPOSE 3000
CMD [ "npm", "start" ]


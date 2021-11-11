FROM iadvize/nodejs:4
MAINTAINER Francois-Guillaume Ribreau <fg@iadvize.com>

ENV API_TOKEN="circle-ci token"
ENV PROJECTS_FILTER_USERNAME="fgribreau"

# Cache NPM install of package.json has not been changed
# cf http://www.clock.co.uk/blog/a-guide-on-how-to-cache-npm-install-with-docker
ADD package.json /app/package.json
RUN cd /app && npm install --production --unsafe-perm

COPY . /app

# Sets the working directory for any further RUN, CMD, ENTRYPOINT, COPY and ADD commands
WORKDIR /app

# Install app dependencies
RUN npm install

EXPOSE 8080

VOLUME ["/app"]

CMD npm start

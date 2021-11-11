FROM node
MAINTAINER  Attila Szeremi <attila+webdev@szeremi.com>
RUN mkdir /src
WORKDIR /src
RUN cd /src
# Copy just the package.json file file as a cache step.
COPY package.json /src/package.json
COPY package-lock.json /src/package-lock.json
# Disable progress so npm would install faster.
# Avoid bad color output by redirecting stderr to stdout
RUN npm set progress=false && npm install 2>&1

COPY . .
EXPOSE  8080
CMD ["bin/run_production.sh"]

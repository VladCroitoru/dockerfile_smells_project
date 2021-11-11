FROM node:0.10.41

RUN apt-get update -qq && apt-get install -y build-essential
RUN apt-get install -y texlive

WORKDIR /home/FAR

# Install Mean.JS Prerequisites
RUN npm install -g grunt-cli
RUN npm install -g bower

# Install Mean.JS packages
ADD package.json /home/FAR/package.json
RUN npm install

# Manually trigger bower. Why doesnt this work via npm install?
ADD .bowerrc /home/FAR/.bowerrc
ADD bower.json /home/FAR/bower.json
RUN bower install --config.interactive=false --allow-root

# Make everything available for start
ADD . /home/FAR

# currently only works for development
ENV NODE_ENV development

# Port 3000 for server
# Port 35729 for livereload
EXPOSE 3000 35729
CMD ["grunt"]

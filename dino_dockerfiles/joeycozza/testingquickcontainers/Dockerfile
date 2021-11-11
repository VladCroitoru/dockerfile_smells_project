FROM node:6

# add the package json first to a tmp directory and build, copy over so that we dont rebuild every time
ADD package.json /tmp/package.json
RUN cd /tmp && npm install
RUN mkdir -p /runner && cp -a /tmp/node_modules /runner

# ADD cli-runner and install node deps
ADD . /runner

CMD ["bash"]

# Reset working dir for running project commands
WORKDIR /runner

#timeout is a fallback in case an error with node prevents it from exiting properly
#ENTRYPOINT ["timeout", "60", "node"]
FROM library/iojs:3.0.0-slim

# Bundle app source
COPY ./src/ /src
# Install app dependencies
RUN cd /src; npm install

EXPOSE  8080
CMD ["iojs", "/src/index.js"]

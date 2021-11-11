# Docker image for citeproc-node app
# Usage: $ docker run -d -p 8085:8085 -t {this image}

FROM node:14.11.0-stretch-slim
MAINTAINER LibreCat community <librecat-dev@lists.uni-bielefeld.de>

# Install prerequisites (for installation only)
RUN apt update -y\
    && apt install -y --no-install-recommends git ca-certificates python \
    && apt -y autoremove \
    && apt -y autoclean

# Add source
RUN git clone --recurse-submodules https://github.com/zotero/citeproc-js-server.git
WORKDIR citeproc-js-server
RUN npm install

# Append nodejs binaries TO PATH
ENV PATH node_modules/.bin:$PATH

# XML to JSON for optimal performance
RUN ./xmltojson.py ./csl ./csl-json \
  && ./xmltojson.py ./csl-locales ./csl-locales-json

# Override configuration
ADD citeServerConf.json config/default.json

# Expose port
EXPOSE 8085

# run app
CMD ["npm", "start"]

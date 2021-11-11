FROM buildpack-deps:jessie-scm
ENV DOCKER_FILE_VERSION 0.0.3

WORKDIR /root/

# cross compile toolchain
# change DOCKER_FILE_VERSION to update this file
RUN curl -s https://tessel-builds.s3.amazonaws.com/firmware/toolchain-mipsel.tar.gz | tar -xz

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get autoremove -y \
  && apt-get clean -y

# Install NVM
RUN ["/bin/bash", "-c", "curl -s -o - https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash"]

# Install node 6.5.0
RUN ["/bin/bash", "-c", ". /root/.nvm/nvm.sh \
  && nvm install 6.5.0 \
  && npm install -g npm \
  && npm install -g pre-gypify node-pre-gyp node-gyp \
  && node-gyp install 6.5.0 \
  "]

COPY compile.sh upload-files.js /root/
ENTRYPOINT ["/root/compile.sh"]
CMD ["--help"]

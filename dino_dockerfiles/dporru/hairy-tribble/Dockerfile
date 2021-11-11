FROM dporru/tribble-base
MAINTAINER Daan Porru <daan@porru.nl>

# Run the rest of the statements as user ph.
USER ph

# Add cabal binaries to the PATH
ENV PATH /home/ph/.cabal/bin:$PATH
ENV LANG C.UTF-8

# Expose port 8000 and set workdir for CMD command.
EXPOSE 8000
WORKDIR /hairy-tribble

# Download enhanced version of TCache.
RUN cd /home/ph &&\
    git clone https://github.com/ariep/TCache.git &&\
    cd TCache &&\
    git checkout 07051743851cce0a97d1284246232b5e48686292

# Download enhanced version of tst.
RUN cd /home/ph &&\
    git clone https://github.com/ariep/language-spelling &&\
    cd language-spelling &&\
    git checkout 98936c01f0fc0baf35b24e9ae975a5d808123aa3

# Download enhanced version of psqueues.
RUN cd /home/ph &&\
    git clone https://github.com/ariep/psqueues &&\
    cd psqueues &&\
    git checkout 1b9d87511bce9f5a3e4db6fa46a43dc03a965308

# Download text-index.
RUN cd /home/ph &&\
    git clone https://github.com/ariep/text-index.git &&\
    cd text-index &&\
    git checkout 2a772d473286098d5a59e4711eb9349400ae2704

# Copy Cabal install file and only install dependecies.
COPY ./ph.cabal /hairy-tribble/ph.cabal
COPY ./install_cabal_dependencies.sh /hairy-tribble/install_cabal_dependencies.sh
RUN cd /home/ph &&\
    cabal sandbox init &&\
    cabal sandbox add-source /home/ph/TCache &&\
    cabal sandbox add-source /home/ph/language-spelling/tst &&\
    cabal sandbox add-source /home/ph/psqueues &&\
    cabal sandbox add-source /home/ph/text-index &&\
    cabal sandbox add-source /hairy-tribble &&\
    cabal update &&\
    touch /hairy-tribble/LICENSE &&\
    cabal install happy &&\
    sh /hairy-tribble/install_cabal_dependencies.sh &&\
    rm /hairy-tribble/LICENSE

# Now do actual build.
ADD ./src/ /hairy-tribble/src/
RUN cd /home/ph &&\
    touch /hairy-tribble/LICENSE &&\
        cabal install ph &&\
        rm /hairy-tribble/LICENSE

# Put sanbox binaries in path.
ENV PATH /home/ph/.cabal-sandbox/bin:$PATH

# Add rest framework files.
ADD ./rest-gen-files/ /hairy-tribble/rest-gen-files/

# Add web-client files.
ADD ./client/ /tmp/client/

# Install Bower and npm dependencies and minify js files.
# Files need to be copied to be writable for user ph.
RUN cp -r /tmp/client /home/ph/ &&\
    cd /home/ph/client/assets &&\
    npm install &&\
    bower install &&\
    gulp uglify &&\
    cp -r /home/ph/client /hairy-tribble/client

# Copy the configuration file to the container.
RUN mkdir /home/ph/.serve &&\
    ln -s /hairy-tribble/config/config /home/ph/.serve/config

# Expose directory for development and deployment.
VOLUME ["/hairy-tribble/client", "/hairy-tribble/config"]

# Work around docker not passing sigTERM to PID 1.
ADD ./my_init /
ENTRYPOINT ["/my_init","--skip-runit","--skip-startup-files"]

# Run rest when this container is started.
CMD ["rest"]


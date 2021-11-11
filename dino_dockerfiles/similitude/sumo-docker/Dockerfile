FROM maven:3

ENV SUMO_VERSION 0.25.0
ENV SUMO_SRC sumo-src-$SUMO_VERSION
ENV SUMO_HOME /opt/sumo

# Install system dependencies.
RUN apt-get update && apt-get install -qq \
    wget \
    g++ \
    make \
    libxerces-c3.1 \
    libxerces-c3-dev \
    python \
    libproj-dev \
    proj-bin

# Download and extract source code
RUN wget http://downloads.sourceforge.net/project/sumo/sumo/version%20$SUMO_VERSION/sumo-src-$SUMO_VERSION.tar.gz
RUN tar xzf sumo-src-$SUMO_VERSION.tar.gz && \
    mv sumo-$SUMO_VERSION $SUMO_HOME && \
    rm sumo-src-$SUMO_VERSION.tar.gz

# Configure and build from source.
RUN cd $SUMO_HOME && ./configure && make install

# Ensure the installation works. If this call fails, the whole build will fail.
RUN sumo

# Download and compile traci4j library
RUN apt-get install -qq -y ssh-client git
RUN mkdir -p /opt/traci4j 
WORKDIR /opt/traci4j
RUN git clone https://github.com/egueli/TraCI4J.git /opt/traci4j && mvn package -Dmaven.test.skip=true

# Add volume to allow for host data to be used
RUN mkdir /data
VOLUME /data

# Expose a port so that SUMO can be started with --remote-port 1234 to be controlled from outside Docker
EXPOSE 1234

ENTRYPOINT ["sumo"]

CMD ["--help"]


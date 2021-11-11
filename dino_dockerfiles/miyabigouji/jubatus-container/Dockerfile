# jubatus base image
FROM buildpack-deps:jessie

ENV PATH /usr/local/bin:$PATH

ENV LANG C.UTF-8

# runtime dependencies
# RUN apt-get update && apt-get install -y python python-dev && rm -rf /var/lib/apt/lists/*

# install the latest jubatus
RUN git clone https://github.com/jubatus/jubatus-installer.git
RUN cd jubatus-installer && \
    git checkout -b refs/tags/1.0.5 && \
    ./install.sh -p /usr/local && \
    rm -rf ./download

# set environment variables from /user/local/jubatus/profile
ENV JUBATUS_HOME /usr/local
ENV PATH ${JUBATUS_HOME}/bin:${PATH}
ENV LD_LIBRARY_PATH ${JUBATUS_HOME}/lib:${LD_LIBRARY_PATH}
ENV LDFLAGS -L${JUBATUS_HOME}/lib ${LDFLAGS}
ENV CPLUS_INCLUDE_PATH ${JUBATUS_HOME}/include:${CPLUS_INCLUDE_PATH}
ENV PKG_CONFIG_PATH ${JUBATUS_HOME}/lib/pkgconfig:${PKG_CONFIG_PATH}

CMD ["jubarecommender", "--configpath=/usr/local/share/jubatus/example/config/recommender/inverted_index.json", "--rpc-port=9199", "--thread=2"]

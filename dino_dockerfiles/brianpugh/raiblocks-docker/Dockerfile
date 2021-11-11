FROM ubuntu:16.04
LABEL maintainer="Brian Pugh <bnp117@gmail.com>"

# Install some standard packages
# Ubuntu images automattically apt-get clean after every apt-get
RUN apt-get update && apt-get install -y \
    cmake \
    g++ \
    git \
    wget

ENV BOOST_URL=https://netix.dl.sourceforge.net/project/boost/boost/1.66.0/boost_1_66_0.tar.gz

WORKDIR /

# Download and install boost
RUN wget -O boost.tar.gz ${BOOST_URL} \
    && mkdir boost \
    && tar xzf boost.tar.gz -C boost --strip-components 1 \
    && rm boost.tar.gz \
    && cd boost \
    && ./bootstrap.sh \
    && ./b2 --prefix=/[boost] link=static install \
    && cd .. && rm -rf boost

ENV XRB_BRANCH=master \
    XRB_URL=https://github.com/clemahieu/raiblocks.git

# Clone the RaiBlocks git, change branch, and build
ADD https://api.github.com/repos/clemahieu/raiblocks/git/refs/heads/$BRANCH version.json
RUN git clone ${XRB_URL} raiblocks \
    && cd raiblocks \
    && git checkout ${XRB_BRANCH} \
    && git submodule init \
    && git submodule update \
    && mkdir build \
    && cd build \
    && cmake -DBOOST_ROOT=/[boost] -G "Unix Makefiles" .. \
    && make rai_node \
    && mv rai_node / \
    && rm -rf raiblocks

EXPOSE 7075 7075/udp 7076

CMD ["/rai_node", "--daemon"]

FROM alpine:edge

ENV BUILDPKGS "git perl autoconf automake flex gawk gcc m4 make g++ bash"
ENV RUNPKGS "mc"

RUN apk --update --no-cache add $RUNPKGS && \
    apk --no-cache add --virtual build-dependencies $BUILDPKGS && \
\
    mkdir /usr/src && cd /usr/src && \
    git clone https://github.com/SDL-Hercules-390/hyperion.git && \
    cd /usr/src/hyperion && \
    ./autogen.sh
    
RUN cd /usr/src/hyperion && \
    /bin/bash ./configure --enable-ipv6=no
    
RUN cd /usr/src/hyperion && \
    make

RUN cd /usr/src/hyperion && \
    make install

    
    #apk del build-dependencies && \
    #rm -rf /var/cache/apk/* && \
  
ENTRYPOINT ["busybox", "sh"]

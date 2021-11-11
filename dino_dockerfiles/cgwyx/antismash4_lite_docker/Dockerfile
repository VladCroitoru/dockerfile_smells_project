FROM antismash/standalone-lite:4.0.0

MAINTAINER cheng gong <512543469@qq.com>

ENV ANTISMASH_URL="https://dl.secondarymetabolites.org/releases"
ENV ANTISMASH_VERSION="4.0.0"

# Grab the databases
WORKDIR /antismash-${ANTISMASH_VERSION}
#RUN python download_databases.py

ADD instance.cfg antismash/config/instance.cfg

ENV PATH /antismash-${ANTISMASH_VERSION}:$PATH

ENTRYPOINT []
CMD ["/bin/bash"]

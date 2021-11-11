FROM alpine:latest

# Get build-base, automake, autoconf, and then compile.  Clean up when finished!

ADD . /samplicator

RUN apk add --update build-base automake autoconf && \
cd /samplicator && \
./autogen.sh && \
./configure && \
make && \
make install && \
cd / && \
rm -rf /samplicator && \
apk del --purge build-base automake autoconf

EXPOSE 2000/udp

# For easy deployment, specify the receivers argument as an environment variable.
# For use with a config file, you'll have to customize the image or build off of this one.

CMD /usr/local/bin/samplicate $RECEIVERS

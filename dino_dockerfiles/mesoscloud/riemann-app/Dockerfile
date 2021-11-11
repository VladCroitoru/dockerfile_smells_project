FROM java:openjdk-8u72-jdk
MAINTAINER Peter Ericson <pdericson@gmail.com>

# https://github.com/Yelp/dumb-init
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && \
chmod +x /usr/local/bin/dumb-init

# http://riemann.io/quickstart.html
RUN VERSION=0.2.11; \
curl -fLOsS https://aphyr.com/riemann/riemann-$VERSION.tar.bz2 && \
test "$(md5sum riemann-$VERSION.tar.bz2 | awk '{print $1}')" = 68733ce5ad99c0974ddd7e3843d5c842 && \
tar jxf riemann-$VERSION.tar.bz2 && \
cp riemann-$VERSION/bin/riemann /usr/local/bin/ && \
cp riemann-$VERSION/lib/riemann.jar /usr/local/lib/ && \
rm -rf riemann-$VERSION riemann-$VERSION.tar.bz2

# http://riemann.io/howto.html
COPY files/usr/local/etc/riemann.config /usr/local/etc/

ENTRYPOINT ["/usr/local/bin/dumb-init"]
CMD ["riemann"]
EXPOSE 5555 5556

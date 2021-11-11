FROM java:8
MAINTAINER Chris Hobbs (RX14) <chris@rx14.co.uk>

ADD . /piespy/
WORKDIR /piespy/

RUN ./gradlew build && \
    sed -i 's/^java/exec java/' run.sh && \
    rm -Rf ~/.gradle .gradle

CMD ["/piespy/run.sh"]


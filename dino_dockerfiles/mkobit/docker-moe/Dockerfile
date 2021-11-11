FROM openjdk:8u131-jre-alpine
# perl is used in unit tests
# TODO: Checking out a specific revision (for now) and fix the dependency resolution failure for temporary fix.
# see https://github.com/google/MOE/pull/41
RUN apk add --no-cache \
        git \
        mercurial \
        subversion \
    && apk add --no-cache --virtual=build-dependencies \
        openjdk8 \
        perl \
        bash \
        maven \
    && git clone --single-branch --branch patch-1 https://github.com/mkobit/MOE.git \
    && cd MOE \
    git checkout b9c7194ec1c39d87271612bed28e8f9dd559c9bd \
    && mvn verify \
    && util/make-binary.sh \
    && mv client/target/moe /usr/local/bin/moe \
    && rm -rf ~/.m2 \
    && cd ../ \
    && rm -rf MOE \
    && apk --purge -v del build-dependencies

ENTRYPOINT ["moe"]

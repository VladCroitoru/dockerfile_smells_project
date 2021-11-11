# https://github.com/phusion/baseimage-docker
FROM hksitorus/predictionio:latest
MAINTAINER harry.kurniawan@bridestory.com

# copying dependencies
RUN mkdir -p /root/.m2/repository
ADD files/repo /root/.m2/repository

# clone ur
RUN mkdir -p /ur && cd /ur && git clone -b bs --single-branch https://github.com/hksitorus/universal-recommender.git vendor

ADD files/engine-vendor.json /ur/vendor/engine.json
ADD files/run /ur/run
RUN chmod +x /ur/run
RUN cd /ur/vendor/ && pio build --verbose

# clean up apt
RUN apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* /var/tmp/* && \
    rm -rf /var/cache/oracle-jdk8-installer

CMD ["bash"]
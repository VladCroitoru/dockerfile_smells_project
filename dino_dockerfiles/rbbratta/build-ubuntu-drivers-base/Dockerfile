FROM ubuntu:14.04
MAINTAINER ross.b.brattain@intel.com


# This will prevent questions from being asked during the install
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        dkms \
        curl \
    && apt-get clean



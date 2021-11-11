# genairics
# VERSION 0.0.3
# The dockerfile sets up the environment for installing dependencies
# in genairics_dependencies.sh
# This script can also be run independently from the dockerfile
# by providing the PREFIX and GAX_INSTALL_PLATFORM_PACKAGES env variable

FROM python:3.6.3
ARG buildtype=production
ENV GAX_REPOS=/repos
ENV GAX_ENVS=/envs
ENV GAX_PREFIX=/usr
ENV GAX_RESOURCES=/resources
ENV GAX_INSTALL_PLATFORM_PACKAGES=
RUN apt-get update
RUN mkdir $GAX_REPOS
ADD genairics/scripts/genairics_dependencies.sh $GAX_REPOS/genairics_dependencies.sh
RUN $GAX_REPOS/genairics_dependencies.sh
RUN if [ "$buildtype" = "production" ]; then pip install genairics; fi
RUN if [ "$buildtype" = "development" ]; then \
    git clone -b dev --single-branch https://github.com/dicaso/genairics.git &&\
    cd genairics && pip install .; fi
EXPOSE 8000
VOLUME ["/resources"]
VOLUME ["/data"]
VOLUME ["/results"]
ENTRYPOINT ["genairics"]
CMD ["-h"]

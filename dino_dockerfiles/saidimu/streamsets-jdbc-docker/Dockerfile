# FROM streamsets/datacollector:2.4.0.0
FROM streamsets/datacollector:2.3.0.1
# FROM streamsets/datacollector:2.2.1.0
# FROM streamsets/datacollector:2.1.0.1

MAINTAINER Said Apale <saidimu@gmail.com>

# build time variable to pass the necessary stage libraries to install
ARG ADD_LIBS

# have to switch to user root, otherwise the SED command does not work in all environments
USER root

# we have to fix the stagelibs command to run on Alpine Linux (the orginal StreamSets docker image is based on)
RUN sed -i -e 's/run sha1sum --status/run sha1sum -s/g'  ${SDC_DIST}/libexec/_stagelibs

# install the necessary stagelibraries if the ADD_LIBS variable is used
RUN if [ "$ADD_LIBS" != "" ]; then ${SDC_DIST}/bin/streamsets stagelibs -install=${ADD_LIBS}; fi

# copy the extended version of docker-entrypoint.sh into the image
COPY docker-entrypoint.sh jdbc-libs.sh /

# copy jdbc-libs into the image
COPY jdbc-libs /jdbc-libs

# copy custom configs
COPY etc ${SDC_CONF}

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["dc", "-exec"]

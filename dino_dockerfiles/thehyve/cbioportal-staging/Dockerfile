#
# Copyright (c) 2018 The Hyve B.V.
# This code is licensed under the GNU Affero General Public License (AGPL),
# version 3, or (at your option) any later version.
#

FROM openjdk:8
LABEL maintainers=" \
 Oleguer Plantalech Casals (The Hyve) <oleguer@thehyve.nl>, \
 Pim van Nierop (The Hyve) <pim@thehyve.nl> \
"

# install build and runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
		maven \
		jq \
		python3 \
		python3-pip \
		python3-venv \
		python3-wheel \
		&& \
		pip3 install setuptools && \
		pip3 install awscli --upgrade --user

# install dependency for running docker client in this container
RUN apt-get update && apt-get install -y libltdl7 && rm -rf /var/lib/apt/lists/*

# get code
ENV STAGING_HOME=/cbioportal-staging
COPY . $STAGING_HOME
WORKDIR $STAGING_HOME

ARG mvnprofiles=''

RUN mvn clean install $mvnprofiles
RUN mv $STAGING_HOME/target/cbioportal-staging-*.jar $STAGING_HOME/target/cbioportal-staging.jar

# install python dependencies for transformation code
RUN pip3 install -r $STAGING_HOME/transformation_requirements.txt

# service to be started with default properties (can be overridden in docker run),
# taking also custom properties, if given at default -v location
ENTRYPOINT ["/cbioportal-staging/target/cbioportal-staging.jar", "--spring.config.location=file:///custom/custom.properties"]

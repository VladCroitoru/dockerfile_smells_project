FROM swift:5.5.0 as build
LABEL maintainer="IBM Swift Engineering at IBM Cloud"
LABEL Description="Template Dockerfile that extends the ibmcom/swift-ubuntu image."

# hadolint ignore=DL3008
RUN apt-get update \
  && apt-get install -y --no-install-recommends sudo libssl-dev libcurl4-openssl-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# We can replace this port with what the user wants
EXPOSE 8080 1024 1025

# Default user if not provided
ARG bx_dev_user=root
ARG bx_dev_userid=1000

# Install system level packages
# RUN apt-get update && apt-get dist-upgrade -y

# Add utils files
ADD https://raw.githubusercontent.com/IBM-Swift/swift-ubuntu-docker/master/utils/tools-utils.sh /swift-utils/tools-utils.sh
ADD https://raw.githubusercontent.com/IBM-Swift/swift-ubuntu-docker/master/utils/common-utils.sh /swift-utils/common-utils.sh
RUN chmod -R 555 /swift-utils

# Create user if not root
RUN if [ "$bx_dev_user" != root ]; then useradd -ms /bin/bash -u $bx_dev_userid $bx_dev_user; fi

# Make password not required for sudo.
# This is necessary to run 'tools-utils.sh debug' script when executed from an interactive shell.
# This will not affect the deploy container.
RUN echo "$bx_dev_user ALL=NOPASSWD: ALL" > /etc/sudoers.d/user && \
    chmod 0440 /etc/sudoers.d/user

# Bundle application source & binaries
COPY . /swift-project
WORKDIR /swift-project
RUN /swift-utils/tools-utils.sh build release


FROM swift:5.5.0
LABEL maintainer="IBM Swift Engineering at IBM Cloud"
LABEL Description="Template Dockerfile that extends the ibmcom/swift-ubuntu-runtime image."

# hadolint ignore=DL3008
RUN apt-get update \
  && apt-get install -y --no-install-recommends sudo libssl-dev libcurl4-openssl-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# We can replace this port with what the user wants
ENV PORT 8080

EXPOSE 8080

# Default user if not provided
ARG bx_dev_user=root
ARG bx_dev_userid=1000

# Install system level packages
# RUN apt-get update && apt-get dist-upgrade -y

# Add utils files
ADD https://raw.githubusercontent.com/IBM-Swift/swift-ubuntu-docker/master/utils/run-utils.sh /swift-utils/run-utils.sh
ADD https://raw.githubusercontent.com/IBM-Swift/swift-ubuntu-docker/master/utils/common-utils.sh /swift-utils/common-utils.sh
RUN chmod -R 555 /swift-utils

# Create user if not root
RUN if [ $bx_dev_user != "root" ]; then useradd -ms /bin/bash -u $bx_dev_userid $bx_dev_user; fi

# Bundle application source & binaries
COPY --from=build /swift-project ./swift-project

# Command to start Swift application
CMD [ "sh", "-c", "cd /swift-project && .build-ubuntu/release/swiftwebapp" ]

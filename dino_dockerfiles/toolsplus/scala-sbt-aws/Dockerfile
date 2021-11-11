FROM hseeberger/scala-sbt

# Install Atlassian Plugin SDK
ARG  SDK_VERSION=6.3.12

RUN curl https://packages.atlassian.com/list/atlassian-sdk-deb/deb-archive/atlassian-plugin-sdk_${SDK_VERSION}_all.deb -O
RUN dpkg -i ./atlassian-plugin-sdk_${SDK_VERSION}_all.deb

# Install AWS CLI
RUN apt-get update -q
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy python-pip
RUN pip install awscli

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy nodejs

# Install yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qy apt-transport-https
RUN apt-get update && apt-get install yarn
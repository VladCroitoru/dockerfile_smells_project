FROM ubuntu:16.04

# Switch to root
USER root

# Work Directory
WORKDIR project/installations/

# Update everything
RUN apt-get update

# Install Dependencies
RUN apt-get install -y build-essential=12.1ubuntu2 \
					   zlib1g-dev=1:1.2.8.dfsg-2ubuntu4.1 \
					   locales \
					   curl \
					   git \
					   openjdk-8-jre \
					   ssh \
					   jq
					   
# Install Ruby & Gems
RUN apt-get install -y ruby-full=1:2.3.0+1
RUN mkdir -p /usr/share/ruby
COPY Gemfile /project/installations/
COPY Gemfile.lock /project/installations/
RUN gem install bundler
RUN bundle install
RUN gem clean

# Install yq & Python
RUN apt-get install -y python python-pip groff
# RUN pip install --upgrade pip
RUN pip install yq

# Install Azure
RUN apt-get install -y lsb-release
RUN apt-get install -y dirmngr
RUN AZ_REPO=$(lsb_release -cs)
RUN apt-get update
RUN echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ wheezy main" | \
    tee /etc/apt/sources.list.d/azure-cli.list
RUN curl -L https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN apt-get install -y apt-transport-https
RUN apt-get update && apt-get install -y azure-cli
    
# Environment Setup
ENV TZ=Asia/Calcutta
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8

COPY build.sh /project/installations/
ENTRYPOINT ./build.sh


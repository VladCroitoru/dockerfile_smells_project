# Pull base image.
FROM node:6.9.2 
MAINTAINER tinytelly <dulwich22@gmail.com>

# Install Yarn package repository
RUN apt-get update && apt-get install -y apt-transport-https ca-certificates apt-utils
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Install time and ts to get timing information
RUN apt-get update && apt-get install -y time moreutils python-pip

# Install Yarn
RUN apt-get install -y yarn=0.17.10-1

# Install Bower
RUN yarn global add bower@1.8.0 && \
    echo '{ "allow_root": true }' > /root/.bowerrc

# Install ember-cli for the Ember build and phantom-js for headless testing
RUN \
	yarn global add ember-cli@2.7.0 &&\
	yarn global add phantomjs-prebuilt@2.1.13

RUN pip install boto3 # required for s3_upload.py

# Define working directory.
WORKDIR /data

# Define default command.
CMD ["bash"]

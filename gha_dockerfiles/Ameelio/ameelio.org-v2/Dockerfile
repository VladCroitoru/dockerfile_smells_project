FROM docker.io/node:14

ENV USER_HOME=/home/docker

# Create docker group/user and disable logins
RUN addgroup --gid 9999 docker \
   && adduser --uid 9999 --gid 9999 --disabled-password --gecos "Docker User" --home ${USER_HOME} docker \
   && usermod -L docker

# Configure apt, install updates and common packages, and clean up apt's cache
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
   && apt-get upgrade --assume-yes \
   && apt-get autoremove --assume-yes \
   && apt-get install --assume-yes --no-install-recommends \
   apt-utils \
   apt-transport-https \
   ca-certificates \
   ca-certificates-java \
   software-properties-common \
   locales \
   && apt-get install --assume-yes --no-install-recommends \
   curl \
   psmisc \
   git \
   build-essential \
   jq \
   && apt-get install --assume-yes --no-install-recommends \
   ffmpeg \
   mysql-server \
   mysql-client \
   && apt-get clean \
   && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/ \
   && update-ca-certificates

# Ensure locale is UTF-8
ENV LANG       en_US.UTF-8
ENV LC_ALL     en_US.UTF-8
ENV LC_TYPE    en_US.UTF-8
ENV LANGUAGE   en_US.UTF-8
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
   && locale-gen \
   && dpkg-reconfigure locales

# Create mnt dir inside the container
RUN chown docker:docker -R /mnt

# Copy package.json into container
RUN mkdir -p /app/src/ssl \
   && chown -R docker:docker /app/src
COPY --chown=docker:docker package.json package-lock.json /app/src/

# switch to docker user
USER docker
WORKDIR /app/src

# Install npm dependencies
#ENV APP_ENV production
#ENV RACK_ENV production
RUN npm install

# Copy remainder of the source code into the container
COPY --chown=docker:docker . /app/src/

RUN npm run build

EXPOSE 8080
CMD npm run start

FROM nicolaspetton/emacs-docker:latest

RUN apt-get update --quiet

# Make sure dpkg does not ask questions (such as which keyboard layout to configure)
ENV DEBIAN_FRONTEND noninteractive

# Install nodejs
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install --quiet -y nodejs
FROM node:latest

# Timezone configuration
ARG TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

RUN apt update && apt install -y yarn

# Adding the init script
COPY ./init_container.sh /usr/local/bin/init_container.sh
RUN chmod +x /usr/local/bin/init_container.sh

ENTRYPOINT [ "/bin/bash", "/usr/local/bin/init_container.sh" ]

# Default folder on SSH
RUN echo "cd /home/assoconnect" >> ~/.bashrc

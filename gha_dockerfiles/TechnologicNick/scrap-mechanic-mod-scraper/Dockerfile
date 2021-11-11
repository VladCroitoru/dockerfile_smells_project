# Install steamcmd under the user steam
FROM cm2network/steamcmd:latest

# Install curl
USER root
RUN apt install -y curl

# Install node (under the user steam)
USER steam

ENV NODE_VERSION=v15.14.0
RUN curl  -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.38.0/install.sh | bash

ENV NVM_DIR=/home/steam/.nvm

RUN /bin/bash -c "source $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use --delete-prefix $NODE_VERSION"
ENV PATH="$NVM_DIR/versions/node/$NODE_VERSION/bin:$PATH"


# Copy project files
RUN mkdir /home/steam/app
WORKDIR /home/steam/app
RUN ls -la
COPY --chown=steam . .
RUN ls -la
RUN whoami

RUN npm install --production
CMD npm start
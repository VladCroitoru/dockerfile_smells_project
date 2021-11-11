FROM nodesource/node:wheezy

RUN npm install -g bower
RUN npm install -g grunt-cli

# Create a nonroot user, and switch to it
RUN /usr/sbin/useradd --create-home --home-dir /usr/local/nonroot --shell /bin/bash nonroot

COPY . /src
RUN chown -R nonroot /src
USER nonroot

# ENV MONGOHQ_URL mongodb://mongo/mean-dev
# ENV NODE_ENV production

WORKDIR src/web

# Install app dependencies
RUN npm install

EXPOSE 3000

CMD grunt >> log.txt

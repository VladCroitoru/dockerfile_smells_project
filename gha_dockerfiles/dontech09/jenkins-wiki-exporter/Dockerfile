FROM node:16.8.0
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN wget -q -nc -O - https://github.com/jgm/pandoc/releases/download/2.7.3/pandoc-2.7.3-linux.tar.gz |  tar xvzf - --strip-components=2 -C /usr/bin pandoc-2.7.3/bin/pandoc

USER node
ENV NODE_ENV=production
WORKDIR /home/node
COPY --chown=node package.json package-lock.json ./
RUN npm install
COPY --chown=node . .
CMD ["npm","run","start"]

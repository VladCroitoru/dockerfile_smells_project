FROM jgillman/node12-libvips
MAINTAINER Joel Gillman <joel@joelgillman.com>

ENV INSTALL_PATH /pantograph
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY package.json package.json
RUN npm install

COPY . .

ENV PORT 80
EXPOSE 80

CMD [ "node", "index.js" ]

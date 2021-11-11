FROM mpneuried/nodejs-alpine-buildtools-gm:latest
MAINTAINER ketchupbomb

RUN git clone https://github.com/exane/not-gwent-online.git
WORKDIR /not-gwent-online
RUN npm install
RUN npm run build
RUN sed -i 's/127.0.0.1/0.0.0.0/' public/Config.js

# On macOS, a file is incorrectly named and needs to be renamed
# RUN cp public/build/cards.PNG public/build/cards.css

EXPOSE 3000/tcp 16918/tcp

ENTRYPOINT ["/usr/bin/node"]
CMD ["/not-gwent-online/server/server.js"]

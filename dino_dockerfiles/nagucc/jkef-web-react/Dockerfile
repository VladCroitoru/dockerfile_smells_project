FROM node

ADD *.js /nagu/
ADD *.json /nagu/
ADD .babelrc /nagu/
ADD lib /nagu/lib
ADD src /nagu/src
ADD static /nagu/static
ADD tools /nagu/tools

WORKDIR /nagu

RUN npm install
RUN npm run build --release
EXPOSE 5000

CMD node build/server.js

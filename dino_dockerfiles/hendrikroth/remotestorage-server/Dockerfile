FROM mhart/alpine-node
MAINTAINER Hendrik Roth <hi@hendrikroth.com>
WORKDIR /src
ADD src .
RUN npm install
VOLUME ["/storage"]
EXPOSE 3000
CMD ["node", "index.js"]

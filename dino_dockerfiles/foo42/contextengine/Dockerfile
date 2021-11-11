FROM node

WORKDIR /src

ADD package.json /src/
ENV NODE_ENV production
RUN npm install
ADD . /src

EXPOSE 9005
CMD ["node", "."]

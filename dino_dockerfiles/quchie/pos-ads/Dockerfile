FROM mhart/alpine-node:6.2.1
WORKDIR /src
ADD . .
RUN npm install
EXPOSE 80
CMD ["npm", "run", "build"]
CMD ["npm", "run", "start:prod"]

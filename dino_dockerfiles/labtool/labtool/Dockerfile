FROM node:8-slim

#Install serve package
RUN npm install -g serve@6.5.8

#Switch to workdir and copy contents
WORKDIR /code
COPY ./labtool2.0 ./
COPY ./labtool2.0/package.json ../

#Run ci and build
RUN npm ci
RUN npm run build

#Export path properly
ENV PATH=".:${PATH}"

#Expose listen port
EXPOSE 3000

ENTRYPOINT ["serve"]
CMD [ "-p", "3000", "-s", "build" ]

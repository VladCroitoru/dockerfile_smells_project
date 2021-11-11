#docker build --rm -t nodeimg -f Dockerfile --build-arg client=basic-http-client --build-arg server=node-http-json .
#docker run --net testnet -h nodehttpjson --ip 172.18.0.37 --add-host nodehttpjson:127.0.0.1 -p 8080:8080 -d nodeimg

FROM node:slim
ARG client
ARG server

LABEL package.server.name="${server}" \
	  package.client.name="${client}"

RUN groupadd -r test && \
	useradd -r -m -s /bin/bash -g test test
RUN npm install tsd typings gulp -g

COPY ./${server} /home/test/server
COPY ./${client} /home/test/client
RUN chown -hR test:test /home/test
USER test

WORKDIR /home/test/server
RUN npm install && \
	tsd install && \
	typings install && \
	gulp script-express
RUN mv -f ./wwwroot ../wwwroot && rm -r ../server

WORKDIR /home/test/client
RUN npm install && \
	tsd install && \
	typings install && \
	gulp build
RUN mv -f ./wwwroot ../wwwroot/client && rm -r ../client
#RUN touch ../wwwroot/client/assets/icons/favicon.ico

WORKDIR /home/test/wwwroot
EXPOSE 8080
CMD ["node", "../wwwroot/app-express.js"]

#ENTRYPOINT ["/bin/bash", "-c"]
#ENTRYPOINT ["node", "../wwwroot/app-express.js"]

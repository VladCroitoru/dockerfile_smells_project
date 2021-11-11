FROM node:0.12-onbuild

WORKDIR /node_app

COPY . /node_app

RUN cd /node_app && npm install .

EXPOSE 2998

CMD [ "/node_app/docker/start.sh" ]

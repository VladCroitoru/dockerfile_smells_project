FROM duraark/microservice-base

MAINTAINER Martin Hecher <martin.hecher@fraunhofer.at>

RUN mkdir /opt/workbench-ui
WORKDIR /opt/workbench-ui

COPY ./package.json /opt/workbench-ui
RUN npm install ember-cli -g && npm install

COPY ./bower.json /opt/workbench-ui
RUN bower install --allow-root

COPY ./ /opt/workbench-ui

CMD ["ember", "serve", "--prod"]

EXPOSE 4200

# Doesn't work above Node 14
FROM node:14@sha256:4164d987bfceb62b17db4938d535dd31fc50d6ee0b4e00ac7a774f82af408d48

ENV ACCEPT_HIGHCHARTS_LICENSE 1
ENV HIGHCHARTS_VERSION "latest"
ENV HIGHCHARTS_USE_STYLED 1
ENV HIGHCHARTS_USE_MAPS 0
ENV HIGHCHARTS_MOMENT 0
ENV HIGHCHARTS_USE_GANTT 0

ENV OPENSSL_CONF=/etc/ssl/

# Use a specific user to do these actions
ARG UID=12000
ARG GID=12001
ARG UNAME=highcharts
# Add the user with a static UID and statid GID
RUN groupadd --gid $GID $UNAME && useradd --uid $UID --gid $UNAME $UNAME
RUN mkdir /home/highcharts
RUN chown -R $UID:$GID /home/highcharts

# Log in as the newly created user
USER $UNAME

WORKDIR /home/highcharts

RUN git clone https://github.com/highcharts/node-export-server.git && cd node-export-server && git checkout 1e992ac40e5f192c9c32fbca4c8b0571062b6247

RUN cd node-export-server && npm install --production
RUN node node-export-server/build.js

EXPOSE 7801

# Migrate and start webserver
CMD ["sh","-c","./node-export-server/bin/cli.js --enableServer 1 --logLevel 4 --workLimit 20"]
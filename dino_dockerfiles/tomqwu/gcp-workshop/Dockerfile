FROM node

ARG GIT_COMMIT=unspecified

LABEL git_commit=$GIT_COMMIT

ENV APP_HOME /gcp_workshop_app

RUN mkdir ${APP_HOME}

COPY _docker/init.sh /usr/local/bin/

COPY . ${APP_HOME}/

RUN cd ${APP_HOME} && npm install

RUN cd ${APP_HOME}/client && yarn install

EXPOSE 3000

CMD /usr/local/bin/init.sh
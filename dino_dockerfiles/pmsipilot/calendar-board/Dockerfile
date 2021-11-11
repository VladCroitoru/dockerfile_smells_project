FROM httpd:2.4

MAINTAINER Cyprien DIOT <industrialisation@pmsipilot.com>

RUN apt-get update && apt-get install -y curl make

RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install -y nodejs

ENV CALENDARBOARD_CLIENT_ID client_id
ENV CALENDARBOARD_CLIENT_SECRET client_secret
ENV CALENDARBOARD_PROJECT_ID project_id
ENV CALENDARBOARD_ORIGIN "http://localhost"

RUN mkdir /calendar-board

ADD docker/entrypoint.sh /entrypoint.sh
ADD index.html htdocs/
ADD index.js Makefile package.json /calendar-board/
ADD config/ /calendar-board/config/
ADD src /calendar-board/src/
RUN cd /calendar-board && make node_modules

ENTRYPOINT [ "/entrypoint.sh" ]

FROM ubuntu:16.04
MAINTAINER Connor Scully-Allison
LABEL description="Front End Application for Wells Fargo Data Mining Competition"


RUN apt-get update -y
RUN apt-get install --yes curl
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs


RUN nodejs --version 
RUN npm --version

COPY . /wf-frontend
WORKDIR /wf-frontend

RUN npm install -g @angular/cli
RUN npm install

EXPOSE 4444
ENV FRONTEND_PORT 80
ENV FRONTEND_HOST 127.0.0.1
EXPOSE ${FRONTEND_PORT}

CMD ng serve --host 127.0.0.1 --port 4444

FROM firstandthird/node:8.9-2-onbuild

USER root
RUN apk add --update make gcc openssl-dev libffi-dev python-dev musl-dev docker curl bash py-pip curl-dev

RUN pip install docker-compose

RUN curl https://raw.githubusercontent.com/firstandthird/docker-builder/3.12.1/builder > /home/app/builder
RUN chmod +x /home/app/builder

RUN ./bin/install-docker-app

ENV PORT=8080
ENV SECRET=""
ENV GITHUB_TOKEN=""
ENV REPOS=/repos
ENV NODE_ENV production

VOLUME /repos

EXPOSE 8080

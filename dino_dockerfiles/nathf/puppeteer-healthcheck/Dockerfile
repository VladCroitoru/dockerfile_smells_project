FROM node:8.9.4-alpine as build
COPY . /root/healthcheck
RUN cd /root/healthcheck && \
    yarn && \
    yarn build


FROM alekzonder/puppeteer:1.1.1
RUN mkdir -p /home/pptruser/app
WORKDIR /home/pptruser/app

RUN mkdir -p /home/pptruser/.npm-global
RUN npm config set prefix '/home/pptruser/.npm-global'
ENV PATH="/home/pptruser/.npm-global/bin:${PATH}"

RUN chown -R pptruser:pptruser /home/pptruser/.npm-global
RUN chown -R pptruser:pptruser /home/pptruser/app

COPY --from=build /root/healthcheck/lib /home/pptruser/app/lib
COPY ./bin/ /home/pptruser/app/bin/
COPY ./package.json /home/pptruser/app/package.json
COPY ./yarn.lock /home/pptruser/app/yarn.lock

ENV NODE_ENV production
RUN  cd /home/pptruser/app && \
      yarn global add /home/pptruser/app

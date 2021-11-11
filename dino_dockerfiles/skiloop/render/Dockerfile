FROM skiloop/docker-node

RUN addgroup -S app && adduser -S -g app app

# Alternatively use ADD https:// (which will not be cached by Docker builder)
RUN apk --no-cache add git chromium

WORKDIR /root/

# Turn down the verbosity to default level.
ENV NPM_CONFIG_LOGLEVEL warn

# clone render project
WORKDIR /home/
RUN git clone https://github.com/skiloop/render.git app 

WORKDIR /home/app
RUN echo "install dependencies" && npm i

# install alternative chromeless
WORKDIR /tmp
RUN npm i -g rimraf typescript
RUN git clone https://github.com/anttiviljami/chromeless.git 
WORKDIR chromeless 
RUN npm i && npm run-script build && rm -rf /home/app/node_modules/chromeless/dist && cp -a dist /home/app/node_modules/chromeless/ 
RUN npm un -g rimraf 
WORKDIR /tmp
RUN rm -fr chromeless


# Set correct permissions to use non root user
WORKDIR /home/app/

# chmod for tmp is for a buildkit issue (@alexellis)
RUN chown app:app -R /home/app \
    && chmod 777 /tmp

USER app
EXPOSE 3000

ENTRYPOINT [ "npm" ]
CMD ["run", "start"]



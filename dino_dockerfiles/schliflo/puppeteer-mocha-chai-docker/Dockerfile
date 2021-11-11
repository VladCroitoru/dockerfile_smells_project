FROM schliflo/docker-puppeteer

USER root

WORKDIR /validator/

ADD package.json /validator/
ADD utils /validator/utils/

RUN yarn global add \
        chai@4 \
        mocha@7 \
    && yarn cache clean \
    && fix_permissions \
    && chown -R $APPLICATION_USER:$APPLICATION_GROUP /validator

USER $APPLICATION_USER

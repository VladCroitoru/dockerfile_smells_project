FROM danlynn/ember-cli:3.7.1 as ember
WORKDIR /base-cms
COPY package.json yarn.lock /base-cms/
COPY ./services/manage /base-cms/services/manage/
RUN yarn
WORKDIR /base-cms/services/manage
RUN node_modules/.bin/ember build --env=production


FROM node:10.15
ENV NODE_ENV production
ADD ./ /base-cms
WORKDIR /base-cms

# Create volume for management app assets
VOLUME /base-cms/services/manage/dist
COPY --from=ember /base-cms/services/manage/dist /base-cms/services/manage/dist/manage

# Create volume for management app config
VOLUME /etc/nginx/conf.d
COPY ./services/manage/nginx.conf /etc/nginx/conf.d/manage.conf

RUN yarn --production

# WORKDIR /base-cms/services/nextjs-example-website
# RUN node_modules/.bin/next build site
# WORKDIR /base-cms

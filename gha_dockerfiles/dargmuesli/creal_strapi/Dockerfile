#######################
# strapi production build.

# Should be the specific version of strapi/base.
# v14 is not kept up to date as of 2021-06-05.
FROM strapi/base:12-alpine@sha256:d91a598b735cfd19eb440e344389f575de9a92e593ab00b86976fc374e0fe96d AS development

ENV NODE_ENV=production

WORKDIR /srv/app/

COPY ./ /srv/app/

RUN yarn install \
  && yarn cache clean \
  && yarn build

CMD ["yarn", "start"]

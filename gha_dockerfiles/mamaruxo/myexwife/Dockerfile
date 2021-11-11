FROM node:16.8
WORKDIR /code
COPY package.json yarn.lock ./
RUN yarn install --frozen-lockfile
COPY src ./src
COPY tsconfig.json ./
# install --prod strips devDeps after build is done
RUN yarn build && yarn install --frozen-lockfile --production

FROM node:16.8
WORKDIR /code
# https://stackoverflow.com/questions/37458287/how-to-run-a-cron-job-inside-a-docker-container
RUN apt-get update && apt-get -qq --no-install-recommends install cron && apt-get clean
COPY run.sh ./
COPY --from=0 /code/node_modules ./node_modules
COPY --from=0 /code/dist ./dist
ENV NODE_ENV=production
ENTRYPOINT ["bash", "run.sh"]
CMD ["yarn", "start"]

FROM node:14.17.0-buster-slim
RUN apt-get update && apt-get install -y git
RUN yarn global add gatsby-cli
WORKDIR app
CMD ["yarn", "develop"]

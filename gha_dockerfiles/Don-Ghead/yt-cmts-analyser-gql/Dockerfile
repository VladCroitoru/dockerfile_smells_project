# Use the lts-alpine image digest as per dockers suggestions for a deterministic build
FROM node@sha256:8c94a0291133e16b92be5c667e0bc35930940dfa7be544fb142e25f8e4510a45

LABEL version="1.0"
LABEL description="Base docker image for the youtube comments analyser gql backend"
LABEL maintainer="luketparsons@gmail.com"

ENV NODE_ENV production
WORKDIR /app

# Change owner to node user when copying files over
COPY --chown=node:node ["package.json", "yarn.lock", "./"]

# --frozen-lockfile works same as `npm ci` whereby it 
#   - Doesn't generate yarn.lock
#   - Fails if update is needed
RUN yarn install --production --frozen-lockfile

COPY --chown=node:node . .

EXPOSE 4000

USER node

CMD ["yarn", "start"]

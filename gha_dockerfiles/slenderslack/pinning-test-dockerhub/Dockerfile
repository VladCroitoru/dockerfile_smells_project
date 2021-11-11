FROM node:12.18.1
ENV NODE_ENV=production

WORKDIR /app

# ARG VCS_REF
# ARG VCS_URL
# ARG REVISION
# ARG SOURCE
# LABEL org.label-schema.vcs-ref=$VCS_REF
# LABEL org.label-schema.vcs-url=$VCS_URL
# LABEL org.opencontainers.image.revision=$REVISION
# LABEL org.opencontainers.image.source=$SOURCE

COPY ["package.json", "package-lock.json*", "index.js", "./"]

RUN npm install --production

COPY . .

CMD [ "node", "index.js" ]

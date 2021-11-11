FROM node:8.10.0-alpine

LABEL maintainer="Jeremie Rodriguez <contact@jeremierodriguez.com> (https://github.com/jeremiergz)" \
    description="Centralized configuration server providing a dynamic RESTful API, allowing retrieval of entire files content or their parsed properties."

WORKDIR /app
COPY package.json LICENSE README.md ./

# Copy build files
COPY ./src/ ./src/
COPY copyright-notice.txt tsconfig.json webpack.config.ts ./

RUN npm install && \
    npm run build && \
    npm prune --production && \
    rm -r ./src copyright-notice.txt tsconfig.json webpack.config.ts

ENV NODE_ENV=production \
    LOG_DIR=/var/log

EXPOSE 20490

CMD ["npm", "start"]

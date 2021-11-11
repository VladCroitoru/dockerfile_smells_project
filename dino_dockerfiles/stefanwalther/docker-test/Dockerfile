ARG NODE_VER="14.3.0"
# --------------------------------------
#               BASE NODE
# --------------------------------------
FROM node:${NODE_VER}-alpine as BASE

ARG PORT=3000
ENV PORT=$PORT

ENV HOME=/app
RUN mkdir -p $HOME
WORKDIR $HOME

COPY package.json package-lock.json ./

# --------------------------------------
#              DEPENDENCIES
# --------------------------------------
FROM BASE as DEPENDENCIES

RUN npm install --only=production

# copy production node_modules aside
RUN cp -R node_modules prod_node_modules

# install ALL node_modules, including 'devDependencies'
RUN npm install


# --------------------------------------
#                  TEST
# --------------------------------------
# run linters, setup and tests
FROM dependencies AS TEST

COPY .eslintrc.json .
COPY /src ./src/
COPY /test ./test/

RUN  npm run lint && npm run test

# --------------------------------------
#                 RELEASE
# --------------------------------------
FROM BASE as RELEASE

# copy production node_modules
COPY --from=dependencies /app/prod_node_modules ./node_modules
COPY /src ./src/

COPY ./nodemon.json ./

EXPOSE $PORT

CMD ["npm", "run", "start"]


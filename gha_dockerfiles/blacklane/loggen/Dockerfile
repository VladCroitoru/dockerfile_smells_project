FROM alpine:3.5 AS base

# install node
RUN apk add --no-cache nodejs-current

# set working directory
WORKDIR /root/loggen

# Copy data file
COPY data/ .

# copy project file
COPY package.json .

##########

FROM base AS dependencies

# install node packages
RUN npm set progress=false && npm config set depth 0
RUN npm install --only=production

# copy production node_modules aside
RUN cp -R node_modules prod_node_modules

# install ALL node_modules, including 'devDependencies'
RUN npm install

########

FROM base AS release

# copy production node_modules
COPY --from=dependencies /root/loggen/prod_node_modules ./node_modules

# copy app sources
COPY . .

# expose port and define CMD
CMD npm run start

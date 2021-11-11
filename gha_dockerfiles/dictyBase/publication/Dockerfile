# It's a multi stage build https://docs.docker.com/develop/develop-images/multistage-build/#stop-at-a-specific-build-stage
# The first one builds a single file js for the web app
# The second one copies the file and server with a golang static web server
FROM node:10.4.0-alpine
LABEL maintainer "Eric Hartline <eric.hartline@northwestern.edu>"

# include git, otherwise npm install doesn't work
RUN apk update && apk upgrade && \
  apk add --no-cache bash git openssh jq

# URL for api server
ARG api_server
ENV REACT_APP_API_SERVER ${api_server:-https://betafunc.dictybase.local}

# URL for auth server
ARG auth_server
ENV REACT_APP_AUTH_SERVER ${auth_server:-https://betatoken.dictybase.local}

# URL for graphql server
ARG graphql_server
ENV REACT_APP_GRAPHQL_SERVER ${graphql_server:-https://betagraphql.dictybase.local}

# base path for React Router
ARG basename
ENV REACT_APP_BASENAME ${basename:-publication}

# URL for navbar json
ARG navbar_json
ENV REACT_APP_NAVBAR_JSON ${navbar_json:-https://raw.githubusercontent.com/dictyBase/migration-data/master/navbar/navbar.json}

# URL for footer json
ARG footer_json
ENV REACT_APP_FOOTER_JSON ${footer_json:-https://raw.githubusercontent.com/dictyBase/migration-data/master/footer/footer.json}

# Setup client keys for third party auth
ARG client_keys
ENV CLIENT_KEYS ${client_keys:-https://raw.githubusercontent.com/dictybase-playground/client-keys/1.0.0/clientConfig.js}

# Create app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# copy only necessary files
COPY package-lock.json tsconfig.json ./

# package.json has to be modified later on, so 
ADD package.json package-dev.json
# create new package.json with relative path
RUN jq '. + {"homepage": "/publication"}' package-dev.json > package.json \
  && rm package-dev.json

# add necessary folders
ADD src src
ADD public public

# overwrite the client key file
ADD $CLIENT_KEYS /usr/src/app/src/common/utils/clientConfig.js

# standard install/build commands
RUN npm install && npm run build

FROM dictybase/static-server:2.0.2
RUN mkdir /www
WORKDIR /www
COPY --from=0 /usr/src/app/build ./
ENTRYPOINT ["/usr/local/bin/app", "run", "-f", "/www", "--sub-url", "/publication"]

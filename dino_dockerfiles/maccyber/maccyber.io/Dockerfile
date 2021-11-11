FROM mhart/alpine-node:10

# Maintainer
MAINTAINER Jonas Enge

#### Begin setup ####

# Bundle app source
COPY . /src

# Change working directory
WORKDIR "/src"

# Install dependencies
RUN npm install --production

# Env variables
ENV SERVER_PORT 3000
ENV TOKEN abc123
# ENV DEBUG DISABLE

# Expose 3000
EXPOSE 3000

# Startup
ENTRYPOINT npm start

### AAP Periodic Application Docker image   ####
FROM adoptapetcom/aap_frontend_env:release
MAINTAINER TRESELLE

WORKDIR /opt/workspace/application_code/

# Argument for npm credential
ARG NPM_TOKEN

### Copy the application code into the docker container  ####
COPY . /opt/workspace/application_code/

### Install Node Package Manager ####
RUN npm install --save-dev

# Remove Credentials [Post Build Action]
RUN rm -f .npmrc

### Expose periodic at PORT 6060, 8080 ####
EXPOSE  6060 8080

### Execute the nodejs application ####
CMD npm start
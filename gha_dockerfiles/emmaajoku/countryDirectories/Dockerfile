# Use the predefined node base image for this module.
FROM node:12.18.1

# create the log directory
RUN mkdir -p /var/log/applications/country-directory

# Creating base "src" directory where the source repo will reside in our container.
# Code is copied from the host machine to this "src" folder in the container as a last step.
RUN mkdir /src
WORKDIR /src
# COPY yarn.lock ./src
COPY . /src


# Install node dependencies

RUN yarn global add typeorm @nestjs/cli

# For development environment, we want to use forever to keep the code running
RUN yarn global add pm2@4.4.1

# RUN yarn

# RUN yarn build

# RUN prisma generate

# Map a volume for the log files and add a volume to override the code
VOLUME ["/src", "/var/log/applications/country-directory"]

# Expose web service and nodejs debug port
EXPOSE  8000
EXPOSE 80

FROM node:7.3.0
MAINTAINER Paul Borrego <leadiv@gmail.com>

# Set up non root user to run install and build
RUN useradd --user-group --create-home --shell /bin/false app

ENV NODE_ENV=${NODE_ENV:-development}
ENV HOME=/home/app
ENV APP=$HOME/breakingnews-vue

# Set up folder and add install files
RUN mkdir -p $APP
COPY package.json $APP
COPY npm-shrinkwrap.json $APP

# Any kind of copying from the host must be down as root so this sets
# the permissions for the app user to be able to read the files
RUN chown -R app:app $HOME/*

USER app
WORKDIR $APP

# Install the dependencies
RUN npm install

# Copy the app source files
USER root
COPY . $APP
RUN chown -R app:app $HOME/*

CMD ["bash"]

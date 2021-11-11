from node:latest

ENV user=rafa93br
# Create a new user to our new container and avoid the root user
RUN useradd --user-group --create-home --shell /bin/false $user && \
    apt-get clean
ENV HOME=/home/$user
ENV APP_FOLDER=$HOME/app


# Create app directory
RUN mkdir -p $APP_FOLDER
WORKDIR $APP_FOLDER

COPY package.json $APP_FOLDER
RUN npm install

RUN chown -R $user:$user $APP_FOLDER/* /usr/local/

COPY . $APP_FOLDER
RUN npm run build

USER $user

EXPOSE 8888
CMD ["npm", "start"]

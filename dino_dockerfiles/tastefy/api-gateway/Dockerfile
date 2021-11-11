from node:latest

ENV user=rafa93br
# Create a new user to our new container and avoid the root user
# RUN useradd --user-group --create-home --shell /bin/false $user && \
    # apt-get clean
ENV HOME=/home/$user
ENV APP_FOLDER=/usr/src


# Create app directory
# RUN mkdir -p $APP_FOLDER
WORKDIR $APP_FOLDER
COPY package.json $APP_FOLDER
# RUN chown -R $user:$user $APP_FOLDER/*

RUN npm install



COPY . $APP_FOLDER
# RUN chown -R $user:$user $APP_FOLDER/*
RUN yarn build

# USER $user
EXPOSE 8090
CMD ["yarn", "start"]

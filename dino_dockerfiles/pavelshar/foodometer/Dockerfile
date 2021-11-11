# Use Chloe -> slim Nodejs + SSH Server container
FROM pavelshar/chloe

# Copy project files
ADD . /foodometer

# Install packages
RUN yarn global add pm2 && \
    cd /foodometer && \
    yarn install


# Init entrypoint + start app with pm2
CMD /.docker/deploy/entrypoint.sh && \
    cd /foodometer && \
    pm2-docker start npm --name foodometer -- start





FROM zenato/puppeteer

USER root

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Only copy the package.json which specifies package dependencies. This is will
# ensure that packages are only re-installed if they are changed.
COPY package.json /usr/src/app/
RUN yarn install

# Copy the application source code and run the optional build step.
COPY . /usr/src/app

EXPOSE 3000

# Change the ownership of the application code and switch to the unprivileged
# user.
# RUN chown -R app:app /usr/src/app
# USER app

# Run the application directly, do not run via npm which heavily pollutes the
# environment variables and other stuff.
CMD [ "node", "index.js" ]

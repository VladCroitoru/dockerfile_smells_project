FROM node:14-alpine

# drop back to the non-privileged user for run-time
WORKDIR /home/node
USER node

# tell node, et al to run in production mode
ENV NODE_ENV production

# copy in the package files so that we can install and build the project
# dependencies
COPY --chown=node:node package*.json ./

# install all the node modules required
RUN npm ci

# copy the code from the project
COPY --chown=node:node ./src ./src
COPY --chown=node:node ./util ./util
COPY --chown=node:node .sequelizerc ./
COPY --chown=node:node ./.secrets ./.secrets

# these variables are for overriding and they only matter during run
ENV LICENSING_DB_HOST override_this_value
ENV LICENSING_DB_PASS override_this_value
ENV TR_DB_PASS override_this_value
ENV RO_TR_DB_PASS override_this_value
ENV TR_NOTIFY_API_KEY override_this_value

# let docker know about our listening port
EXPOSE 3001

# run the default start script, which kicks off a few pre-start things too
CMD ["npm", "start", "--silent"]

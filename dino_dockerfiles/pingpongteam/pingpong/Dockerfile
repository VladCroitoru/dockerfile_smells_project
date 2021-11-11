FROM nginx:1.13-alpine

# Install node
RUN apk add --update nodejs

RUN mkdir -p /opt/frontend/app &&\
    mkdir -p /opt/backend/app

ARG PORT=3005
ENV PORT=${PORT}

COPY default-nginx.conf /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
# COPY index.html /usr/share/nginx/html
# COPY index2.html /usr/share/nginx/html2/index.html

# set the environment type of the node server. This can be either dev or prod.
# dockerfile will default it to prod, the composer file will later override this
ARG NODE_ENV=production
ENV NODE_ENV ${NODE_ENV}
ARG BACKEND_URL=localhost:3001
ENV BACKEND_URL ${BACKEND_URL}
ARG SOCKETIO_SERVER_PORT=3001
ENV SOCKETIO_SERVER_PORT ${SOCKETIO_SERVER_PORT}

ARG DB_USERNAME=pingpong
ARG DB_PASSWORD=pingpongpassword
ARG DB_NAME=pingpong
ARG DB_HOSTNAME=db:5432
ENV DB_USERNAME ${DB_USERNAME}
ENV DB_PASSWORD ${DB_PASSWORD}
ENV DB_NAME ${DB_NAME}
ENV DB_HOSTNAME ${DB_HOSTNAME}

ARG APP_HOST=underskruv.com
ENV APP_HOST ${APP_HOST}
ARG WS_HOST=ws.underskruv.com
ENV WS_HOST ${WS_HOST}

# install dependencies first, in a different location for easier app bind mounting for local development
# FRONTEND
WORKDIR /opt/frontend
COPY frontend/package.json frontend/package-lock.json* ./
RUN npm install && npm cache clean --force
ENV PATH /opt/frontend/node_modules/.bin:$PATH
COPY ./frontend /opt/frontend/app
WORKDIR /opt/frontend/app
RUN npm run-script build
RUN cp -a /opt/frontend/app/build/. /usr/share/nginx/html/

# BACKEND
WORKDIR /opt/backend
COPY backend/package.json backend/package-lock.json* ./
RUN npm install && npm cache clean --force
ENV PATH /opt/backend/node_modules/.bin:$PATH
# copy in our source code last, as it changes the most
COPY ./backend /opt/backend/app

# run the node server
WORKDIR /opt/backend/app
#ENTRYPOINT ["/entrypoint.sh"]
#CMD [ "npm", "start" ]
#CMD ["nginx", "-g", "daemon off;"]
CMD ["/entrypoint.sh"]

FROM mhart/alpine-node

# COPY the files/folders to /code
RUN mkdir -p /code
COPY routes /code/routes/
COPY assets /code/assets/
COPY www /code/www/
COPY node_modules /code/node_modules/
COPY *.json /code/
COPY server.js /code/

RUN ls -la /code

# Set the workdir
WORKDIR /code

EXPOSE  3000
CMD ["node", "server.js"]

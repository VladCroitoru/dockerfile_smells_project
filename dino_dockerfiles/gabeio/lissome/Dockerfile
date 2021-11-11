# use node
FROM node
# default port 80
ENV PORT 80
# expost default port 80
EXPOSE 80
# copy this directory to container
COPY . .
# install manifest
RUN npm install
# install build tools
RUN npm install -g gulp livescript
# build
RUN make
# default script
CMD ["/entrypoint.sh"]

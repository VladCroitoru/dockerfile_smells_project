FROM node:6
MAINTAINER Paolo Scanferla <paolo.scanferla@mondora.com>
RUN mkdir /mondora-website-front
ADD ./ /mondora-website-front/
WORKDIR /mondora-website-front
RUN npm install --unsafe-perm
RUN MINIFY_FILES=true npm run build
EXPOSE 8080
ENTRYPOINT ["./start.sh"]

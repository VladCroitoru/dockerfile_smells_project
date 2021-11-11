FROM nginx

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections

RUN apt-get -qq update
RUN apt-get -qq install git -y
RUN apt-get -qq install nodejs -y
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN apt-get -qq install curl -y
RUN curl -q https://www.npmjs.com/install.sh | sh
COPY src /src
COPY lib /lib
COPY gulp /gulp
COPY gulpfile.js /gulpfile.js
COPY package.json /package.json
RUN npm config set registry http://registry.npmjs.org/
RUN npm install
RUN npm install gulp -g
RUN gulp production
RUN rm -rf src/
RUN rm -rf gulp/
RUN ls /usr/share/nginx/html
RUN rm /usr/share/nginx/html/index.html
RUN ls /usr/share/nginx/html
RUN mv /build/debug.html /build/debugraw.html
RUN mv /build/index.html /build/indexraw.html
RUN cp -avr /build/. /usr/share/nginx/html
RUN rm -rf build/
#from control-ui
# TODO: This is only a workaround, it doesn't trap signals corretly for nginx to stop on SIGINT, has to wait for SIGKILL.
ENTRYPOINT ["/bin/bash", "-c", "envsubst < /usr/share/nginx/html/debugraw.html > /usr/share/nginx/html/debug.html && envsubst < /usr/share/nginx/html/indexraw.html > /usr/share/nginx/html/index.html && nginx -g 'daemon off;'"]
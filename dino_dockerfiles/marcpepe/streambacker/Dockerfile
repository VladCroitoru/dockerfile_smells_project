FROM node:latest
LABEL version="0.0.1"
MAINTAINER Marc Perrin-Pelletier <marc.perrinpelletier@gmail.com>

# WORKDIR /home/stbk
WORKDIR /var/www/stbk

RUN useradd -ms /bin/bash stbk
# RUN useradd stbk
# RUN cd && cp -R .bashrc .profile /home/stbk

# RUN chown -R stbk:stbk /home/stbk
# RUN usermod -u 1000 stbk
RUN chown -R stbk:stbk /var/www
USER stbk

# COPY devops devops/
# COPY bower.json \
     # gulpfile.js \
     # package.json \
     # ./
# ADD . .
# RUN pwd
# RUN npm install
# CMD ./node_modules/.bin/sails lift

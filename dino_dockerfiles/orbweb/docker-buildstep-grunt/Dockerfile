FROM        node
# 1. npm install global grunt bower
# 2. npm install && bower install
# 3. grunt build
RUN         npm set progress=false && npm install -g bower grunt-cli
WORKDIR     /usr/src
CMD         npm install && bower install --allow-root && grunt build --force --output=/usr/build/static

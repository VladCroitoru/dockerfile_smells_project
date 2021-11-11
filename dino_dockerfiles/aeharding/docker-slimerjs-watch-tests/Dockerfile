FROM cmfatih/slimerjs
MAINTAINER Alexander Harding <alexander.harding@software.dell.com>

# install lightweight http server for static content
RUN apt-get install -y webfs

RUN mkdir cux.css


# add your code with a link on runtime
# https://docs.docker.com/reference/run/#volume-shared-filesystems
CMD cd cux.css && webfsd -p 8001 -r ./styleguide && casperjs test test/*.js --engine=slimerjs

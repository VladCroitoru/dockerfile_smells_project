FROM node:8.9.4

LABEL author="Zack Yang <zack9433@gmail.com>"

RUN npm install -g semver conventional-changelog-angular conventional-recommended-bump

ADD clog /bin/
ADD drone-clog.sh /bin/

ENTRYPOINT /bin/drone-clog.sh


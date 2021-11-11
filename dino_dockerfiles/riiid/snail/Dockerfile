FROM fprieur/docker-casperjs
MAINTAINER kyung yeol kim <kykim@riiid.co>

LABEL version="0.0.4"

ADD *.js /src/snail/
ADD deps/*.js /src/snail/

ENTRYPOINT ["casperjs", "/src/snail/index.js"]

# present (Reveal JS presentation using reveal-md)
#
# docker run -v `pwd`:/slides -p 1948:1948 -d madhuakula/present
#

# Using node slim (alpine image for node)
FROM node:slim

MAINTAINER Madhu Akula <madhu.akula@hotmail.com>

# installing reveal-md package
RUN npm install -g reveal-md

# reveal-md default port for presentation 
EXPOSE 1948

# reveal-md local path to give as entrypoint
ENTRYPOINT ["/usr/local/bin/reveal-md"]

CMD [ "--help" ]

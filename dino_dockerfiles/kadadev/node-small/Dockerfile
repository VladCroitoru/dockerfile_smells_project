FROM mhart/alpine-node:10

RUN apk add --no-cache git bash openssh openssh-client libc6-compat

# Add things needed to build grpc
RUN apk add --no-cache python make g++

RUN ["/bin/bash", "-c", "rm /bin/sh && ln -s /bin/bash /bin/sh"]

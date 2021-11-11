FROM alpine:3.7
RUN apk --update add git zip tar bash
COPY entrypoint.sh /entrypoint.sh
RUN chmod -x entrypoint.sh
ENV GIT_BRANCH="master"
ENV GIT_URL="https://github.com/Fiercely/git-zipper"
ENV NAME="fiercely"
ENV PATHS="Dockerfile"
ENTRYPOINT [ "/bin/bash", "/entrypoint.sh" ]
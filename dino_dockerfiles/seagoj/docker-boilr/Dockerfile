# Run Rainbowstream in a container
#
# docker run -it --rm \
#   -v /etc/localtime:/etc/localtime:ro \
#   -v $PWD:/home/boilr/cwd \
#   -v $HOME/.config/boilr:/home/boilr/.config/boilr \
#   --name boilr \
#   seagoj/docker-boilr

FROM golang
LABEL maintainer "Jeremy Seago <seagoj@gmail.com>"
ARG GID=1000
ARG UID=1000
ARG REPO="github.com/Ilyes512/boilr"

RUN groupadd -r boilr -g $GID && useradd --no-log-init -r --create-home -g boilr -u $UID boilr
USER boilr
WORKDIR /home/boilr
RUN go get "${REPO}" && go install "${REPO}"

ENTRYPOINT [ "boilr" ]

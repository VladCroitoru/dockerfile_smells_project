FROM ghcr.io/gregtkogut/statick:publish_docker_image

LABEL "name"="Statick"
LABEL "version"="0.0"
LABEL "repository"="https://github.com/sscpac/statick-action.git"
LABEL "homepage"="https://github.com/sscpac/statick-action"
LABEL "maintainer"="Thomas Denewiler <tdenewiler@gmail.com>"

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
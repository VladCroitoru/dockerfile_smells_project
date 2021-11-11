FROM docker/compose:1.25.3

ARG version="0.1.0-dev"
ARG build_date="unknown"
ARG commit_hash="unknown"
ARG vcs_url="unknown"
ARG vcs_branch="unknown"

LABEL org.label-schema.vendor="softonic" \
    org.label-schema.name="compose-project-running" \
    org.label-schema.description="Waits until a compose project is running" \
    org.label-schema.usage="/src/README.md" \
    org.label-schema.url="https://github.com/softonic/docker-compose-project-running/blob/master/README.md" \
    org.label-schema.vcs-url=$vcs_url \
    org.label-schema.vcs-branch=$vcs_branch \
    org.label-schema.vcs-ref=$commit_hash \
    org.label-schema.version=$version \
    org.label-schema.schema-version="1.0" \
    org.label-schema.build-date=$build_date \
    org.label-schema.docker.cmd="docker run --rm \
        -v \${PWD}/.:/project:ro \
        -v /var/run/docker.sock:/var/run/docker.sock:ro \
        -e TIMEOUT=30 \
        -e COMPOSE_PROJECT_NAME=$(basename \"\$PWD\") \
        softonic/compose-project-is-up" \
    org.label-schema.docker.params="TIMEOUT=Max number of seconds before assume something gone wrong \
        COMPOSE_PROJECT_NAME=Project name used when launching the compose file \
        EXPECTED_CONTAINERS=Number of expected running containers \
        COMPOSE_FILE=Compose file to read. Defaults to none \
        VERBOSE=Output container name if activated (1 for active, 0 for disabled. Defaults to 0)"

COPY ./get-compose-running.sh /get-compose-running.sh

WORKDIR /project

CMD ["/get-compose-running.sh"]

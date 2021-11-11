FROM registry-gitlab.i.wish.com/contextlogic/tooling-image/protobuf/master:v0.0.1 as build

ARG ITA_JOB_TOKEN
ARG GITLAB_ACCESS_TOKEN=${ITA_JOB_TOKEN}
ARG ITA_PROJECT_NAME

# Validating the Arguments
RUN if [[ -z "$GITLAB_ACCESS_TOKEN" ]]; then \
    echo -e "\n[ Error ] GITLAB_ACCESS_TOKEN is missing\n"; \
    exit 1; \
    fi; \
    if [[ -z "$ITA_PROJECT_NAME" ]]; then \
    echo -e "\n[ Error ] ITA_PROJECT_NAME is missing. This should be the same as the value of your project\n"; \
    exit 1; \
    fi

COPY . /go/src/github.com/ContextLogic/${ITA_PROJECT_NAME}
WORKDIR /go/src/github.com/ContextLogic/${ITA_PROJECT_NAME}

RUN git config --global url.https://gitlab-ci-token:${GITLAB_ACCESS_TOKEN}@gitlab.i.wish.com/ContextLogic.insteadof 'https://github.com/ContextLogic'
RUN echo ${ITA_PROJECT_NAME}
RUN GOOS=linux GOARCH=amd64 GO111MODULE=on go build -o bin/${ITA_PROJECT_NAME} github.com/ContextLogic/${ITA_PROJECT_NAME}/pkg

FROM registry-gitlab.i.wish.com/contextlogic/tooling-image/node:13.12.0-alpine as ui_build

ARG ITA_PROJECT_NAME
ENV BIN_NAME=/bin/${ITA_PROJECT_NAME}
ENV LD_LIBRARY_PATH=/usr/lib

COPY --from=build /usr/lib /lib /usr/lib/
COPY --from=build /go/src/github.com/ContextLogic/${ITA_PROJECT_NAME}/bin/${ITA_PROJECT_NAME} /bin/${ITA_PROJECT_NAME}
COPY --from=build /go/src/github.com/ContextLogic/${ITA_PROJECT_NAME}/pkg/config /go/src/github.com/ContextLogic/${ITA_PROJECT_NAME}/pkg/config

CMD [ "sh", "-c", "${BIN_NAME}" ]

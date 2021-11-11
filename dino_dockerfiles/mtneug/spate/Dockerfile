# Copyright (c) 2016 Matthias Neugebauer <mtneug@mailbox.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM golang:1.9-alpine AS build

COPY . /go/src/github.com/mtneug/spate
WORKDIR /go/src/github.com/mtneug/spate

RUN apk add --no-cache make git ca-certificates \
 && make build-static

FROM scratch
LABEL maintainer="Matthias Neugebauer <mtneug@mailbox.org>" \
      org.label-schema.schema-version="1.0" \
      org.label-schema.name="spate" \
      org.label-schema.version="0.1.0" \
      org.label-schema.description="Horizontal service autoscaler for Docker Swarm mode" \
      org.label-schema.usage="https://github.com/mtneug/spate/blob/0.1.0/README.md" \
      org.label-schema.url="https://github.com/mtneug/spate" \
      org.label-schema.vcs-url="https://github.com/mtneug/spate" \
      org.label-schema.docker.debug="docker exec -it $CONTAINER sh" \
      org.label-schema.docker.cmd="docker service create --network 'example' --constraint 'node.role == manager' --mount 'type=bind,src=/var/run/docker.sock,dst=/var/run/docker.sock' --publish 8080:8080 mtneug/spate:0.1.0" \
      org.label-schema.docker.cmd.help="docker run --rm mtneug/spate:0.1.0 --help"

COPY --from=build /go/src/github.com/mtneug/spate/bin/spate /
COPY --from=build /usr/share/ca-certificates/mozilla /etc/ssl/certs/

EXPOSE 8080
ENTRYPOINT ["/spate"]

# Copyright 2017-2019 The FIAAS Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# dockerma archs:amd64,arm,arm64:
FROM python:3.6-alpine3.7 as common
MAINTAINER fiaas@googlegroups.com
# Install any binary package dependencies here
RUN apk --no-cache add \
    yaml

FROM common as build
# Install build tools, and build wheels of all dependencies
RUN apk --no-cache add \
    build-base \
    git \
    yaml-dev
COPY . /skipper
COPY .wheel_cache/*.whl /links/
WORKDIR /skipper
RUN pip wheel . --quiet --no-cache-dir --wheel-dir=/wheels/ --find-links=/links/

FROM common as production
# Get rid of all build dependencies, install application using only pre-built binary wheels
COPY --from=build /wheels/ /wheels/
RUN pip install --quiet --no-index --no-cache-dir --find-links=/wheels/ --only-binary all /wheels/fiaas_skipper*.whl
EXPOSE 5000
CMD ["skipper"]

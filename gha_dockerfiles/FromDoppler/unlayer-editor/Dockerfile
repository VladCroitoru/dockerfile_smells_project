FROM koalaman/shellcheck-alpine as verify-sh
WORKDIR /src
COPY ./*.sh ./
COPY ./**/*.sh ./
RUN shellcheck -e SC1091,SC1090 ./*.sh

FROM node:14.18.1 AS restore
WORKDIR /src
COPY package.json yarn.lock ./
RUN yarn
COPY . .

FROM restore AS verify-format
RUN yarn verify-format

FROM restore AS test
ENV CI=true
RUN yarn coverage:ci

FROM restore as build
RUN yarn build

# Using specific digest (f7f7607...) to avoid unwanted changes in the non-oficial image
FROM ttionya/openssh-client@sha256:f7f7607d56f09a7c42e246e9c256ff51cf2f0802e3b2d88da6537bea516fe142 as final
WORKDIR /work
COPY ./cdn-helpers/* ./
COPY --from=build /src/build ./build/

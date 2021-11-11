# sources:
# https://docs.docker.com/develop/develop-images/multistage-build/
# https://nodejs.org/en/docs/guides/nodejs-docker-webapp/


FROM node:14 as react

WORKDIR /squeng/squawg

COPY feuawg/.npmrc ./
COPY feuawg/package*.json ./
# https://docs.npmjs.com/cli/v7/commands/npm-ci
RUN npm ci

COPY feuawg/public ./public
COPY feuawg/src ./src
# https://create-react-app.dev/docs/adding-custom-environment-variables#linux-macos-bash
RUN INLINE_RUNTIME_CHUNK=false npm run build


FROM hseeberger/scala-sbt:11.0.13_1.5.5_2.13.7 as play

WORKDIR /squeng/squawg

COPY beuawg/app ./app
COPY beuawg/conf ./conf
COPY beuawg/project ./project
COPY beuawg/public ./public
COPY beuawg/reinraum ./reinraum
COPY beuawg/build.sbt ./
COPY --from=react /squeng/squawg/build ./public/build
RUN sbt stage


FROM openjdk:11-jre

WORKDIR /squeng/squawg

COPY --from=play /squeng/squawg/target/universal/stage ./target/universal/stage

RUN groupadd -r gruppe && useradd --no-log-init -r -g gruppe benutzer
USER benutzer

EXPOSE 8080
EXPOSE 8484
CMD ["target/universal/stage/bin/squawg", "-Dpidfile.path=play.pid", "-Dhttp.port=8080", "-Dhttps.port=8484"]

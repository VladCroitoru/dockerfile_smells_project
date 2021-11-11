FROM gcr.io/cloud-builders/yarn AS yarn
ADD website/package.json website/package.json
ADD pgn-viewer pgn-viewer

WORKDIR website

RUN yarn

WORKDIR /
ADD . .

WORKDIR website

RUN ["yarn", "build"]


FROM gcr.io/cloud-builders/gsutil
WORKDIR app

COPY --from=yarn /website/build /app

ENTRYPOINT ["/bin/bash", "-c"]

FROM ghcr.io/charlieegan3/racket-gregor:latest as build

WORKDIR /app

COPY . .

RUN make update_status
RUN make update_readme


FROM scratch
WORKDIR /
COPY --from=build /app/README.md .

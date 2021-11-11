FROM golang as builder

COPY items /items
RUN ls /items
RUN go build -o /items/items /items/main.go

FROM python:3.9-slim
ENV DOCKER=1

RUN apt-get update && apt-get install -y curl git && mkdir /files

RUN mkdir -p /usr/local/share/keyrings && \
    curl -o /usr/local/share/keyrings/packsquash.key https://comunidadaylas.github.io/PackSquash-apt-repo/public.key && \
    echo 'deb [signed-by=/usr/local/share/keyrings/packsquash.key] https://comunidadaylas.github.io/PackSquash-apt-repo/debian stable main' > /etc/apt/sources.list.d/packsquash.list && \
    apt-get update && apt-get install -y packsquash

RUN pip install b2

WORKDIR /files

COPY --from=builder /items/items /usr/bin/items
COPY build.sh /build.sh
COPY packsquash.toml /files/packsquash.toml

VOLUME [ "/pack" ]

CMD [ "/build.sh" ]
FROM rust:1.55.0

WORKDIR /app

COPY . .

RUN cargo build --release

ENV HOST 0.0.0.0
ENV PORT 3000

EXPOSE 3000

CMD [ "/app/target/release/central-api" ]

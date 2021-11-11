FROM lukemathwalker/cargo-chef:latest-rust-1.54.0 as chef
WORKDIR /app

# Compute lock-file
FROM chef as planner
COPY . .
RUN cargo chef prepare --recipe-path recipe.json

# Builder stage
FROM chef AS builder
COPY --from=planner /app/recipe.json recipe.json
# Build project dependencies only
RUN cargo chef cook --release --recipe-path recipe.json
# Build application
COPY . .
ENV SQLX_OFFLINE true
RUN cargo build --release --bin zero2prod

# Runtime stage
FROM debian:bullseye-slim AS runtime
WORKDIR /app
# Install OpenSSL - it is dynamically linked by some of our dependencies
RUN apt-get update -y \
	&& apt-get install -y --no-install-recommends openssl \
	# Clean up
	&& apt-get autoremove -y \
	&& apt-get clean -y \
	&& rm -rf /var/lib/apt/lists/*
COPY --from=builder /app/target/release/zero2prod zero2prod
COPY configuration configuration
ENV APP_ENVIRONMENT production
ENTRYPOINT ["./zero2prod"]

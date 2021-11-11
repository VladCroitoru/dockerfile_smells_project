FROM node:12 as builder

# Add tini to act as PID1 for proper signal handling
ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# Build the app
WORKDIR /app
COPY package.json package-lock.json ./
ENV NODE_ENV production
RUN npm ci
COPY . .

# Build runtime
FROM gcr.io/distroless/nodejs:12 as runtime

# Add tini from build stage
COPY --from=builder /tini /tini
ENTRYPOINT ["/tini", "--", "/nodejs/bin/node"]

# Copy the app from build stage
COPY --from=builder /app /app
WORKDIR /app

ENV NODE_ENV production
ENV DEBUG trifid:*

# Run as non-privileged, user "nobody"
USER 65534

# Expose the HTTP service under the unprivileged (>1024) http-alt port
EXPOSE 8080

CMD ["./node_modules/.bin/trifid", "--config", "config.json"]

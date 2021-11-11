FROM alpine:3.6
RUN apk add --no-cache cargo rust git docker

# Compiling the proxy
RUN mkdir -p /home/rust
COPY proxy /home/rust/
RUN cargo install --path=/home/rust
RUN rm -rf /home/rust

# Prepare the git repository
RUN mkdir -p /var/git && \
    git init --bare /var/git && \
    git config --global --bool http.receivepack true
COPY hook /var/git/hooks
RUN mv /var/git/hooks/hook /var/git/hooks/update
VOLUME ["/var/git"]

# Compiling the hook binary
RUN mkdir -p /home/rust
COPY hook-bin /home/rust/
RUN cargo install --path=/home/rust
RUN rm -rf /home/rust


EXPOSE 80
HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost/ || exit 1
ENV PATH=/root/.cargo/bin:/usr/local/musl/bin:/usr/local/bin:/usr/bin:/bin
ENTRYPOINT proxy

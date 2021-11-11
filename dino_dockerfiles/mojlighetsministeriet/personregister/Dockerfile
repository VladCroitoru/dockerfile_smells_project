# Run the build
FROM ekidd/rust-musl-builder
COPY . /home/rust/src
RUN cargo build --release

# Create the final docker image
FROM scratch
COPY --from=0 /personregister /
ENTRYPOINT ["/personregister"]

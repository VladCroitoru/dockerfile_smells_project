FROM mqsohdockerfiles/rust AS big-image
COPY ./med /build
RUN cd /build && /root/.cargo/bin/cargo build --release

FROM debian:stretch
COPY --from=big-image /build/target/release/med /bin/
ADD ./med/foo.txt /

CMD [ "med" ]

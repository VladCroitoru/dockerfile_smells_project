FROM scorpil/rust:beta
MAINTAINER Matthew Bentley "bentley@case.edu"

ENV USER "Matthew Bentley"

RUN apt update && apt install -y libssl-dev openssl pkg-config

RUN mkdir /hackcwru/
ADD . /hackcwru/
WORKDIR /hackcwru/

RUN cargo build --release

CMD ["/hackcwru/target/release/hackcwru"]

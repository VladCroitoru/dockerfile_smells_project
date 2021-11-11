FROM fedora:latest

RUN dnf -y update && dnf clean all
RUN dnf -y install npm bzip2 glibc-devel glibc-headers glibc-static gcc cpp sqlite-devel  && dnf clean all

EXPOSE 5000
ENV FLASK_APP powergrid
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV DATABASE="/data/powergrid.db"
RUN mkdir /data && chmod a+rwx /data
VOLUME ["/data"]

WORKDIR /srv

ADD package.json /srv/
RUN npm install &&             \
    npm prune &&               \
    npm cache clean --force && \
    rm -rf ~/.npm

ENV RUSTUP_HOME=/rust
ENV CARGO_HOME=/cargo
ENV ROCKET_ENV="production"
ENV PATH=/cargo/bin:/rust/bin:$PATH

RUN curl -sSf https://sh.rustup.rs \
   | sh -s -- -y --default-toolchain nightly

RUN cargo -V

ADD . /srv/

RUN cargo build --release

RUN npm run build            && \
    rm -rf /srv/build        && \
    rm -rf /srv/config       && \
    rm -rf /srv/node_modules

CMD ["/srv/run.sh"]

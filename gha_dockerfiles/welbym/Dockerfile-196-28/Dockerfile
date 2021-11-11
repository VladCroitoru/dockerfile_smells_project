# pull from the Alpine linux docker image
FROM alpine:latest

# set the user env variable
ENV USER='grader'

# update and upgrade the Alpine package manager
RUN apk update
RUN apk upgrade 

# install Rust and Cargo
RUN apk add --no-cache rust cargo

# Install python3 and pip
RUN apk add --no-cache python3 py3-pip

# create a project to grade rust assignments
# when grading, copy source files to this folder
RUN cargo new /home/dummy_project

# add grading script
ADD rust_196_test /home/rust_196_test
RUN pip3 install -r /home/rust_196_test/requirements.txt

# add any required dependencies for grading to Cargo.toml
# run cargo build to compile required dependencies
# when the student source files are copied over, the binaries will already be built
# source: https://stackoverflow.com/a/42139535
ADD Cargo.toml /home/dummy_project/Cargo.toml
RUN cd /home/dummy_project && cargo build && cargo check
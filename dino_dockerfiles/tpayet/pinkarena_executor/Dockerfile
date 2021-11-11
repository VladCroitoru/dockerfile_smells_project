FROM debian:jessie

RUN	apt-get update -qq && \
	apt-get install -y unzip \
	curl \
	# C/C++
	build-essential \
	# PYTHON
	python3 \
	python-pip \
	python-dev \
	# NODE
	nodejs \
	# RUBY
	ruby-full \
	#  GO
	golang-go

# RUST
RUN mkdir -p /opt/rust && \
    curl https://sh.rustup.rs -sSf | HOME=/opt/rust sh -s -- --no-modify-path -y && \
    chmod -R 777 /opt/rust
ENV	USER executor
ENV PATH "/opt/rust/.cargo/bin:${PATH}"
# Fix "error: no default toolchain configured"
RUN rustup install stable
RUN rustup default stable

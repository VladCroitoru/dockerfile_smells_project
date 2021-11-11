FROM commiebstrd/afl-rs-docker:pacman
MAINTAINER Spenser Reinhardt <spenserreinhardt@gmail.com>

# update system
RUN pacman -Sy --noconfirm && \
	pacman -S --noconfirm archlinux-keyring && \
	pacman -S --noconfirm pacman && \
	pacman-db-upgrade && \
	pacman -Syu --noconfirm && \
	pacman -S --noconfirm wget curl vim git base-devel openssl python2 python cmake llvm clang

# move to opt, build and store files in place
WORKDIR /opt

# clone repos and download afl
RUN git clone https://github.com/rust-lang/rust.git && \
	git clone https://github.com/rust-lang/cargo && \
	wget http://lcamtuf.coredump.cx/afl/releases/afl-$VERSION.tgz

# build rust
RUN cd rust && \
	./configure --enable-clang --disable-libcpp --enable-optimize --disable-docs && \
	make -j 2 && \
	cd .. && \
	echo 'export PATH=$PATH:/opt/rust/x86_64-unknown-linux-gnu/stage2/bin' >> /root/.bashrc && \
	echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/rust/x86_64-unknown-linux-gnu/stage2/lib/' >> /root/.bashrc

# build cargo
RUN	cd cargo && \
	./configure --local-rust-root=/opt/rust/x86_64-unknown-linux-gnu/stage2/ --enable-optimize && \
	make && \
	echo 'export PATH=$PATH:/opt/cargo/target/x86_64-unknown-linux-gnu/release' >> /root/.bashrc

# build afl
RUN VERSION=1.96b && \
	tar xf afl-$VERSION.tgz && \
	cd afl-$VERSION && \
	make && \
	make install

# set user for cargo and path for everything else
ENV USER root
ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/cargo/target/x86_64-unknown-linux-gnu/release:/opt/cargo/target/x86_64-unknown-linux-gnu/release:/opt/afl-1.96b

# return to root and sh
WORKDIR /root/
ENTRYPOINT ["/usr/bin/bash"]

# To build and properly execute this container:
#
# docker build --force-rm --rm=true -t arch-rust-afl .
# echo core > /proc/sys/kernel/core_pattern
# cd /sys/devices/system/cpu
# echo performance | tee cpu*/cpufreq/scaling_governor

# compilation instructions
#
# add deps and features for afl to cargo.toml
# add to main/lib.rs
# cargo rustc --verbose --features fuzz -- -Z no-landing-pads

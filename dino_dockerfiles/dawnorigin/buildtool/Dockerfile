FROM mizzy/centos-4.8-i386

RUN yum -y install \
	tar \
	unzip \
	wget \
	curl \
	git \
	bzip2 \
	file \
	procps \
	pkgconfig \
	make \
	gcc \
	autoconf \
	gettext \
	automake \
	automake16 \
	automake17 \
	automake14 \
	automake15 \
	gcc-c++ \
	gdb \
	libtool \
	rpm-build \
	strace \
	pstack \
	binutils \
	diffstat \
	bison \
	flex \
	cdecl \
	splint \
	indent \
	ctags \
	cscope \
	patchutils \
	texinfo \
	elfutils \
	elfutils-libelf \
	oprofile\ 
	doxygen \
	cproto \
	kernel-devel \
	kernel-smp-devel \
	kernel-hugemem-devel \
	perl-XML-SAX \
	perl-XML-Parser \
	perl-XML-Dumper \
	perl-XML-Twig \
	perl-LDAP \
	perl-XML-LibXML \
	perl-XML-LibXML-Common \
	perl-XML-Grove \
	perl-XML-Encoding \
	perl-Crypt-SSLeay \
	perl-XML-NamespaceSupport \
	perl-TimeDate \
	dmalloc \
	ElectricFence \
	valgrind \
	valgrind-callgrind \
	elfutils-devel \
	glibc-devel \
	bzip2-devel \
	python-devel \
	curl-devel \
	rpm-devel \
	zlib-devel \
	libusb-devel \
	libxml2-devel \
	pam-devel \
	pcre-devel \
	pciutils-devel \
	sqlite-devel \
	readline-devel \
	gdbm-devel \
	ncurses-devel \
	libdbi-devel \
# clean up
	&& rm -rf /var/cache/yum/* \
	&& yum clean all

# Install openssl
RUN set -ex \
	&& cd /tmp \
	&& wget --no-check-certificate https://www.openssl.org/source/openssl-1.0.2l.tar.gz \
	&& tar xzf openssl-1.0.2l.tar.gz \
	&& cd openssl-1.0.2l \
	&& ./Configure linux-generic32 --prefix=/usr \
	&& make \
	&& make install \
	&& cd .. \
	&& rm -rf openssl-1.0.2l* \
# Install python 2.7
	&& wget --no-check-certificate https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz \
	&& tar xzf Python-2.7.13.tgz \
	&& cd Python-2.7.13 \
	&& ./configure --prefix=/usr/local \
	&& make \
	&& make altinstall \
	&& ln -sf /usr/local/bin/python2.7 /usr/bin/python \
	&& ln -sf /usr/bin/python2.3 /usr/bin/python2 \
	&& sed -i "s/#\!\/usr\/bin\/python/#\!\/usr\/bin\/python2/" /usr/bin/yum \
	&& cd .. \
	&& rm -rf Python* \

CMD ["/bin/bash"]

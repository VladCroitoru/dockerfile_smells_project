FROM fedora:32

EXPOSE 5222
VOLUME ["/etc/spectrum2/transports", "/var/lib/spectrum2"]
ARG commit=unknown
RUN echo $commit

COPY . spectrum2

RUN echo "---> Installing swiften" && \
		dnf install -y avahi-devel boost-devel expat-devel gcc-c++ git libidn-devel libnatpmp-devel libxml2-devel miniupnpc-devel openssl-devel python3-scons && \
		git clone git://swift.im/swift && \
		cd swift && \
		scons Swiften swiften_dll=1 SWIFTEN_INSTALLDIR=/usr SWIFTEN_LIBDIR=/usr/lib64 /usr && \
		cd .. && \
		rm -rf swift

# Spectrum 2
RUN echo "---> Installing Spectrum 2" && \
		dnf install -y cmake cppunit-devel jsoncpp-devel libcommuni-devel libcurl-devel libev-libevent-devel libpqxx-devel libpurple-devel libsqlite3x-devel log4cxx-devel make mysql-devel popt-devel protobuf-devel qt5-qtbase-devel rpm-build && \
		cd spectrum2 && \
		./packaging/fedora/build_rpm.sh && \
		rpm -U /root/rpmbuild/RPMS/x86_64/*.rpm && \
		cp ./packaging/docker/run.sh /run.sh && \
		cd .. && \
		rm -rf spectrum2 && \
		rm -rf ~/rpmbuild

RUN dnf install -y purple-discord purple-facebook purple-hangouts purple-libsteam purple-skypeweb purple-telegram

RUN echo "---> Installing purple-instagram" && \
		dnf install json-glib-devel -y && \
		git clone https://github.com/EionRobb/purple-instagram.git && \
		cd purple-instagram && \
		make && \
		make install && \
		cd .. && \
		rm -rf purple-instagram
RUN echo "---> Installing icyque" && \
		git clone git://github.com/EionRobb/icyque.git && \
		cd icyque && \
		make && \
		make install && \
		cd .. && \
		rm -rf icyque
RUN echo "---> Installing transwhat" && \
		dnf install -y python-unversioned-command python3-appdirs python3-cffi python3-devel python3-pip python3-pycparser && \
		pip3 install --pre consonance==0.1.2 python-axolotl==0.2.2 six==1.10 &&\
		git clone git://github.com/stv0g/transwhat.git &&\
		cd transwhat &&\
		git checkout yowsup-3 &&\
		python setup.py install &&\
		cd .. &&\
		rm -r transwhat
RUN echo "---> purple-gowhatsapp" && \
		dnf install -y golang && \
		git clone https://github.com/hoehermann/purple-gowhatsapp && \
		cd purple-gowhatsapp && \
		make && \
		make install && \
		cd .. && \
		rm -rf purple-gowhatsapp
RUN echo "---> cleanup" && \
		dnf remove -y \
			avahi-devel boost-devel expat-devel gcc-c++ git libidn-devel libnatpmp-devel libxml2-devel miniupnpc-devel openssl-devel python3-scons \
			cmake cppunit-devel jsoncpp-devel libcommuni-devel libcurl-devel libev-libevent-devel libpqxx-devel libpurple-devel libsqlite3x-devel log4cxx-devel make mysql-devel popt-devel protobuf-devel qt5-qtbase-devel rpm-build spectrum2-debuginfo \
			json-glib-devel \
			python3-devel python3-pip \
			golang && \
		rm -rf /usr/share/locale/* && \
		rm -rf /usr/share/doc/* && \
		rm -rf /usr/share/icons/* && \
		rm -rf /usr/share/cracklib* && \
		rm -rf /usr/share/hwdata* && \
		rm -rf /usr/lib64/libQtGui* && \
		rm -rf /usr/lib64/libQtSvg* && \
		rm -rf /usr/lib64/libQtDeclarative* && \
		rm -rf /usr/lib64/libQtOpenGL* && \
		rm -rf /usr/lib64/libQtScriptTools* && \
		rm -rf /usr/lib64/libQtMultimedia* && \
		rm -rf /usr/lib64/libQtHelp* && \
		rm -rf /usr/lib64/libQtDesigner* && \
		rm -rf /usr/lib64/libQt3* && \
		rm -rf /usr/include && \
		dnf clean all -y && \
		rm -rf /var/lib/rpm/*

CMD "/run.sh"

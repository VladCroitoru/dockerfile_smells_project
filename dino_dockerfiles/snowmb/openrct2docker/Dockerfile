
FROM openrct2/openrct2:ubuntu_amd64

EXPOSE 11753

ADD ./ca-certificates.crt /etc/ssl/certs/ca-certificates.crt

RUN 	mkdir -p /openrct2/config /openrct2/original_files \
	&& git clone https://github.com/OpenRCT2/OpenRCT2.git /openrct2/src \
	&& mkdir /openrct2/src/build \
	&& cmake -B/openrct2/src/build -H/openrct2/src \
	&& make -C /openrct2/src/build \
	&& make -C /openrct2/src/build g2 \
	&& ln -s /openrct2/src/data /openrct2/src/build/data \
	&& ln -s /openrct2/src/build/g2.dat /openrct2/src/data/g2.dat


ADD ./docker-entrypoint.sh docker-entrypoint.sh

CMD ./docker-entrypoint.sh

FROM debian:latest

RUN apt-get update && apt-get install -y \    
		build-essential \
		python \
		curl \
		unzip \
    && rm -rf /var/lib/apt/lists/*

# Build BAM Compiler
ENV BAM_PATH					/usr/local/bam-src
ENV BAM_VERSION					0.4.0
ENV BAM_DOWNLOAD_URL			http://github.com/downloads/matricks/bam/bam-${BAM_VERSION}.tar.gz
ENV BAM_DOWNLOAD_SHA256			5e4e4920b4d265da582f66774e9b1ec8ddfbe75ddc028fba86c12f686ea18db3

RUN curl -fsSL "${BAM_DOWNLOAD_URL}" -o bam.tar.gz \
    && echo "${BAM_DOWNLOAD_SHA256}  bam.tar.gz" | sha256sum -c - \
    && mkdir -p ${BAM_PATH} \
    && tar -C ${BAM_PATH} -zxf bam.tar.gz \
    && rm bam.tar.gz

RUN cd ${BAM_PATH}/bam-${BAM_VERSION} && \
	./make_unix.sh && \
	ln -nfs ${BAM_PATH}/bam-${BAM_VERSION}/bam /usr/local/bin/bam

# Build Teeworlds base server
ENV TEEWORLDS_PATH               /usr/local/teeworlds-src
ENV TEEWORLDS_VERSION            0.6.4
ENV TEEWORLDS_DOWNLOAD_URL       https://github.com/teeworlds/teeworlds/archive/${TEEWORLDS_VERSION}-release.tar.gz
ENV TEEWORLDS_DOWNLOAD_SHA256    831afdea9e343cd712382c74b941c6c14adfb9192d32504022b41c2abbb910d7

RUN curl -fsSL "${TEEWORLDS_DOWNLOAD_URL}" -o teeworlds.tar.gz \
    && echo "${TEEWORLDS_DOWNLOAD_SHA256}  teeworlds.tar.gz" | sha256sum -c - \
    && mkdir -p ${TEEWORLDS_PATH} \
    && tar -C ${TEEWORLDS_PATH} -zxf teeworlds.tar.gz \
    && rm teeworlds.tar.gz

RUN cd ${TEEWORLDS_PATH}/teeworlds-${TEEWORLDS_VERSION}-release && \
	bam server_release && \
	ln -nfs ${TEEWORLDS_PATH}/teeworlds-${TEEWORLDS_VERSION}-release /usr/local/bin/teeworlds

# Build Teeworlds Basket base server
ENV TEEWORLDS_BASKET_PATH               /usr/local/teeworlds-basket-src
ENV TEEWORLDS_BASKET_VERSION            4.3
ENV TEEWORLDS_BASKET_DOWNLOAD_URL       http://duneudne.free.fr/source/gamer${TEEWORLDS_BASKET_VERSION}_src.zip
ENV TEEWORLDS_BASKET_DOWNLOAD_SHA256    596c2622652264ac1038f260344410bc15843e60615178f16b17d718aee617df

RUN curl -fsSL "${TEEWORLDS_BASKET_DOWNLOAD_URL}" -o teeworlds-basket.zip \
    && echo "${TEEWORLDS_BASKET_DOWNLOAD_SHA256}  teeworlds-basket.zip" | sha256sum -c - \
    && mkdir -p ${TEEWORLDS_BASKET_PATH} \
    && unzip teeworlds-basket.zip -d ${TEEWORLDS_BASKET_PATH} \
    && rm teeworlds-basket.zip

#RUN cd ${TEEWORLDS_BASKET_PATH} && \
#	bam server_release && \
#	ln -nfs ${TEEWORLDS_BASKET_PATH}/gamer${TEEWORLDS_BASKET_VERSION}_src /usr/local/bin/teeworlds_basket

EXPOSE 8303

VOLUME ["/usr/local/teeworlds/serverconfig.cfg"]

CMD ["/usr/local/bin/teeworlds/teeworlds_srv", "-f", "/usr/local/teeworlds/serverconfig.cfg"]

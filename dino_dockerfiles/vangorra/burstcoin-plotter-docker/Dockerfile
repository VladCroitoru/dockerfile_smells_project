FROM alpine:3.7

RUN apk --no-cache add --virtual=build-dependencies git make gcc g++ && \
	git clone https://github.com/PoC-Consortium/cg_obup /usr/src/cg_obup && \
	cd /usr/src/cg_obup && \
	git reset --hard 177015beb923a4e6afb47a816a5490e326e5af84 && \
	make && \
        cd / && \
	mv /usr/src/cg_obup/plot64 /usr/local/bin && \
	rm -rf /usr/src/cg_obup && \
	apk del --purge build-dependencies

WORKDIR /plots

ENTRYPOINT ["/usr/local/bin/plot64"]

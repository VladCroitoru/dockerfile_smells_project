FROM drydock/u14jav:prod

COPY * /

RUN	java "-Dcom.adobe.systemIdsForWhichTheTermsOfTheAdobeLicenseAgreementAreAccepted=$(java IdHelper)" -jar apache-flex-sdk-converter-151126.jar -flexVersion 4.16.0 -flashVersions 11.0 -airVersion 2.6 -platforms LINUX -fontkit -fdkDir /flex-sdk-4.16.0 -mavenDir ~/.m2/repository download convert && \
	rm -rf /flex-sdk-4.16.0 IdHelper apache-flex-sdk-converter.jar

RUN	apt-get update && \
	apt-get install -y postgresql-9.3 postgresql-contrib-9.3 postgresql-9.3-postgis-2.1 && \
	echo "host all all localhost trust" > /etc/postgresql/9.3/main/pg_hba.conf && \
	echo "local all all trust" >> /etc/postgresql/9.3/main/pg_hba.conf && \
	service postgresql start && \
	psql -v ON_ERROR_STOP=1 -c 'create database projectx;' -U postgres && \
	psql -v ON_ERROR_STOP=1 -c 'create schema "publicsample";' -U postgres projectx

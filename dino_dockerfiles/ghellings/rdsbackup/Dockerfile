FROM perl:5.22.1-threaded

COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
RUN \
	apt-get install libxml2-dev libssl-dev && \
	cpan Carton && \
	carton install
	
RUN carton install && \
	ls ./t -1 | xargs -i bash -c 'echo "Testing {}" && carton exec t/{}'


ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""

ENTRYPOINT ["carton", "exec", "script/snap"]


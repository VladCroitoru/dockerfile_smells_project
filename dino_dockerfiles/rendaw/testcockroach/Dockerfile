from golang:1.10.2 as build
run apt-get update && apt-get -y upgrade
run apt-get install -y build-essential
run apt-get install -y git
run apt-get install -y cmake
run apt-get install -y autoconf
run apt-get install -y libncurses-dev
run curl -sL https://deb.nodesource.com/setup_10.x | bash - && apt-get install -y nodejs
run npm install -g yarn
run (\
	git clone --recurse-submodules https://github.com/cockroachdb/cockroach.git /go/src/github.com/cockroachdb/cockroach && \
	cd /go/src/github.com/cockroachdb/cockroach && \
	git checkout v2.0.2 && \
	make bin/.bootstrap && \
	cp bin/* $(GOPATH)/bin && \
	go-bindata -version && \
	sed -i 's/6.7.3/6.8.6","espree":"","escodegen":"","estraverse":"/g' pkg/ui/package.json && \
	grep 6.8.6 pkg/ui/package.json && \
	make buildoss\
	)
add . /go/src/github.com/micromicromicro/testcockroach
run (cd /go/src/github.com/micromicromicro/testcockroach && go install)
from golang:1.10.2
copy --from=build /go/bin/testcockroach .
copy --from=build /go/src/github.com/cockroachdb/cockroach/cockroach .
cmd ./testcockroach
entrypoint []
expose 8080
expose 26257
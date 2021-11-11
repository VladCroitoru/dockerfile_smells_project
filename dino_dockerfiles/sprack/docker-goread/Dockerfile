FROM ubuntu

ENV PATH=$PATH:/work/go_appengine:/usr/local/go/bin GOPATH=/work

RUN mkdir -p /work/goread && \
		apt-get update -y && \
		apt-get install -y python git mercurial unzip curl nginx  && \
		curl -s https://storage.googleapis.com/appengine-sdks/featured/go_appengine_sdk_linux_amd64-1.9.48.zip -o /work/go_appengine_sdk_linux_amd64-1.9.48.zip && \
		unzip /work/go_appengine_sdk_linux_amd64-1.9.48.zip -d /work/ && \
		curl -s https://storage.googleapis.com/golang/go1.8.1.linux-amd64.tar.gz -o /work/go1.8.1.linux-amd64.tar.gz && \
		tar zxf /work/go1.8.1.linux-amd64.tar.gz -C /usr/local/ && \
		rm -f /work/go_appengine_sdk_linux_amd64-1.9.48.zip /work/go1.8.1.linux-amd64.tar.gz && \
		goapp get -d github.com/mjibson/goread && \
		cd $GOPATH/src/github.com/mjibson/goread/ && \
		cp settings.go.dist settings.go && \
		cd $GOPATH/src/github.com/mjibson/goread/app/ && \
		cp app.sample.yaml app.yaml

EXPOSE 8080 8000
WORKDIR $GOPATH/src/github.com/mjibson/goread/app/
ENTRYPOINT /work/go_appengine/dev_appserver.py --skip_sdk_update_check --host 0.0.0.0 --admin_host 0.0.0.0 --storage_path /work/goread app.yaml

FROM node:alpine

LABEL maintainer "https://github.com/blacktop"

ENV MATTERMOST="v4.4.0"
ENV GOLANG_VERSION="1.9.2"

ENV TERM=screen-256color

# Setup Language Environtment
ENV LANG="C.UTF-8"
ENV LC_COLLATE="C.UTF-8"
ENV LC_CTYPE="C.UTF-8"
ENV LC_MESSAGES="C.UTF-8"
ENV LC_MONETARY="C.UTF-8"
ENV LC_NUMERIC="C.UTF-8"
ENV LC_TIME="C.UTF-8"

RUN apk add --no-cache vim git zsh make sed ca-certificates

####################
## INSTALL GOLANG ##
####################
COPY *.patch /go-alpine-patches/
RUN set -eux; \
	apk add --no-cache --virtual .build-deps \
		bash \
		gcc \
		musl-dev \
		openssl \
		go \
	; \
	export \
# set GOROOT_BOOTSTRAP such that we can actually build Go
		GOROOT_BOOTSTRAP="$(go env GOROOT)" \
# ... and set "cross-building" related vars to the installed system's values so that we create a build targeting the proper arch
# (for example, if our build host is GOARCH=amd64, but our build env/image is GOARCH=386, our build needs GOARCH=386)
		GOOS="$(go env GOOS)" \
		GOARCH="$(go env GOARCH)" \
		GO386="$(go env GO386)" \
		GOARM="$(go env GOARM)" \
		GOHOSTOS="$(go env GOHOSTOS)" \
		GOHOSTARCH="$(go env GOHOSTARCH)" \
	; \
	\
	wget -O go.tgz "https://golang.org/dl/go$GOLANG_VERSION.src.tar.gz"; \
	echo '665f184bf8ac89986cfd5a4460736976f60b57df6b320ad71ad4cef53bb143dc *go.tgz' | sha256sum -c -; \
	tar -C /usr/local -xzf go.tgz; \
	rm go.tgz; \
	\
	cd /usr/local/go/src; \
	for p in /go-alpine-patches/*.patch; do \
		[ -f "$p" ] || continue; \
		patch -p2 -i "$p"; \
	done; \
	./make.bash; \
	\
	rm -rf /go-alpine-patches; \
	apk del .build-deps; \
	\
	export PATH="/usr/local/go/bin:$PATH"; \
	go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH

RUN git clone -b $MATTERMOST https://github.com/mattermost/mattermost-server.git /go/src/github.com/mattermost/mattermost-server \
  && cd /go/src/github.com/mattermost/mattermost-server \
  && make build-linux

# Install mattermost-webapp
RUN apk add --no-cache --virtual .build-deps git build-base python libpng-dev \
  && git clone -b $MATTERMOST https://github.com/mattermost/mattermost-webapp.git /go/src/github.com/mattermost/mattermost-webapp \
  && cd /go/src/github.com/mattermost/mattermost-webapp \
  && sed -i "24i DEV = true;" webpack.config.js \
  && sed -i "25i FULLMAP = true;" webpack.config.js \
  && make build || true \
  && apk del .build-deps

# Install vim plugins
RUN git clone https://github.com/fatih/vim-go.git ~/.vim/pack/plugins/start/vim-go
RUN git clone https://github.com/scrooloose/nerdtree.git ~/.vim/pack/plugins/start/nerdtree
RUN git clone https://github.com/pangloss/vim-javascript.git ~/.vim/pack/plugins/start/vim-javascript
RUN git clone https://github.com/mxw/vim-jsx.git ~/.vim/pack/plugins/start/vim-jsx
RUN git clone https://github.com/mattn/emmet-vim.git ~/.vim/pack/plugins/start/emmet-vim
RUN git clone https://github.com/w0rp/ale.git ~/.vim/pack/plugins/start/ale
RUN git clone https://github.com/skywind3000/asyncrun.vim.git ~/.vim/pack/plugins/start/asyncrun.vim
RUN git clone https://github.com/leshill/vim-json.git ~/.vim/pack/plugins/start/vim-json
RUN git clone https://github.com/itchyny/lightline.vim ~/.vim/pack/plugins/start/lightline.vim
RUN git clone https://github.com/jacoborus/tender.vim.git ~/.vim/pack/plugins/start/tender \
  && mkdir -p ~/.vim/colors \
  && cp ~/.vim/pack/plugins/start/tender/colors/tender.vim ~/.vim/colors/tender.vim
# Install vim plugins deps
RUN yarn add --dev eslint babel-eslint eslint-plugin-react
RUN yarn add --dev prettier eslint-config-prettier eslint-plugin-prettier

# Install oh-my-zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh

COPY vimrc /root/.vimrc
COPY zshrc /root/.zshrc

WORKDIR /go/src/github.com/mattermost/mattermost-server

ENTRYPOINT ["zsh"]

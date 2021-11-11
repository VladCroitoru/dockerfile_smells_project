FROM golang:1.16-buster as builder

RUN echo "deb http://deb.debian.org/debian buster-backports main" > /etc/apt/sources.list.d/backports.list \
    && echo "deb http://deb.debian.org/debian bullseye main" > /etc/apt/sources.list.d/bullseye.list \
    && apt-get update -qq \
    && apt-get install -y git/buster-backports tig/bullseye vim less bash sudo \
    && apt-get install -y fontconfig fonts-noto-cjk \
    && fc-cache -fv \
    ;

#ENV USER=app \
ENV USER=root \
    GO111MODULE=on \
    EDITOR=vim \
    LANG=C.UTF-8

#RUN addgroup wheel \
#    && echo "auth sufficient pam_wheel.so trust group=wheel" >> /etc/pam.d/su \
#    && echo "%wheel ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers \
#    && useradd -s /bin/bash -m -G wheel $USER \
#    ;

USER $USER

#ENV HOME=/home/$USER
ENV HOME=/$USER

RUN curl -fsSL https://raw.github.com/git/git/master/contrib/completion/git-completion.bash -o ~/.git-completion.bash \
    && curl -fsSL https://raw.github.com/git/git/master/contrib/completion/git-prompt.sh -o ~/.git-prompt.sh \
    && chmod a+x ~/.git-* \
    ;

WORKDIR /opt/app/src

RUN go get golang.org/x/tools/gopls@latest \
    && go get -u github.com/ramya-rao-a/go-outline \
    && go install github.com/go-delve/delve/cmd/dlv@master \
    && mv $GOPATH/bin/dlv $GOPATH/bin/dlv-dap \
    ;

COPY --chown=$USER:$USER src ./

RUN go mod download

RUN go build -o /go/bin/app

COPY --chown=$USER:$USER Makefile .editorconfig ../
COPY --chown=$USER:$USER .bashrc .vimrc $HOME/

# multi stage build for slim
FROM gcr.io/distroless/base-debian10:latest as prod

COPY --from=builder /go/bin/app /go/bin/app

ENTRYPOINT ["/go/bin/app"]

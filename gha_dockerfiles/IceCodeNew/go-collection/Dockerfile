FROM quay.io/icecodenew/go-collection:build_base AS github-release
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/github-release/github-release/releases/latest
ARG github_release_latest_tag_name='v0.9.0'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/github-release/github-release \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS nfpm
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/goreleaser/nfpm/commits?per_page=1
ARG nfpm_latest_commit_hash='4a81c34939f8dd4a287bc378858dea70ca8e1b35'
WORKDIR '/go/src/nfpm'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && git_clone 'https://github.com/goreleaser/nfpm.git' '/go/src/nfpm' \
    && go mod download \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/nfpm -v cmd/nfpm/main.go \
    && strip "/go/bin"/* \
    && /go/bin/nfpm --version \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS mmp-go
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/Qv2ray/mmp-go/commits?per_page=1
ARG mmp_go_latest_commit_hash='92ace24d84b98c00a219d1eeb3c602466b9a5c4a'
WORKDIR '/go/src/mmp-go'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && git_clone 'https://github.com/Qv2ray/mmp-go.git' '/go/src/mmp-go' \
    && go build -trimpath -ldflags="-linkmode=external -X 'github.com/Qv2ray/mmp-go/config.Version=$(git describe --tags --long --always)' -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/mmp-go -v . \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS caddy
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/caddyserver/caddy/commits?per_page=1
ARG CADDY_VERSION='b6e96d6f4a55f96ccbb69f112822f0a923942246'
# https://api.github.com/repos/caddy-dns/cloudflare/commits?per_page=1
ARG caddydns_cloudflare_latest_commit_hash='eda8e5aa22232e9c279b0df7531f20c331b331c6'
# https://api.github.com/repos/caddyserver/jsonc-adapter/commits?per_page=1
ARG caddy_jsoncadapter_latest_commit_hash='825ee096306c2af9a28858f0db87fb982795cbea'
# https://api.github.com/repos/caddyserver/nginx-adapter/commits?per_page=1
ARG caddy_nginxadapter_latest_commit_hash='77eae3ff99cb283fd474a9a59f7b652de3d6b61d'
# https://api.github.com/repos/porech/caddy-maxmind-geolocation/commits?per_page=1
ARG caddy_geoip_latest_commit_hash='d500cc3ca64b734da42e0f0446003f437c915ac8'
# https://api.github.com/repos/mastercactapus/caddy2-proxyprotocol/commits?per_page=1
ARG caddy_proxyprotocol_latest_commit_hash='8cd17723e0ed50a258a2f8b498155cd9a5ece941'
# https://api.github.com/repos/mholt/caddy-l4/commits?per_page=1
ARG caddy_l4_latest_commit_hash='bf3444c4665a1d7e0df58c2f4e9fbafc2aa1ed29'
# https://api.github.com/repos/klzgrad/forwardproxy/commits?per_page=1&sha=naive
ARG caddy_naiveproxy_latest_commit_hash='ff60d3bb5ad18a21551acbe20419cb88e70f198e'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/caddyserver/xcaddy/cmd/xcaddy \
    && "/go/bin/xcaddy" build --output "/go/bin/caddy-with-geoip-proxyproto-l4-naiveproxy" \
    --with github.com/caddy-dns/cloudflare@master \
    --with github.com/caddyserver/jsonc-adapter@master \
    --with github.com/caddyserver/nginx-adapter@master \
    --with github.com/porech/caddy-maxmind-geolocation@master \
    --with github.com/mastercactapus/caddy2-proxyprotocol@master \
    --with github.com/mholt/caddy-l4@master \
    --with github.com/caddyserver/forwardproxy@caddy2=github.com/klzgrad/forwardproxy@naive \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 "/go/bin/xcaddy" build --output "/go/bin/caddy-with-geoip-proxyproto-l4-naiveproxy.exe" \
    --with github.com/caddy-dns/cloudflare@master \
    --with github.com/caddyserver/jsonc-adapter@master \
    --with github.com/caddyserver/nginx-adapter@master \
    --with github.com/porech/caddy-maxmind-geolocation@master \
    --with github.com/mastercactapus/caddy2-proxyprotocol@master \
    --with github.com/mholt/caddy-l4@master \
    --with github.com/caddyserver/forwardproxy@caddy2=github.com/klzgrad/forwardproxy@naive \
    && rm -rf "/go/bin/xcaddy" "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS age
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/FiloSottile/age/commits?per_page=1
ARG age_latest_commit_hash='53f0ebda67901013bddf1a6bd59c946574c87d0b'
WORKDIR '/go/src/age'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/FiloSottile/age.git' '/go/src/age' \
    && go build -trimpath -ldflags="-linkmode=external -X 'main.Version=$(git describe --tags --long --always) ($(go version))' -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/ -v ./cmd/... \
    && strip "/go/bin"/* \
    && mv "/go/bin/age" "/go/bin/age-keygen" ./ \
    && bsdtar --no-xattrs -a -cf /go/bin/age-linux-amd64.tar.gz ./age ./age-keygen
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -X 'main.Version=$(git describe --tags --long --always) ($(go version))' -buildid=" -o /go/bin/ -v ./cmd/... \
    && mv "/go/bin/age.exe" "/go/bin/age-keygen.exe" ./ \
    && bsdtar --no-xattrs -a -cf /go/bin/age-windows-amd64.zip ./age.exe ./age-keygen.exe \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS mtg
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/9seconds/mtg/commits?per_page=1
ARG mtg_latest_commit_hash='e075169dd4e9fc4c2b1453668f85f5099c4fb895'
WORKDIR '/go/src/mtg'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    # && git_clone 'https://github.com/9seconds/mtg.git' --branch 'stable' '/go/src/mtg' \
    && git_clone 'https://github.com/9seconds/mtg.git' '/go/src/mtg' \
    && go build -trimpath -ldflags="-linkmode=external -X 'main.version=$(git describe --tags --long --always) ($(go version)) [$(date -Ru)]' -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/mtg -v . \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS got
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/melbahja/got/releases/latest
ARG got_latest_tag_name='v0.5.0'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/melbahja/got/cmd/got \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS shfmt
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/mvdan/sh/commits?per_page=1&path=go.mod
ARG shfmt_latest_commit_hash='c5ff78f0d68e4067c7218775c2ff4cef6a1d23fc'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -v mvdan.cc/sh/v3/cmd/shfmt \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS croc
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/schollz/croc/commits?per_page=1
ARG croc_latest_commit_hash='0bafce5efe88bbf39f6ec05cb27ae7242478f43b'
WORKDIR '/go/src/croc'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && git_clone 'https://github.com/schollz/croc.git' '/go/src/croc' \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/croc -v . \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -buildid=" -o /go/bin/croc.exe -v . \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS mosdns
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/IrineSistiana/mosdns/commits?per_page=1
ARG mosdns_latest_commit_hash='5ee263d0b686404c93016351076851861a854eb4'
WORKDIR '/go/src/mosdns'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/IrineSistiana/mosdns.git' '/go/src/mosdns' \
    && go build -trimpath -ldflags="-linkmode=external -X main.version=$(git describe --tags --long --always) -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/mosdns -v . \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -X main.version=$(git describe --tags --long --always) -buildid=" -o /go/bin/mosdns.exe -v . \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS go-shadowsocks2
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/shadowsocks/go-shadowsocks2/commits?per_page=1
ARG go_ss2_latest_commit_hash='75d43273f5a50373be2a70e91372a3a6afc53a54'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/shadowsocks/go-shadowsocks2 \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go get -trimpath -ldflags="-s -w -buildid=" -u -v github.com/shadowsocks/go-shadowsocks2 \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS overmind
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/DarthSim/overmind/commits?per_page=1
ARG overmind_latest_commit_hash='e654d50f630d7b44192f3bb22ef0d5889854d110'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/DarthSim/overmind/v2 \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS frp
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/fatedier/frp/commits?per_page=1
ARG frp_latest_commit_hash='72595b2da84f7eaceac735dbe8fd45ff9668d92c'
WORKDIR '/go/src/frp'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && git_clone 'https://github.com/fatedier/frp.git' '/go/src/frp' \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/frpc -v ./cmd/frpc \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/frps -v ./cmd/frps \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -buildid=" -o /go/bin/frpc.exe -v ./cmd/frpc \
    && GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -buildid=" -o /go/bin/frps.exe -v ./cmd/frps \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS nali
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/zu1k/nali/commits?per_page=1&path=go.mod
ARG nali_latest_commit_hash='9b0aa92bd4a677a9e61f27be5e1cce30b8040fc9'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/zu1k/nali \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS dnslookup
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/ameshkov/dnslookup/commits?per_page=1
ARG dnslookup_latest_commit_hash='a20f98f33d92f88c10231536b77e4b8013aeecac'
WORKDIR '/go/src/dnslookup'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go env -w GO111MODULE=on \
    && git_clone 'https://github.com/ameshkov/dnslookup.git' '/go/src/dnslookup' \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/dnslookup -v . \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -buildid=" -o /go/bin/dnslookup.exe -v . \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS wgcf
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/ViRb3/wgcf/commits?per_page=1
ARG wgcf_latest_commit_hash='d3850639fe43559370b9575b35fca0167ac5689d'
WORKDIR '/go/src/wgcf'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/ViRb3/wgcf.git' '/go/src/wgcf' \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/wgcf -v . \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS dive
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/wagoodman/dive/commits?per_page=1
ARG dive_latest_tag_name='v0.10.0'
ARG dive_latest_commit_hash='64880972b0726ec2ff2b005b0cc97801067c1bb5'
WORKDIR '/go/src/dive'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/wagoodman/dive.git' '/go/src/dive' \
    && go build -trimpath -ldflags="-linkmode=external -X main.version=${dive_latest_tag_name} -X 'main.commit=${dive_latest_commit_hash} -X main.buildTime=$(date -u --rfc-3339=seconds)' -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/dive -v . \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS duf
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/muesli/duf/commits?per_page=1&path=go.mod
ARG duf_latest_commit_hash='02161643e0fb8530aa13bfbcfefad79bd8ffdf3c'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/muesli/duf \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS wuzz
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/asciimoo/wuzz/commits?per_page=1
ARG wuzz_latest_commit_hash='0935ebdf55d223abbf0fd10cb8f0f9c0a323ccb7'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/asciimoo/wuzz \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS httpstat
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/davecheney/httpstat/commits?per_page=1
ARG httpstat_latest_commit_hash='48531c3e2d3e4cd51f04c33002898d81d61e0c93'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/davecheney/httpstat \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS chisel
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/jpillora/chisel/commits?per_page=1
ARG chisel_latest_commit_hash='20921074b5827147b1a24d4ef4f5cba174856430'
WORKDIR '/go/src/chisel'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/jpillora/chisel.git' '/go/src/chisel' \
    && go build -trimpath -ldflags="-linkmode=external -X github.com/jpillora/chisel/share.BuildVersion=$(git describe --tags --long --always) -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/chisel -v . \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -X github.com/jpillora/chisel/share.BuildVersion=$(git describe --tags --long --always) -buildid=" -o /go/bin/chisel.exe -v . \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS cloudflarespeedtest
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/XIU2/CloudflareSpeedTest/commits?per_page=1
ARG cloudflarespeedtest_latest_commit_hash='7ece9d6cda56f42c4c44c9c2e39991a318e5731d'
WORKDIR '/go/src/CloudflareSpeedTest'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/XIU2/CloudflareSpeedTest.git' '/go/src/CloudflareSpeedTest' \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/CloudflareST -v . \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go build -trimpath -ldflags="-s -w -buildid=" -o /go/bin/CloudflareST.exe -v . \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS netflix-verify
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/sjlleo/netflix-verify/commits?per_page=1
ARG netflix_verify_latest_commit_hash='8ee2a91086d1e723fb506ca37ae1edfaf044abc5'
WORKDIR '/go/src/netflix-verify'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && git_clone 'https://github.com/sjlleo/netflix-verify.git' '/go/src/netflix-verify' \
    && go mod init \
    && go mod tidy \
    && go build -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -o /go/bin/nf -v . \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS piknik
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/jedisct1/piknik/commits?per_page=1
ARG piknik_latest_commit_hash='00ee34cd9fe6c6c3fca2ba954c93e2a3b129f45c'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/jedisct1/piknik \
    && strip "/go/bin"/*
RUN GOOS=windows GOARCH=amd64 go get -trimpath -ldflags="-s -w -buildid=" -u -v github.com/jedisct1/piknik \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/go-collection:build_base AS apk-file
SHELL ["/bin/bash", "-o", "pipefail", "-c"]
# https://api.github.com/repos/genuinetools/apk-file/releases/latest
ARG apk_file_latest_tag_name='v0.3.6'
RUN source "/root/.bashrc" \
    && go env -w CGO_ENABLED=0 \
    && go get -trimpath -ldflags="-linkmode=external -extldflags '-fuse-ld=lld -Wl,-z,noexecstack,-z,relro,-z,now,-z,defs -Wl,--icf=all -static-pie' -buildid=" -u -v github.com/genuinetools/apk-file \
    && strip "/go/bin"/* \
    && rm -rf "/root/.cache/go-build" "/go/pkg" "/go/src" || exit 0

FROM quay.io/icecodenew/alpine:latest AS collection
SHELL ["/bin/ash", "-eo", "pipefail", "-c"]
# date +%s
# ARG cachebust='1603527789'
ARG TZ='Asia/Taipei'
ENV DEFAULT_TZ ${TZ}
COPY --from=github-release /go/bin /go/bin/
COPY --from=nfpm /go/bin /go/bin/
COPY --from=mmp-go /go/bin /go/bin/
COPY --from=caddy /go/bin /go/bin/
COPY --from=age /go/bin /go/bin/
COPY --from=mtg /go/bin /go/bin/
COPY --from=got /go/bin /go/bin/
COPY --from=shfmt /go/bin /go/bin/
COPY --from=croc /go/bin /go/bin/
COPY --from=mosdns /go/bin /go/bin/
COPY --from=go-shadowsocks2 /go/bin /go/bin/
COPY --from=overmind /go/bin /go/bin/
COPY --from=frp /go/bin /go/bin/
COPY --from=nali /go/bin /go/bin/
COPY --from=dnslookup /go/bin /go/bin/
COPY --from=wgcf /go/bin /go/bin/
COPY --from=dive /go/bin /go/bin/
COPY --from=duf /go/bin /go/bin/
COPY --from=wuzz /go/bin /go/bin/
COPY --from=httpstat /go/bin /go/bin/
COPY --from=chisel /go/bin /go/bin/
COPY --from=cloudflarespeedtest /go/bin /go/bin/
COPY --from=netflix-verify /go/bin /go/bin/
COPY --from=piknik /go/bin /go/bin/
COPY --from=apk-file /go/bin /go/bin/
RUN apk update; apk --no-progress --no-cache add \
    bash tzdata; \
    apk --no-progress --no-cache upgrade; \
    rm -rf /var/cache/apk/*; \
    cp -f /usr/share/zoneinfo/${DEFAULT_TZ} /etc/localtime; \
    mv /go/bin/windows_amd64/* /go/bin/

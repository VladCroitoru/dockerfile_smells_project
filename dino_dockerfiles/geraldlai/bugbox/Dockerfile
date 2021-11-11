FROM alpine:edge
MAINTAINER Gerald Lai <laigera@gmail.com>

ENTRYPOINT [ "/sbin/dumb-init" ]
CMD [ "/bin/bash" ]

ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    MANPATH=/usr/share/man \
    PAGER=less

# alpine-conf: /sbin/setup-*, /etc/init.d/networking (not installed)
# arping: host probe and discovery
# bind-tools: dig
# binutils: ld (GNU linker), as, ar, nm, objdump, readelf, strings
# bridge-utils: brctl
# bwm-ng: bandwidth monitor (vs iftop)
# coreutils: cp/mv/rm*, wc, uniq, sort, touch, etc.
# dstat: multi perf monitor (vs sar, vmstat, iostat)
# dumb-init: (vs init)
# fcron: (vs dcron)
# fd: (vs find)
# fping: parallel ping (vs ping)
# glances: multi perf monitor
# htop: (vs top, atop)
# ioping: disk I/O latency (vs dd measurement)
# iotop: (vs iostat, /proc/<pid>/io, ps STAT=D)
# iperf: (vs nuttcp, iperf3)
# iproute2: ip, bridge (vs net-tools: ifconfig, route, iptunnel, netstat)
# libressl: (vs openssl)
# mtr: (vs traceroute & ping)
# nanomsg: nanocat
# ncdu: (vs du)
# nmap-doc: (fix to not show German manpage)
# outils: jot, rs, un/vis, calendar, apply, lndir, lam, signify
# procps: ps, top, vmstat, w, kill, free, etc. (fix busybox overrides)
# psmisc: fuser, pstree, killall, peekfd
# pv: pipe monitor
# ripgrep: (vs grep, ag/the_silver_searcher)
# shadow: chsh, passwd, useradd, groupadd, etc. (not installed)
# socat: (vs netcat)
# sysstat: sar, mpstat, pidstat, iostat, sa, sadf, etc. (multi perf monitor)
# util-linux: col, fsck, mkfs, mkswap, more, reset, setterm
# tcpdump, tcpflow, tshark, ngrep, httpry
# wrk: HTTP benchmark
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories \
 && sed -i 's/cdn/3/' /etc/apk/repositories \
 && apk update \
 && apk upgrade \
 && apk update \
 && apk add man mdocml-apropos \
 && apk add ansible ansible-doc \
            bash bash-doc \
            bc bc-doc \
            bind-tools bind-doc \
            binutils binutils-doc \
            bridge-utils bridge-utils-doc \
            bwm-ng bwm-ng-doc iftop iftop-doc \
            ca-certificates \
            coreutils coreutils-doc \
            curl curl-doc \
            dstat dstat-doc \
            elinks elinks-lang elinks-doc \
            ethtool ethtool-doc \
            fcron fcron-doc \
            fd fd-doc \
            file file-doc \
            findutils findutils-doc \
            fping fping-doc arping arping-doc ioping ioping-doc \
            gawk gawk-doc \
            git git-perl git-doc \
            glances glances-doc \
            gnupg gnupg-doc \
            grep grep-doc \
            gzip gzip-doc \
            hdparm hdparm-doc \
            htop htop-doc iotop iotop-doc \
            httpry httpry-doc \
            iperf iperf-doc nuttcp \
            iproute2 iproute2-doc \
            jq jq-doc \
            less less-doc \
            lftp lftp-doc \
            libressl libressl-doc \
            lsof lsof-doc \
            man-pages mdocml-doc \
            mitmproxy \
            mosh mosh-doc \
            mtr mtr-doc \
            nano nano-doc \
            nanomsg nanomsg-doc \
            ncdu ncdu-doc \
            ncurses ncurses-terminfo-base \
            ngrep ngrep-doc \
            nmap nmap-ncat nmap-nping nmap-scripts nmap-doc \
            openssh openssh-doc \
            outils outils-jot outils-rs outils-vis outils-unvis outils-calendar outils-apply outils-lndir outils-lam outils-signify \
            parallel parallel-doc \
            patch patch-doc \
            patchutils patchutils-doc \
            perl perl-doc \
            pigz pigz-doc \
            procps procps-doc \
            pv pv-doc \
            python2 python2-doc \
            psmisc psmisc-doc \
            ripgrep ripgrep-doc \
            rsync rsync-doc \
            sed sed-doc \
            socat socat-doc \
            strace strace-doc ltrace ltrace-doc \
            sudo sudo-doc \
            sysstat sysstat-doc \
            tar tar-doc \
            tcpdump tcpdump-doc \
            tcpflow tcpflow-doc \
            the_silver_searcher the_silver_searcher-doc \
            tmux tmux-doc \
            tree tree-doc \
            tshark wireshark-doc \
            tzdata tzdata-doc \
            unzip unzip-doc zip zip-doc \
            util-linux util-linux-doc \
            vim vim-doc vimdiff \
            wget wget-doc \
            whois whois-doc \
            wrk wrk-doc \
            xz xz-doc \
 && apk add -f outils-doc \
 && curl -sSL -o /sbin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.2.2/dumb-init_1.2.2_amd64 \
 && chmod +x /sbin/dumb-init \
 && rm /usr/bin/blkdiscard \
 && bash -c 'rm -rf /usr/share/man/{de/man1/nmap.1.gz,es,fr,hr,hu,it,ja,pl,pt*,ro,ru,sk,zh}' \
 && (cd /usr/share/man/de/man1 && ln -s ../../man1/nmap.1.gz)

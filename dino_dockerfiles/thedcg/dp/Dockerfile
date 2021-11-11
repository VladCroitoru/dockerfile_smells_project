################################
# Dockerfile: thedcg/dp:latest

# ベース
FROM ubuntu:latest

################################
# Dockerfile.common

# 管理者
MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>

# Timezone
ENV TZ=Asia/Tokyo

# アップデート
RUN date --iso-8601=ns\
 && apt-get update\
 && apt-get -y upgrade\
 && DEBIAN_FRONTEND=noninteractive\
    apt-get -y install\
	tzdata \
	make \
	git \
	curl \
	openssh-client \
	perl \
	  libencode-perl \
	  libipc-run-perl \
	  libipc-run-safehandles-perl \
	  libjson-perl \
	  liburi-encode-perl \
	  liburi-perl \
	xz-utils \
	zip \
	unzip \
	dos2unix \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*\
 && echo "${TZ}" > /etc/timezone\
 && ln -sf "/usr/share/zoneinfo/${TZ}" /etc/localtime\
 && dpkg-reconfigure --frontend noninteractive tzdata\
 && date --iso-8601=ns

# 終了

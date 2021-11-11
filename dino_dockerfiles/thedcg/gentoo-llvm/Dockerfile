################################
# Dockerfile: thedcg/gentoo-llvm:latest

# ベース
FROM thedcg/gentoo-llvm_prep:latest

################################
# Dockerfile

# 管理者
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>

# アップデート
RUN date --iso-8601=ns\
 && emerge\
	sys-devel/llvm\
 && date --iso-8601=ns

# 終了

################################
# Dockerfile: thedcg/tl-gentoo:latest

# ベース
FROM thedcg/tl-gentoo_prep8:latest

################################
# Dockerfile

# 管理者
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>

# パッケージ
RUN date --iso-8601=ns\
 && emerge --depclean\
 && eclean-dist --deep\
 && echo '======== equery list * ========'\
 && equery list '*'\
 && date --iso-8601=ns\

#RUN eclean-pkg --deep

# 終了

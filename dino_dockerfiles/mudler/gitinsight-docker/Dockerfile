FROM sabayon/base-amd64
MAINTAINER mudler <mudler@sabayonlinux.org>

ENV ACCEPT_LICENSE=*
RUN equo update && equo u && equo i  perl git sci-libs/gsl dev-perl/PDL dev-perl/App-cpanminus gcc dev-perl/GD
RUN git clone https://github.com/mudler/WebApp-GitInsight.git /webapp/ && cd /webapp && cpanm --installdeps .
RUN cpanm install Mojolicious::Plugin::StaticCompressor Mojolicious::Plugin::AssetPack Mojolicious::Plugin::AssetPack::Backcompat LWP::Protocol::https

EXPOSE 8080
WORKDIR /webapp
VOLUME [ "/webapp/public/insight" ]
ENTRYPOINT [ "hypnotoad" ]
CMD [ "-f", "/webapp/script/git_insight" ]

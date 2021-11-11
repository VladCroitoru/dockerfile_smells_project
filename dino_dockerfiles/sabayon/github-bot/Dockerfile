FROM sabayon/base-amd64

MAINTAINER mudler <mudler@sabayonlinux.org>

# Set locales to en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV ACCEPT_LICENSE=*

RUN equo repo enable sabayon-limbo && equo up
RUN equo u && equo i dev-lang/perl sabayon-devkit dev-perl/App-cpanminus \
				dev-perl/Net-SSLeay \
				dev-perl/libwww-perl \
				dev-perl/Moo \
				dev-perl/JavaScript-Minifier \
				dev-perl/CSS-Minifier \
				dev-perl/Sereal-Decoder \
				dev-perl/Sereal-Encoder \
				app-emulation/docker \
				dev-perl/JavaScript-Minifier-XS \
				dev-perl/UUID-Tiny \
				app-misc/sabayon-sark \
				dev-vcs/git

RUN cpanm -n Mojolicious \
                   Net::GitHub \
                   Mojolicious::Plugin::Minion \
                   Mojolicious::Plugin::Directory \
									 Mojo::IOLoop::ReadWriteProcess \
                   Minion::Backend::Storable \
                   Minion \
                   Mojolicious::Plugin::AssetPack \
                   IPC::Open3 \
                   Storable \
                   Git::Sub \
                   Mojo::File && mkdir /app

ADD event_handler.pl /app/app.pl

# Set environment variables.
ENV HOME /app
ENV WORK_DIRECTORY=/app/shared

# Define working directory.
WORKDIR /app

# Define default command.
ENTRYPOINT ["/app/app.pl"]

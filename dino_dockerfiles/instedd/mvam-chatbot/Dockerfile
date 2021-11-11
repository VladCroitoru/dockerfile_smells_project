FROM crystallang/crystal:0.18.6

# Install dependencies
RUN apt-get update && apt-get -y install git libyaml-0-2 postgresql-client curl xz-utils && apt-get clean && rm -rf /var/lib/apt/lists/*

# Download ffmpeg and symlink it to bin
WORKDIR /opt
RUN curl -o ffmpeg.tar.xz http://ffmpeg.org/releases/ffmpeg-3.0.5.tar.xz
RUN tar xvJf ffmpeg.tar.xz
RUN ln -ns /opt/ffmpeg-3.0.5/ffmpeg /usr/local/bin/

# Install crystal deps
ADD shard.yml /app/
ADD shard.lock /app/
WORKDIR /app
RUN crystal deps

# Add and build bot and web
ADD . /app
RUN crystal compile src/mvam-bot.cr --release
RUN crystal compile src/mvam-web.cr --release
RUN crystal compile src/mvam-cron.cr --release
RUN crystal compile src/mvam-notifications.cr --release

# Start the bot
CMD "./mvam-bot"

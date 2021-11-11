# Base docker image
FROM debian:sid

# Install deps + add Chrome Stable + purge all the things
RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
	xvfb \
	xorg \
	gtk2-engines-pixbuf \
	dbus-x11 \
	imagemagick \
	ssh \
	openssh-client \
	git \
	curl \
  	gnupg \
	--no-install-recommends \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable \
	--no-install-recommends \
	&& apt-get purge --auto-remove -y curl gnupg

# Add Chrome as a user
RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome && chown -R chrome:chrome /home/chrome

ADD git-push /usr/local/bin/
RUN chmod u+x /usr/local/bin/git-push
RUN chown chrome:chrome /usr/local/bin/git-push

# Run Chrome non-privileged
USER chrome

# Expose port 9222
EXPOSE 9222

RUN export DISPLAY=:0
RUN wget https://raw.githubusercontent.com/jfrazelle/dotfiles/master/etc/docker/seccomp/chrome.json -O ~/chrome.json

CMD xvfb-run -e /dev/stdout --server-args='-screen 0, 1024x768x16' google-chrome-stable --headless --disable-gpu --remote-debugging-address=0.0.0.0 --remote-debugging-port=9222 --enable-logging=stderr --v=1

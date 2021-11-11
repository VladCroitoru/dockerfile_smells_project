# Dockerfile extending the generic Node image with application files for a
# single application.
FROM gcr.io/google_appengine/nodejs
LABEL name="bot-render" \
      version="0.3" \
      description="Renders a webpage for bot consumption (not production ready)"

RUN apt-get update && apt-get install -y \
  wget \
  gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 \
libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 \
libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 \
libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 git libxtst6 \
ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget \
  && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update && apt-get install -y \
  google-chrome-stable \
  --no-install-recommends \
  && rm -rf /var/lib/apt/lists/*

# Check to see if the the version included in the base runtime satisfies
# '>=7.6', if not then do an npm install of the latest available
# version that satisfies it.
RUN /usr/local/bin/install_node '>=7.6'

#COPY . /app/

RUN git clone https://github.com/GoogleChrome/rendertron.git /app


ADD thirdfonts /usr/share/fonts/thirdfonts
RUN fc-cache -fv

# Add botrender as a user
RUN groupadd -r botrender && useradd -r -g botrender -G audio,video botrender \
    && mkdir -p /home/botrender && chown -R botrender:botrender /home/botrender \
    && chown -R botrender:botrender /app

# Run botrender non-privileged
USER botrender

RUN npm install || \
  ((if [ -f npm-debug.log ]; then \
      cat npm-debug.log; \
    fi) && false)
    
RUN npm run build

ENV PORT=3000
EXPOSE 3000


ENTRYPOINT [ "npm" ]
CMD ["run", "start"]

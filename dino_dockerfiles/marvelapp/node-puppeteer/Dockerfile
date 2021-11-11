FROM node:16

WORKDIR /app

RUN apt-get update && apt-get install -y gconf-service \
    libasound2 \
    libatk1.0-0\
    libc6\
    libcairo2\
    libcups2\
    libdbus-1-3\
    libexpat1\
    libfontconfig1\
    libgcc1\
    libgconf-2-4\
    libgdk-pixbuf2.0-0\
    libglib2.0-0\
    libgtk-3-0\
    libgbm-dev\
    libnspr4\
    libpango-1.0-0\
    libpangocairo-1.0-0\
    libstdc++6\
    libx11-6\
    libx11-xcb1\
    libxcb1\
    libxcomposite1\
    libxcursor1\
    libxdamage1\
    libxext6\
    libxfixes3\
    libxi6\
    libxrandr2\
    libxrender1\
    libxss1\
    libxtst6\
    ca-certificates\
    fonts-liberation\
    libappindicator1\
    libnss3\
    lsb-release\
    xdg-utils\
    wget\
    fontconfig \
    fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf\
    && fc-cache -f -v

RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-init_1.2.1_amd64.deb \
    && dpkg -i dumb-init_*.deb \
    && rm -f dumb-init_*

# Add pptr user.
RUN groupadd -r pptruser \
    && useradd -r -g pptruser -G audio,video pptruser \
    && mkdir -p /home/pptruser/Downloads \
    && chown -R pptruser:pptruser /home/pptruser \
    && chown -R pptruser:pptruser /app


# && apt-cache search -n '^fonts-*' | cut -d' ' -f1 | grep -v 'unhinted' | xargs -d '\n' -- apt-get install -y && apt-get clean && fc-cache -f -v
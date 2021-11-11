FROM node:8-slim
RUN apt-get update \
  && apt-get install -y \
      libpangocairo-1.0-0 \
      libx11-xcb1 \
      libxcursor1 \
      libxdamage1 \
      libxi6 \
      libxtst6 \
      libnss3 \
      libcups2 \
      libxss1 \
      libxrandr2 \
      libgconf2-4 \
      libasound2 \
      libatk1.0-0 \
      libgtk-3-common \
  && apt-get autoremove -y \
  && rm -Rf /tmp/* /var/lib/apt/lists/*
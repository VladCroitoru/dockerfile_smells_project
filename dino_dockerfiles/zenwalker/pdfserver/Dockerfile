FROM python:3.6.5-jessie
ENV CHROME_VERSION=66.0.3359.139-1

RUN apt-get update && apt-get install -y --no-install-recommends \
        apt-transport-https ca-certificates curl gnupg \
    && curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app
RUN useradd -m chrome \
    && chown -R chrome:chrome /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./ ./

USER chrome
EXPOSE 8000
CMD ["gunicorn", "pdfserver.app:app", "--bind", "0.0.0.0:8000"]

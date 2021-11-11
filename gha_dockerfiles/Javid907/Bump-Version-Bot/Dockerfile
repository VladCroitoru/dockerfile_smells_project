FROM python:slim-buster

ENV APP_HOME /app
ENV LANG=en_US.UTF-8 LANGUAGE=en_US:en LC_ALL=en_US.UTF-8 PATH="/root/.local/bin:${PATH}"
EXPOSE 5000

RUN apt-get update && apt-get install -y --no-install-recommends \
												locales curl git jq procps cmake pkg-config \
												libicu-dev zlib1g-dev make build-essential \
												libcurl4-openssl-dev libssl-dev ruby-dev \
	&& sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
	&& locale-gen \
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

RUN gem install rdoc --version "6.3.1" \
	&& gem install github-linguist --version "7.16.1"
RUN mkdir $APP_HOME
COPY . $APP_HOME
WORKDIR $APP_HOME

RUN pip3 install --no-cache-dir -r ./requirements.txt
RUN pip3 install --no-cache-dir --user -U -e ./

CMD ["python3.10","-u","./bin/app.py"]

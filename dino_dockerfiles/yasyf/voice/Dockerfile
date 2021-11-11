FROM ubuntu

LABEL authors="Yasyf Mohamedali <yasyfm@gmail.com>"

CMD ./run.sh

EXPOSE 5000
EXPOSE 3000
WORKDIR /app

ARG GIT_CREDS

RUN apt-get update; \
  apt-get install -y git build-essential curl; \
  curl -sL https://deb.nodesource.com/setup_6.x | bash -; \
  apt-get install -y cmake \
  swig \
  libsndfile1-dev \
  libsdl1.2-dev \
  liblapack-dev \
  python2.7-dev \
  gfortran \
  libfftw3-dev \
  python \
  python-dev \
  python-pip \
  libpulse-dev \
  python-pyaudio \
  redis-server \
  nodejs \
  nginx;

RUN git clone https://$GIT_CREDS@github.com/VarunMohan/aaaaaalto speaker-diarization; \
  cd ./speaker-diarization; \
  ln -s ../AaltoASR ./ ; \
  ln -s ../AaltoASR/build ./ ; \
  ln -s ../AaltoASR/build/aku/feacat ./ ; \
  pip install numpy scipy docopt lxml;

COPY . ./

RUN pip install --upgrade pip setuptools wheel; \
  pip install -r requirements.txt;

RUN git clone https://$GIT_CREDS@github.com/suryabhupa/simple-nlu simple_nlu; \
  cd ./simple_nlu; \
  cp ./client_secret.json ../; \
  cp -R ./.credentials ~; \
  pip install -r requirements.txt;

RUN git clone https://$GIT_CREDS@github.com/josephwandile/soprano; \
  cd ./soprano; \
  npm install; \
  npm run build;

RUN mv ./nginx.conf /etc/nginx/sites-available/default;

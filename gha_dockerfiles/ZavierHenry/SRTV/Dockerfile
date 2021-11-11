# Copy local submodule
FROM mcr.microsoft.com/dotnet/runtime:5.0 AS base

# Restore dependencies
FROM mcr.microsoft.com/dotnet/sdk:5.0 AS restore
COPY LinqToTwitter/src/LinqToTwitter6 /LinqToTwitter/src/LinqToTwitter6
WORKDIR /app
COPY sr_tweet_vis/sr_tweet_vis.fsproj .
RUN dotnet restore

# Extract needed FFMPEG files and directories
FROM jrottenberg/ffmpeg:4.1-scratch AS ffmpeg
#FROM base
#COPY --from=ffmpeg / /

# Publish app
FROM restore AS publish
COPY sr_tweet_vis/ .
RUN dotnet publish -c Release -o publish

# Copy published app to base
#FROM base
#COPY --from=publish /app/publish .
#COPY --from=publish /app/assets/ /app/assets/

FROM base AS puppeteer
RUN apt-get update && apt-get -f install && apt-get -y install wget gnupg2 apt-utils
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Extract needed TTS files and directories
#FROM synesthesiam/coqui-tts:latest AS tts
#RUN	mkdir -p /TTS/app/bin && \
	#mkdir -p /TTS/usr/local && \
	#mkdir -p /TTS/app/lib/python3.7 && \
	#mkdir -p /TTS/usr/lib && \
     #mkdir -p /TTS/usr/bin && \
	#cp /app/bin/tts /app/bin/python3 /TTS/app/bin && \
	#cp -r /usr/local/lib /TTS/usr/local && \
	#cp -r /usr/local/bin /TTS/usr/local && \
	#cp -r /usr/lib/x86_64-linux-gnu /TTS/usr/lib && \
	#cp --parents -r /etc/ld.so.* /TTS && \
	#cp -r /lib /TTS && \
	#cp --parents -r /app/lib/python3.7/site-packages/librosa/ /TTS && \
	#find /app/lib/python3.7/site-packages -name __pycache__ -exec rm -r {} + && \
	#/app/bin/python3 -m compileall -b /app/lib/python3.7/site-packages && \
	#find /app/lib/python3.7/site-packages -name *.py -exec rm {} + && \
	#cp -r /app/lib/python3.7/site-packages /TTS/app/lib/python3.7

FROM python:3.7-buster AS tts-builder
WORKDIR /app
ENV PATH="/venv/bin:$PATH"

RUN python -m venv /venv

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --compile "torch==1.8.0+cpu" TTS -f https://download.pytorch.org/whl/torch_stable.html

FROM python:3.7-slim-buster as tts
RUN	apt update -y && apt -y install --no-install-recommends libsndfile1 && \
	rm -rf /var/lib/apt/lists/*
COPY --from=tts-builder /venv /venv

# Delete unnessary packages
#WORKDIR /TTS/app/lib/python3.7/site-packages
#RUN rm -r pip wheel setuptools tests werkzeug *.dist-info Cython \
	     #matplotlib/mpl-data/images unidic_lite/dicdir/unidic-mecab.pdf && \
    #find . -name test -exec rm -r {} + && \
    #find . -name tests -exec rm -r {} + && \
    #cp -r /app/lib/python3.7/site-packages/gdown-*.dist-info .
#
#WORKDIR /TTS/tts/models
#RUN	wget -O vits.zip "https://coqui.gateway.scarf.sh/v0.2.0/tts_models--en--ljspeech--vits.zip" && \
	#unzip vits.zip && \
	#rm -r __MACOSX vits.zip && \
	#mv tts_models--en--ljspeech--vits vits
#
#WORKDIR /TTS/usr/local/lib/python3.7/site-packages
#RUN rm -r pip wheel setuptools *.dist-info ../lib2to3 ../ensurepip

# Run program
FROM base
COPY --from=publish /app/publish .
COPY --from=publish /app/assets/ /app/assets/
COPY --from=ffmpeg / /
# COPY --from=tts /TTS /
COPY --from=tts / /
COPY --from=puppeteer / /

# Update cache to have soundfile
RUN /sbin/ldconfig

ENV PATH="/venv/bin:$PATH"
ENV FFMPEG_EXECUTABLE="/bin/ffmpeg"
ENV TTS_EXECUTABLE="/venv/bin/tts"
ENV LD_LIBRARY_PATH="/usr/local/lib"
ENV PYTHONPATH="/app/lib/python3.7/site-packages"
ENV CHROME_EXECUTABLE="/usr/bin/google-chrome"
# ENV TTS_MODEL_DIRECTORY="/tts/models/vits"
# ENTRYPOINT [ "/app/bin/tts", "-h" ]
# ENTRYPOINT ["dotnet", "sr_tweet_vis.dll", "synthesize", "This is the chosen spoken text to test the docker version of the text to speech. This speech also has a longer line than I would use to test this in order the see if detecting silence needs to be refined to preserve synchronization"]

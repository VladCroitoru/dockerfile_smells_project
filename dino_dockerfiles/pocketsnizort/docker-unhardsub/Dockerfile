FROM jrottenberg/ffmpeg:ubuntu

ENV PYTHONPATH="/usr/share/vsscripts"

VOLUME /input
VOLUME /output
    
RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository -y ppa:djcj/vapoursynth && \
    apt-get update -y --fix-missing && \
    apt-get install -y \
        python3-pip \
        vapoursynth \
        vapoursynth-extra-plugins

ADD https://raw.githubusercontent.com/Irrational-Encoding-Wizardry/kagefunc/master/kagefunc.py "/usr/share/vsscripts/kagefunc.py"
ADD https://raw.githubusercontent.com/Irrational-Encoding-Wizardry/fvsfunc/master/fvsfunc.py "/usr/share/vsscripts/fvsfunc.py"
ADD https://raw.githubusercontent.com/WolframRhodium/muvsfunc/master/muvsfunc.py "/usr/share/vsscripts/muvsfunc.py"
ADD "unhardsub.vpy" "/usr/share/vsscripts/unhardsub.vpy"

ENTRYPOINT ["/bin/bash", "-c"]
#CMD ["--help"]

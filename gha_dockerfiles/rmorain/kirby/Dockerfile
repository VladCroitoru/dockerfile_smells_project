FROM pytorch/pytorch

WORKDIR /kirby

ADD . /kirby

ENV PACKAGES="\
    git \
    vim \
"

RUN apt update && apt -y install ${PACKAGES}

RUN pip install -r requirements.txt

RUN python setup.py develop

ENV NAME kirby 

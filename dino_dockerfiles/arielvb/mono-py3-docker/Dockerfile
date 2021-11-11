FROM mono:6.12.0.107

LABEL mantainer="arielvb"

ENV APT_KEY_DONT_WARN_ON_DANGEROUS_USAGE="1"

# Fix upgrade problem with mono repository
RUN rm /etc/apt/sources.list.d/mono-official-stable.list
RUN apt-get update && apt upgrade -y && apt-get install gnupg2 -y
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF
RUN echo "deb https://download.mono-project.com/repo/ubuntu vs-bionic main" | tee /etc/apt/sources.list.d/mono-official-vs.list
RUN apt-get update && apt-get install monodevelop python3 python3-pip python3-lxml -y


# Upgrade pip
## Fix pip index url and disable pip version check
RUN mkdir -p /root/.pip && echo "[global]\nindex-url=https://pypi.python.org/pypi\ndisable-pip-version-check=true\n" > /root/.pip/pip.conf
RUN pip3 install --upgrade pip


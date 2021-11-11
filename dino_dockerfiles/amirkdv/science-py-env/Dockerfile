FROM ubuntu:16.04

RUN apt-get update -qq
RUN apt-get install -qqy vim build-essential pkg-config
RUN apt-get install -qqy python-dev python-setuptools python-pip virtualenv

# Dependencies found by manually inspecting the output of:
#
#   $ apt-cache show python-numpy python-scipy python-matplotlib | grep ^Depends:
#
# Dependencies for python-numpy and python-scipy
RUN apt-get install -qqy libblas3 libc6 liblapack3 libgcc1 libgfortran3 libstdc++6
# Dependencies for python-matplotlib
RUN apt-get install -qqy libfreetype6 libgdk-pixbuf2.0-0 libglib2.0-0 \
                         libgtk2.0-0 libpng12-0 libtcl8.6 libtk8.6
RUN apt-get install -qqy libfreetype6-dev libpng12-dev
# Without tk-dev you get "cannot import name _tkagg"
RUN apt-get install -qqy tk-dev

# Support TeX rendering in matplotlib. This requires dvipng, and in Ubuntu,
# type1cm, to be installed. Note that this pulls in texlive. Skip recommended
# packages (includes texlive-latex-doc which is huge).
# cf. http://matplotlib.org/users/usetex.html.
RUN apt-get install --no-install-recommends -y dvipng texlive-latex-extra

RUN pip install --upgrade pip

# create a virtualenv
ENV SCI_PY_ENV /sci-py-env
RUN virtualenv $SCI_PY_ENV
RUN . $SCI_PY_ENV/bin/activate && pip install numpy scipy matplotlib

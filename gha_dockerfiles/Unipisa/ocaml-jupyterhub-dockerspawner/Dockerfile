FROM jupyterhub/singleuser
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Rome

USER root

RUN apt-get -y update
RUN apt-get -y install -qq --force-yes apt-utils apt-file
RUN apt-get -y install -qq --force-yes vim nano wget curl iputils-ping git tzdata python3-pip ocaml opam libgmp-dev pkg-config libzmq3-dev

RUN pip3 install notebook RISE jupyter jupyter_contrib_nbextensions
RUN jupyter contrib nbextensions install --system

USER jovyan
RUN opam init --disable-sandboxing
RUN eval $(opam env)
RUN opam update
RUN pip3 install jupyter nbgitpuller jupyterlab_github
RUN opam install -y jupyter
RUN eval $(opam env) && ocaml-jupyter-opam-genspec
RUN jupyter kernelspec install --user --name ocaml-jupyter "$(opam var share)/jupyter"
RUN jupyter nbextension enable splitcell/splitcell

USER jovyan
WORKDIR $HOME

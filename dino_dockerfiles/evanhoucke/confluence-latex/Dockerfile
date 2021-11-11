FROM atlassian/confluence-server:7.1.2

RUN apt-get update --quiet && \
    apt-get install --yes --no-install-recommends dvipng texlive-latex-base texlive-extra-utils texlive-science mimetex graphviz && \
    rm -rf /var/lib/apt/lists/*


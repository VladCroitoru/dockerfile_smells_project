FROM bioboxes/gaet@sha256:e6f9d92208176f4f8125fda6e5aaa300e26acb3ea05bd49b96e79da3d8fa61b4

# See CHANGELOG entry for 2017-12-20
ADD image /usr/local
RUN /usr/local/bin/install/remove_tbl2asn_from_prokka.sh && \
    rm -r /usr/local/bin/install.sh /usr/local/bin/install

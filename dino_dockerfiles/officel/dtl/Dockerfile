FROM mhart/alpine-node

MAINTAINER Office L

# about textlint. see: https://textlint.github.io/
# see: https://github.com/textlint/textlint/wiki/Collection-of-textlint-rule

ENV TEXTLINT_PLUGINS \
    textlint-rule-no-todo \
    textlint-rule-preset-ja-spacing \
    textlint-rule-preset-ja-technical-writing \ 
    textlint-rule-preset-jtf-style \
    textlint-rule-prh \
    textlint-rule-spellcheck-tech-word \
    textlint-rule-general-novel-style-ja \
    \
    textlint-rule-ja-unnatural-alphabet \
    textlint-rule-ja-no-redundant-expression \
    textlint-rule-ja-no-abusage \
    textlint-rule-no-double-negative-ja \
    textlint-rule-no-mixed-zenkaku-and-hankaku-alphabet \
    textlint-rule-ja-no-successive-word \
    textlint-rule-ja-yahoo-kousei \
    \
    textlint-filter-rule-comments \
    textlint-filter-rule-node-types \
    textlint-filter-rule-whitelist \
    \
    textlint-plugin-html


RUN npm install -g textlint $TEXTLINT_PLUGINS 

WORKDIR /docs

# Samples
COPY .textlintrc /
COPY .textlintrc_preset-ja-technical-writing /
COPY prh.yml /

# ENTRYPOINT ["textlint"]

CMD ["textlint", "-h"]

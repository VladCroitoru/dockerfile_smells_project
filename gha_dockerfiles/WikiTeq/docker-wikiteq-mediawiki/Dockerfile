FROM centos:7.9.2009 as base

LABEL maintainers="pastakhov@yandex.ru,alexey@wikiteq.com"
LABEL org.opencontainers.image.source=https://github.com/WikiTeq/docker-wikiteq-mediawiki

ENV MW_VERSION=REL1_35 \
	MW_CORE_VERSION=1.35.4 \
	MW_HOME=/var/www/html/w \
	MW_LOG=/var/log/mediawiki \
	MW_VOLUME=/mediawiki \
	MW_ORIGIN_FILES=/mw_origin_files \
	WWW_USER=apache \
	WWW_GROUP=apache \
	APACHE_LOG_DIR=/var/log/apache2

# Install requered packages
RUN set -x; \
	yum -y install --nogpgcheck yum-utils \
	https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
	https://rpms.remirepo.net/enterprise/remi-release-7.rpm \
	https://download1.rpmfusion.org/free/el/rpmfusion-free-release-7.noarch.rpm \
	https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-7.noarch.rpm \
	&& yum-config-manager --enable remi-php74 \
	&& yum -y update \
	&& yum -y install \
	 applydeltarpm \
	 httpd \
	 php \
	 php-cli \
	 php-mysqlnd \
	 php-gd \
	 php-mbstring \
	 php-xml \
	 php-intl \
	 php-opcache \
	 php-pecl-apcu \
	 php-redis \
	 git \
	 mysql \
	 wget \
	 unzip \
	 ImageMagick \
	 python-pygments \
	 ssmtp \
	 patch \
	 vim \
	 mc \
	 ffmpeg \
	 curl \
	 monit \
	 clamav \
	 --exclude=clamav-update \
	&& yum clean all \
	# remove clamav virus signature data, because we use clamav outside of the docker container
	&& rm -fr /var/lib/clamav/* \
	&& mkdir -p $MW_ORIGIN_FILES \
	&& mkdir -p $MW_HOME \
	&& mkdir -p $MW_LOG

# Composer
RUN set -x -o pipefail; \
	curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \
    && composer self-update 2.1.3

FROM base as extensions

# Extensions
# This stage install all the necessary extensions into $MW_HOME/extensions & applies their patches
RUN set -x; \
	mkdir -p $MW_HOME/extensions \
	&& cd $MW_HOME/extensions \
	# PageSchemas
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/PageSchemas $MW_HOME/extensions/PageSchemas \
	&& cd $MW_HOME/extensions/PageSchemas \
	&& git checkout -q 2f602017201dc2d518e813c967b8668f5d7a2817 \
	# AdminLinks
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/AdminLinks $MW_HOME/extensions/AdminLinks \
	&& cd $MW_HOME/extensions/AdminLinks \
	&& git checkout -q ea76d25167320f5a0d8a63254bd38ff5582e4ff4 \
	# ContributionScores
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ContributionScores $MW_HOME/extensions/ContributionScores \
	&& cd $MW_HOME/extensions/ContributionScores \
	&& git checkout -q de75d9f6904e9b41f7148417cc9fd491164da722 \
	# ExternalData
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ExternalData $MW_HOME/extensions/ExternalData \
	&& cd $MW_HOME/extensions/ExternalData \
	&& git checkout -q 70116a96a53c78d1466219d5ddde384677e97c8a \
	# DismissableSiteNotice
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/DismissableSiteNotice $MW_HOME/extensions/DismissableSiteNotice \
	&& cd $MW_HOME/extensions/DismissableSiteNotice \
	&& git checkout -q ad3a7802f78498e748833886613e28b4f7cb91b8 \
	# MobileFrontend
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/MobileFrontend $MW_HOME/extensions/MobileFrontend \
	&& cd $MW_HOME/extensions/MobileFrontend \
	&& git checkout -q db7c7843189a9009dde59503e3e3d4cbcab8eaef \
	# RevisionSlider
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/RevisionSlider $MW_HOME/extensions/RevisionSlider \
	&& cd $MW_HOME/extensions/RevisionSlider \
	&& git checkout -q d1a6af207e26e220d93d16381a58055259575d3b \
	# SandboxLink
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SandboxLink $MW_HOME/extensions/SandboxLink \
	&& cd $MW_HOME/extensions/SandboxLink \
	&& git checkout -q 2d7123c29b5e61f2c7d6e81168dc6d261ff93cbd \
	# OpenIDConnect
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/OpenIDConnect $MW_HOME/extensions/OpenIDConnect \
	&& cd $MW_HOME/extensions/OpenIDConnect \
	&& git checkout -q 19f422146969691ac2e3c9b5b33cf07116c7ee79 \
	# PluggableAuth
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/PluggableAuth $MW_HOME/extensions/PluggableAuth \
	&& cd $MW_HOME/extensions/PluggableAuth \
	&& git checkout -q d036ae0bf509ce160c4f6a1965c795d4fdae82b4 \
	# WhoIsWatching
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/WhoIsWatching $MW_HOME/extensions/WhoIsWatching \
	&& cd $MW_HOME/extensions/WhoIsWatching \
	&& git checkout -q 510e95a76fe140890ea83abf75be64ce97f7fd30 \
	# LabeledSectionTransclusion
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/LabeledSectionTransclusion $MW_HOME/extensions/LabeledSectionTransclusion \
	&& cd $MW_HOME/extensions/LabeledSectionTransclusion \
	&& git checkout -q 8b0ba6952488763201a0defef0499c743ef933f7 \
	# GlobalNotice
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/GlobalNotice $MW_HOME/extensions/GlobalNotice \
	&& cd $MW_HOME/extensions/GlobalNotice \
	&& git checkout -q f86637d27e6be7c60ec12bb8859f4b76cceb1be2 \
	# FixedHeaderTable
	&& git clone --single-branch -b master https://gerrit.wikimedia.org/r/mediawiki/extensions/FixedHeaderTable $MW_HOME/extensions/FixedHeaderTable \
	&& cd $MW_HOME/extensions/FixedHeaderTable \
	&& git checkout -q 5096d0f2cfc2409612484774541cd485494ee7ea \
	# Lingo
	&& git clone --single-branch -b master https://gerrit.wikimedia.org/r/mediawiki/extensions/Lingo $MW_HOME/extensions/Lingo \
	&& cd $MW_HOME/extensions/Lingo \
	&& git checkout -q d59cdaf9afbb98a0a8b507afdb102a2755dd85a1 \
	# OpenGraphMeta
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/OpenGraphMeta $MW_HOME/extensions/OpenGraphMeta \
	&& cd $MW_HOME/extensions/OpenGraphMeta \
	&& git checkout -q 5bbb2754497515a08562ad6cf62ed51ab9e588bd \
	# NumerAlpha
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/NumerAlpha $MW_HOME/extensions/NumerAlpha \
	&& cd $MW_HOME/extensions/NumerAlpha \
	&& git checkout -q ab24279b72af1c199651d4630aa198d39344785f \
	# DataTransfer
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/DataTransfer $MW_HOME/extensions/DataTransfer \
	&& cd $MW_HOME/extensions/DataTransfer \
	&& git checkout -q d14a8f9acdcc42887dc3da3560300d60f1ecee8b \
	# Variables
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Variables $MW_HOME/extensions/Variables \
	&& cd $MW_HOME/extensions/Variables \
	&& git checkout -q e20f4c7469bdc724ccc71767ed86deec3d1c3325 \
	# Loops
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Loops $MW_HOME/extensions/Loops \
	&& cd $MW_HOME/extensions/Loops \
	&& git checkout -q f0f1191f56e6b31b063f59ee2710a6f62890a336 \
	# MyVariables
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/MyVariables $MW_HOME/extensions/MyVariables \
	&& cd $MW_HOME/extensions/MyVariables \
	&& git checkout -q cde2562ffde8a1b648be10b78b86386a9c7d3151 \
	# Arrays
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Arrays $MW_HOME/extensions/Arrays \
	&& cd $MW_HOME/extensions/Arrays \
	&& git checkout -q e09d74379c191f3e83560d7bb35d39fb4162f0fc \
	# DisplayTitle
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/DisplayTitle $MW_HOME/extensions/DisplayTitle \
	&& cd $MW_HOME/extensions/DisplayTitle \
	&& git checkout -q 1bbe37df7b769f4b42884fef7347ab4ec8db16aa \
	# ConfirmAccount
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ConfirmAccount $MW_HOME/extensions/ConfirmAccount \
	&& cd $MW_HOME/extensions/ConfirmAccount \
	&& git checkout -q cde8cece830eaeebf66d0d96dc09a206683435c7 \
	# Lockdown
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Lockdown $MW_HOME/extensions/Lockdown \
	&& cd $MW_HOME/extensions/Lockdown \
	&& git checkout -q 4d595408c96190a1c44cfed96f244988fc88054a \
	# Math
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Math $MW_HOME/extensions/Math \
	&& cd $MW_HOME/extensions/Math \
	&& git checkout -q ce438004cb7366860d3bff1f60839ef3c304aa1e \
	# Echo
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Echo $MW_HOME/extensions/Echo \
	&& cd $MW_HOME/extensions/Echo \
	&& git checkout -q a3dedc0d64380d74d2e153aad9a8d54cee1b85bd \
	# ChangeAuthor
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ChangeAuthor $MW_HOME/extensions/ChangeAuthor \
	&& cd $MW_HOME/extensions/ChangeAuthor \
	&& git checkout -q 2afac6dcc34264de8f952ab89c4c0332ddb67051 \
	# ContactPage
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ContactPage $MW_HOME/extensions/ContactPage \
	&& cd $MW_HOME/extensions/ContactPage \
	&& git checkout -q 0466489a8c2ad8f5c045b145cb8b65bb8b164c48 \
	# IframePage
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/IframePage $MW_HOME/extensions/IframePage \
	&& cd $MW_HOME/extensions/IframePage \
	&& git checkout -q abbff3dd72194ae7ec07415ff6816170198d1f01 \
	# MsUpload
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/MsUpload $MW_HOME/extensions/MsUpload \
	&& cd $MW_HOME/extensions/MsUpload \
	&& git checkout -q 583f3a9fdc541ef492f042be3313f4edd47205de \
	# SelectCategory
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SelectCategory $MW_HOME/extensions/SelectCategory \
	&& cd $MW_HOME/extensions/SelectCategory \
	&& git checkout -q 4c28f553dcec7534e0d403fb3e1b45bbfafb21ad \
	# ShowMe
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ShowMe $MW_HOME/extensions/ShowMe \
	&& cd $MW_HOME/extensions/ShowMe \
	&& git checkout -q 368f7a9cdd151a9fb198c83ca9a48efacf6b2b1f \
	# SoundManager2Button
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SoundManager2Button $MW_HOME/extensions/SoundManager2Button \
	&& cd $MW_HOME/extensions/SoundManager2Button \
	&& git checkout -q 5264bf3eaad7b9ed6cc794bbb3c8622d4d164e8d \
	# CirrusSearch
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/CirrusSearch $MW_HOME/extensions/CirrusSearch \
	&& cd $MW_HOME/extensions/CirrusSearch \
	&& git checkout -q 203237ef2828c46094c5f6ba26baaeff2ab3596b \
	# Elastica
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Elastica $MW_HOME/extensions/Elastica \
	&& cd $MW_HOME/extensions/Elastica \
	&& git checkout -q 8af6b458adf628a98af4ba8e407f9c676bf4a4fb \
	# googleAnalytics
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/googleAnalytics $MW_HOME/extensions/googleAnalytics \
	&& cd $MW_HOME/extensions/googleAnalytics \
	&& git checkout -q ad1906e59ff4d460962d91c4865c47cbec77a5d4 \
	# UniversalLanguageSelector
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/UniversalLanguageSelector $MW_HOME/extensions/UniversalLanguageSelector \
	&& cd $MW_HOME/extensions/UniversalLanguageSelector \
	&& git checkout -q e7ab607dd91b55f15a733bcba793619cf48d3604 \
	# Survey
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Survey $MW_HOME/extensions/Survey \
	&& cd $MW_HOME/extensions/Survey \
	&& git checkout -q eab540c594d630c6672cc0920951a45f4e272f81 \
	# LiquidThreads
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/LiquidThreads $MW_HOME/extensions/LiquidThreads \
	&& cd $MW_HOME/extensions/LiquidThreads \
	&& git checkout -q 21ebc92586f75b9551822eb2f6f0ee0235856ad8 \
	# CodeMirror
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/CodeMirror $MW_HOME/extensions/CodeMirror \
	&& cd $MW_HOME/extensions/CodeMirror \
	&& git checkout -q 84846ec71fb3be844771025ddd9c039da3cc1616 \
	# Flow
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Flow $MW_HOME/extensions/Flow \
	&& cd $MW_HOME/extensions/Flow \
	&& git checkout -q d37f94241d8cb94ac96c7946f83c1038844cf7e6 \
	# ApprovedRevs
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/ApprovedRevs $MW_HOME/extensions/ApprovedRevs \
	&& cd $MW_HOME/extensions/ApprovedRevs \
	&& git checkout -q 99fadf2d9e030b8305e53e6557d32dc67ffbbc68 \
	# Collection
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Collection $MW_HOME/extensions/Collection \
	&& cd $MW_HOME/extensions/Collection \
	&& git checkout -q c22330cb462cbcb7e01da48b7ab1e0caa4e3841f \
	# HTMLTags
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/HTMLTags $MW_HOME/extensions/HTMLTags \
	&& cd $MW_HOME/extensions/HTMLTags \
	&& git checkout -q 3476196e1e46b3cb56035d2151d98797c088bc90 \
	# BetaFeatures
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/BetaFeatures $MW_HOME/extensions/BetaFeatures \
	&& cd $MW_HOME/extensions/BetaFeatures \
	&& git checkout -q 27486070bff17b4886543fe8d888585a722c6a76 \
	# SkinPerNamespace
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SkinPerNamespace $MW_HOME/extensions/SkinPerNamespace \
	&& cd $MW_HOME/extensions/SkinPerNamespace \
	&& git checkout -q e17cff49d8dda42b8118375188ca0f7847e10b3f \
	# SkinPerPage
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SkinPerPage $MW_HOME/extensions/SkinPerPage \
	&& cd $MW_HOME/extensions/SkinPerPage \
	&& git checkout -q b929bc6e56b51a8356c04b3761c262b6a9a423e3 \
	# CharInsert
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/CharInsert $MW_HOME/extensions/CharInsert \
	&& cd $MW_HOME/extensions/CharInsert \
	&& git checkout -q 98fa7c3c8b114a565c2e63e52319ea5382ed695a \
	# Tabs
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Tabs $MW_HOME/extensions/Tabs \
	&& cd $MW_HOME/extensions/Tabs \
	&& git checkout -q 1d669869c746183f9972ab7201e7e4981a248311 \
	# AdvancedSearch
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/AdvancedSearch $MW_HOME/extensions/AdvancedSearch \
	&& cd $MW_HOME/extensions/AdvancedSearch \
	&& git checkout -q d1895707f3750a6d4a486b425ac9a727707f27f9 \
	# Disambiguator
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Disambiguator $MW_HOME/extensions/Disambiguator \
	&& cd $MW_HOME/extensions/Disambiguator \
	&& git checkout -q 06cae54808417caa72c6fe6702af23da5f4c45c5 \
	# CheckUser
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/CheckUser $MW_HOME/extensions/CheckUser \
	&& cd $MW_HOME/extensions/CheckUser \
	&& git checkout -q 025d552c4ca4968cca8a8717b25129d62147c9a7 \
	# CommonsMetadata
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/CommonsMetadata $MW_HOME/extensions/CommonsMetadata \
	&& cd $MW_HOME/extensions/CommonsMetadata \
	&& git checkout -q badf499682be04d2b2b1139ae9063fb7b436daa3 \
	# TimedMediaHandler
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/TimedMediaHandler $MW_HOME/extensions/TimedMediaHandler \
	&& cd $MW_HOME/extensions/TimedMediaHandler \
	&& git checkout -q 6d922042852cd9c6b02a406ccfcc0dae8533624b \
	# SocialProfile
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SocialProfile $MW_HOME/extensions/SocialProfile \
	&& cd $MW_HOME/extensions/SocialProfile \
	&& git checkout -q d34f32174c23818dbf057a5482dc6ed4781a3a25 \
	# WikiForum
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/WikiForum $MW_HOME/extensions/WikiForum \
	&& cd $MW_HOME/extensions/WikiForum \
	&& git checkout -q 9cffc82dfd761fbb7a91aa778fb6633215c47501 \
	# VoteNY
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/VoteNY $MW_HOME/extensions/VoteNY \
	&& cd $MW_HOME/extensions/VoteNY \
	&& git checkout -q b73dd009cf151a9f442361f6eb1e355817ca1e18 \
	# AJAXPoll
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/AJAXPoll $MW_HOME/extensions/AJAXPoll \
	&& cd $MW_HOME/extensions/AJAXPoll \
	&& git checkout -q 846bbd16799efb7b279433856a5e85914961314b \
	# YouTube
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/YouTube $MW_HOME/extensions/YouTube \
	&& cd $MW_HOME/extensions/YouTube \
	&& git checkout -q bd736585dca8412d5eb9dde8f68a54b3c69df9cf \
	# AntiSpoof
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/AntiSpoof $MW_HOME/extensions/AntiSpoof \
	&& cd $MW_HOME/extensions/AntiSpoof \
	&& git checkout -q 1c82ce797d2eefa7f82fb88f82d550c2c73ff3b6 \
	# Popups
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Popups $MW_HOME/extensions/Popups \
	&& cd $MW_HOME/extensions/Popups \
	&& git checkout -q dccd60752353eac1063a79f81a8059b3b06b9353 \
	# Description2
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Description2 $MW_HOME/extensions/Description2 \
	&& cd $MW_HOME/extensions/Description2 \
	&& git checkout -q c471ce36b822e74104a38e302bd59b993c679d72 \
	# Thanks
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Thanks $MW_HOME/extensions/Thanks \
	&& cd $MW_HOME/extensions/Thanks \
	&& git checkout -q e28a16d38b5a4c0d32f2388aa4fcc93ec48e7b02 \
	# MobileDetect
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/MobileDetect $MW_HOME/extensions/MobileDetect \
	&& cd $MW_HOME/extensions/MobileDetect \
	&& git checkout -q 017464a0f56fa34fd03118d6502f15c9952f9d9a \
	# SimpleChanges
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SimpleChanges $MW_HOME/extensions/SimpleChanges \
	&& cd $MW_HOME/extensions/SimpleChanges \
	&& git checkout -q c0991c9245dc8907e59f8e4c6fb89852f0c52dde \
	# UserMerge
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/UserMerge $MW_HOME/extensions/UserMerge \
	&& cd $MW_HOME/extensions/UserMerge \
	&& git checkout -q 1c161b2c12c3882b4230561d1834e7c5170d9200 \
	# LinkSuggest
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/LinkSuggest $MW_HOME/extensions/LinkSuggest \
	&& cd $MW_HOME/extensions/LinkSuggest \
	&& git checkout -q 44f905ee4e7ac8349a822bfd9d22f79a1e24e4a4 \
	# TwitterTag
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/TwitterTag $MW_HOME/extensions/TwitterTag \
	&& cd $MW_HOME/extensions/TwitterTag \
	&& git checkout -q 6758d15d8e4f0553bbcbc7af026ba245f1ff9282 \
	# TemplateStyles
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/TemplateStyles $MW_HOME/extensions/TemplateStyles \
	&& cd $MW_HOME/extensions/TemplateStyles \
	&& git checkout -q a859a0c0b742af1709d5b836737ff93ffa5a43c9 \
	# LookupUser
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/LookupUser $MW_HOME/extensions/LookupUser \
	&& cd $MW_HOME/extensions/LookupUser \
	&& git checkout -q 57d8f2df716758f87e2286c52f0bdea78a8a85cf \
	# HeadScript
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/HeadScript $MW_HOME/extensions/HeadScript \
	&& cd $MW_HOME/extensions/HeadScript \
	&& git checkout -q f8245e350d6e3452a20d871240ebb193f69f384d \
	# Favorites
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Favorites $MW_HOME/extensions/Favorites \
	&& cd $MW_HOME/extensions/Favorites \
	&& git checkout -q 782afc856a35c37b1a508ce37f7402954cc32efb \
	# GoogleDocTag
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/GoogleDocTag $MW_HOME/extensions/GoogleDocTag \
	&& cd $MW_HOME/extensions/GoogleDocTag \
	&& git checkout -q f9fdb27250112fd02d9ff8eeb2a54ecd8c49b08d \
	# EditAccount
	&& git clone --single-branch -b master https://gerrit.wikimedia.org/r/mediawiki/extensions/EditAccount $MW_HOME/extensions/EditAccount \
	&& cd $MW_HOME/extensions/EditAccount \
	&& git checkout -q 7da60b98d196dc7bab82ce73e1e88ec82ba03725 \
	# EventLogging
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/EventLogging $MW_HOME/extensions/EventLogging \
	&& cd $MW_HOME/extensions/EventLogging \
	&& git checkout -q 71f88485e0bea9c668dec20e018d3da2d444585e \
	# EventStreamConfig
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/EventStreamConfig $MW_HOME/extensions/EventStreamConfig \
	&& cd $MW_HOME/extensions/EventStreamConfig \
	&& git checkout -q bce5bc385b2919cf294a074b64bc330ac48f78db \
	# SaveSpinner
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/SaveSpinner $MW_HOME/extensions/SaveSpinner \
	&& cd $MW_HOME/extensions/SaveSpinner \
	&& git checkout -q 2f19bdd7c6cc48729faa4b8e9afc8953dbeaeae1 \
	# UploadWizard
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/UploadWizard $MW_HOME/extensions/UploadWizard \
	&& cd $MW_HOME/extensions/UploadWizard \
	&& git checkout -q c54e588bac935db78fad297602f61d47ed2162d5 \
	# CommentStreams
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/CommentStreams $MW_HOME/extensions/CommentStreams \
	&& cd $MW_HOME/extensions/CommentStreams \
	&& git checkout -q 91161ea4cf31df54229b5881a7f96bcbd6fa48ff \
	# GoogleAnalyticsMetrics
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/GoogleAnalyticsMetrics $MW_HOME/extensions/GoogleAnalyticsMetrics \
	&& cd $MW_HOME/extensions/GoogleAnalyticsMetrics \
	&& git checkout -q c292c17b2e1f44f11a82323b48ec2911c384a085 \
	# MassMessage
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/MassMessage $MW_HOME/extensions/MassMessage \
	&& cd $MW_HOME/extensions/MassMessage \
	&& git checkout -q 4c6be095fcb1eb2d741881773a6b8ef0487871af \
	# MassMessageEmail
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/MassMessageEmail $MW_HOME/extensions/MassMessageEmail \
	&& cd $MW_HOME/extensions/MassMessageEmail \
	&& git checkout -q 2424d03ac7b53844d49379cba3cceb5d9f4b578e \
	# SemanticDrilldown
	&& git clone --single-branch -b master https://gerrit.wikimedia.org/r/mediawiki/extensions/SemanticDrilldown $MW_HOME/extensions/SemanticDrilldown \
	&& cd $MW_HOME/extensions/SemanticDrilldown \
	&& git checkout -q c9f0770512d9c34efc1fa1235a7ccf894e8aef9e \
	# VEForAll TODO (version 0.3, master), switch back to REL_x for 1.36
	&& git clone --single-branch -b master https://gerrit.wikimedia.org/r/mediawiki/extensions/VEForAll $MW_HOME/extensions/VEForAll \
	&& cd $MW_HOME/extensions/VEForAll \
	&& git checkout -q 8f83eb6e607b89f6e1a44966e8637cadd7942bd7 \
	# HeaderTabs
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/HeaderTabs $MW_HOME/extensions/HeaderTabs \
	&& cd $MW_HOME/extensions/HeaderTabs \
	&& git checkout -q 6c0787d956ba993027aae80f8f7cba0c4437ada7 \
	# UrlGetParameters
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/UrlGetParameters $MW_HOME/extensions/UrlGetParameters \
	&& cd $MW_HOME/extensions/UrlGetParameters \
	&& git checkout -q 163df22a566c34e0717ed8a7154f40dfb71cef4f \
	# TinyMCE
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/TinyMCE $MW_HOME/extensions/TinyMCE \
	&& cd $MW_HOME/extensions/TinyMCE \
	&& git checkout -q 587bbb0b98044ae4904cf67f104d0cf27bd6972d \
	# RandomInCategory
	&& git clone --single-branch -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/RandomInCategory $MW_HOME/extensions/RandomInCategory \
	&& cd $MW_HOME/extensions/RandomInCategory \
	&& git checkout -q 6281429fc91d96cd5c25952984eebd08c1182260 \
	# SimpleMathJax
	&& git clone --single-branch https://github.com/jmnote/SimpleMathJax.git $MW_HOME/extensions/SimpleMathJax \
	&& cd $MW_HOME/extensions/SimpleMathJax \
	&& git checkout -q ddcac9ac1616aed794576f2914ee426879194f0f \
	# Wiretap
	&& git clone https://github.com/enterprisemediawiki/Wiretap.git $MW_HOME/extensions/Wiretap \
	&& cd $MW_HOME/extensions/Wiretap \
	&& git checkout -q a97b708c3093ea66e7cf625859b1b38178526bab \
    # PDFEmbed
    && git clone https://github.com/WolfgangFahl/PDFEmbed.git $MW_HOME/extensions/PDFEmbed \
    && cd $MW_HOME/extensions/PDFEmbed \
    && git checkout -q 04f5712db04cdd6deb28a60858aa16f9a269be72 \
	# LockAuthor
	&& cd $MW_HOME/extensions \
	&& git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/LockAuthor \
	&& cd LockAuthor \
	&& git checkout -b $MW_VERSION ee5ab1ed2bc34ab1b08c799fb1e14e0d5de65953 \
	# EncryptedUploads
	&& cd $MW_HOME/extensions \
	&& git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/EncryptedUploads \
	&& cd EncryptedUploads \
	&& git checkout -b $MW_VERSION 51e3482462f1852e289d5863849b164e1b1a7ea9 \
	# PageExchange, we use master because of compatibility issues of REL1_35 branch of the extension with core 1.35.1 tag
	&& cd $MW_HOME/extensions \
	&& git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/PageExchange \
	&& cd PageExchange \
    && git checkout -b $MW_VERSION 339056ffba8db1a98ff166aa11f639e5bc1ac665 \
	# LinkTarget
	&& cd $MW_HOME/extensions \
	&& git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/LinkTarget \
	&& cd LinkTarget \
	&& git checkout -b $MW_VERSION ab1aba0a4a138f80c4cd9c86cc53259ca0fe4545 \
	# Widgets
	&& cd $MW_HOME/extensions \
	&& git clone -b $MW_VERSION https://gerrit.wikimedia.org/r/mediawiki/extensions/Widgets \
	&& cd Widgets \
	&& git checkout e9ebcb7a60e04a4b6054538032d1d2e1badf9934 \
	&& mkdir -p $MW_ORIGIN_FILES/extensions/Widgets \
	&& mv compiled_templates $MW_ORIGIN_FILES/extensions/Widgets/ \
	&& ln -s $MW_VOLUME/extensions/Widgets/compiled_templates compiled_templates \
	# SimpleTooltip
	&& cd $MW_HOME/extensions \
	&& git clone https://github.com/Fannon/SimpleTooltip.git \
	&& cd SimpleTooltip \
	&& git checkout -b $MW_VERSION 2476bff8f4555f86795c26ca5fdb7db99bfe58d1 \
	# PubmedParser
	&& cd $MW_HOME/extensions \
	&& git clone https://github.com/bovender/PubmedParser.git \
	&& cd PubmedParser \
	&& git checkout -b $MW_VERSION 9cd01d828b23853e3e790dc7bf49cdd230847272 \
	# NCBITaxonomyLookup
	&& cd $MW_HOME/extensions \
    && git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/NCBITaxonomyLookup \
    && cd NCBITaxonomyLookup \
    && git checkout -b $MW_VERSION 512a390a62fbe6f3a7480641f6582126678e5a7c \
    # Skinny
    && cd $MW_HOME/extensions \
    && git clone https://github.com/tinymighty/skinny.git Skinny \
    && cd Skinny \
    && git checkout -b $MW_VERSION 41ba4e90522f6fa971a136fab072c3911750e35c \
    # BreadCrumbs2
    # TODO: update once https://gerrit.wikimedia.org/r/c/mediawiki/extensions/BreadCrumbs2/+/701603 is merged
    && cd $MW_HOME/extensions \
    && git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/BreadCrumbs2.git \
    && cd BreadCrumbs2 \
    && git fetch "https://gerrit.wikimedia.org/r/mediawiki/extensions/BreadCrumbs2" refs/changes/03/701603/1 \
    && git checkout FETCH_HEAD \
    # RottenLinks version 1.0.11
	&& cd $MW_HOME/extensions \
	&& git clone https://github.com/miraheze/RottenLinks.git \
	&& cd RottenLinks \
	&& git checkout -b $MW_VERSION 4e7e675bb26fc39b85dd62c9ad37e29d8f705a41 \
    # EmbedVideo
    && cd $MW_HOME/extensions \
    && git clone https://gitlab.com/hydrawiki/extensions/EmbedVideo.git \
    && cd EmbedVideo \
    && git checkout -b $MW_VERSION 85c5219593cc86367ffb17bfb650f73ca3eb9b11 \
    # Lazyload
    # TODO change me when https://github.com/mudkipme/mediawiki-lazyload/pull/15 will be merged
    && cd $MW_HOME/extensions \
	#	&& git clone https://github.com/mudkipme/mediawiki-lazyload.git Lazyload \
    && git clone https://github.com/WikiTeq/mediawiki-lazyload.git Lazyload \
    && cd Lazyload \
    && git checkout -b $MW_VERSION 92172c30ee5ac764627e397b19eddd536155394e \
    # WikiSEO Dont change me without testing well!
    && cd $MW_HOME/extensions \
    && git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/WikiSEO \
    && cd WikiSEO \
    && git checkout -b $MW_VERSION 30bb8c323e8cd44df52c7537f97f8518de2557df \
    # GoogleDocCreator
    && cd $MW_HOME/extensions \
    && git clone https://github.com/nischayn22/GoogleDocCreator.git \
    && cd GoogleDocCreator \
    && git checkout -b $MW_VERSION 63aecabb4292ad9d4e8336a93aec25f977ee633e \
    # MassPasswordReset
    && cd $MW_HOME/extensions \
    && git clone https://github.com/nischayn22/MassPasswordReset.git \
    && cd MassPasswordReset \
    && git checkout -b $MW_VERSION affaeee6620f9a70b9dc80c53879a35c9aed92c6 \
    # Tabber
    && cd $MW_HOME/extensions \
    && git clone https://gitlab.com/hydrawiki/extensions/Tabber.git \
    && cd Tabber \
    && git checkout -b $MW_VERSION 6c67baf4d18518fa78e07add4c032d62dd384b06 \
    # UploadWizardExtraButtons
    && cd $MW_HOME/extensions \
    && git clone https://github.com/vedmaka/mediawiki-extension-UploadWizardExtraButtons.git UploadWizardExtraButtons \
    && cd UploadWizardExtraButtons \
    && git checkout -b $MW_VERSION accba1b9b6f50e67d709bd727c9f4ad6de78c0c0 \
    # Mendeley
    && cd $MW_HOME/extensions \
    && git clone https://github.com/nischayn22/Mendeley.git \
    && cd Mendeley \
    && git checkout -b $MW_VERSION b866c3608ada025ce8a3e161e4605cd9106056c4 \
    # Scopus
    && cd $MW_HOME/extensions \
    && git clone https://github.com/nischayn22/Scopus.git \
    && cd Scopus \
    && git checkout -b $MW_VERSION 4fe8048459d9189626d82d9d93a0d5f906c43746 \
    # SemanticQueryInterface
    && cd $MW_HOME/extensions \
    && git clone https://github.com/vedmaka/SemanticQueryInterface.git \
    && cd SemanticQueryInterface \
    && git checkout -b $MW_VERSION 0016305a95ecbb6ed4709bfa3fc6d9995d51336f \
    && mv SemanticQueryInterface/* . \
    && rmdir SemanticQueryInterface \
    && ln -s SQI.php SemanticQueryInterface.php \
    && rm -fr .git \
    # SRFEventCalendarMod
    && cd $MW_HOME/extensions \
    && git clone https://github.com/vedmaka/mediawiki-extension-SRFEventCalendarMod.git SRFEventCalendarMod \
    && cd SRFEventCalendarMod \
    && git checkout -b $MW_VERSION e0dfa797af0709c90f9c9295d217bbb6d564a7a8 \
    # Sync
    && cd $MW_HOME/extensions \
    && git clone https://github.com/nischayn22/Sync.git \
    && cd Sync \
    && git checkout -b $MW_VERSION f56b956521f383221737261ad68aef2367466b76 \
    # SemanticExternalQueryLookup (WikiTeq's fork)
    && cd $MW_HOME/extensions \
    && git clone https://github.com/WikiTeq/SemanticExternalQueryLookup.git \
    && cd SemanticExternalQueryLookup \
    && git checkout -b $MW_VERSION dd7810061f2f1a9eef7be5ee09da999cbf9ecd8a \
    # DebugMode, see https://www.mediawiki.org/wiki/Extension:DebugMode
    && git clone --single-branch -b master https://github.com/wikimedia/mediawiki-extensions-DebugMode.git $MW_HOME/extensions/DebugMode \
    && cd $MW_HOME/extensions/DebugMode \
    && git checkout -q ea803a501175fb3009f0fcde7d9168ef8e374399

# GTag1
ADD sources/GTag1.2.0.tar.gz $MW_HOME/extensions/

FROM base as skins
# Skins
# This stage installs all the necessary skins into $MW_HOME/skins & applies their patches
RUN set -x; \
	mkdir -p $MW_HOME/skins \
	&& cd $MW_HOME/skins \
    # CologneBlue, Modern, Refreshed skins
    && git clone -b $MW_VERSION --single-branch https://gerrit.wikimedia.org/r/mediawiki/skins/CologneBlue $MW_HOME/skins/CologneBlue \
    && cd $MW_HOME/skins/CologneBlue \
    && git checkout -q 515a545dfee9f534f74a42057b7a4509076716b4 \
    # MinervaNeue
    && git clone -b $MW_VERSION --single-branch https://gerrit.wikimedia.org/r/mediawiki/skins/MinervaNeue $MW_HOME/skins/MinervaNeue \
    && cd $MW_HOME/skins/MinervaNeue \
    && git checkout -q 6c99418af845a7761c246ee5a50fbb82715f4003 \
    # Modern
    && git clone -b $MW_VERSION --single-branch https://gerrit.wikimedia.org/r/mediawiki/skins/Modern $MW_HOME/skins/Modern \
    && cd $MW_HOME/skins/Modern \
    && git checkout -q d0a04c91132105f712df4de44a99d3643e7afbba \
    # Refreshed
    && git clone -b $MW_VERSION --single-branch https://gerrit.wikimedia.org/r/mediawiki/skins/Refreshed $MW_HOME/skins/Refreshed \
    && cd $MW_HOME/skins/Refreshed \
    && git checkout -q 3fad8765c3ec8082bb899239f502199f651818cb \
	# Pivot
	&& git clone -b v2.3.0 https://github.com/Hutchy68/pivot.git $MW_HOME/skins/pivot \
    && cd $MW_HOME/skins/pivot \
    && git checkout -q -b $MW_VERSION 0d3d6b03a83afd7e1cb170aa41bdf23c0ce3e93b

# TODO send to upstream, see https://wikiteq.atlassian.net/browse/MW-64 and https://wikiteq.atlassian.net/browse/MW-81
COPY patches/skin-refreshed.patch /tmp/skin-refreshed.patch
RUN set -x; \
	cd $MW_HOME/skins/Refreshed \
	&& patch -u -b includes/RefreshedTemplate.php -i /tmp/skin-refreshed.patch

FROM base as source

# MediaWiki core setup
# This stage installs mediawiki core into $MW_HOME & crease all the necessary symlinks & patches
# and imports skins & extensions files from related stages
RUN set -x; \
	git clone --depth 1 -b $MW_CORE_VERSION https://gerrit.wikimedia.org/r/mediawiki/core.git $MW_HOME \
	&& cd $MW_HOME \
	&& git submodule update --init \
	# VisualEditor
	&& cd $MW_HOME/extensions/VisualEditor \
	&& git submodule update --init \
	# Toss directories
	&& mv $MW_HOME/images $MW_ORIGIN_FILES/ \
	&& mv $MW_HOME/cache $MW_ORIGIN_FILES/ \
	&& ln -s $MW_VOLUME/images $MW_HOME/images \
	&& ln -s $MW_VOLUME/cache $MW_HOME/cache

# Skins files from skins stage
COPY --from=skins $MW_HOME/skins $MW_HOME/skins

# Extensions files from extensions stage
COPY --from=extensions $MW_HOME/extensions $MW_HOME/extensions

# Patches
COPY patches /tmp/patches

# WLDR-92, WLDR-125, probably need to be removed if there will be a similar
# change of UserGroupManager on future wiki releases
RUN set -x; \
    cd $MW_HOME \
    && git apply /tmp/patches/ugm.patch

# Resolve composer conflicts for GoogleAnalyticsMetrics extension TODO remove me when update the core or extension
RUN set -x; \
	cd $MW_HOME \
	&& git apply /tmp/patches/core-fix-composer-for-GoogleAnalyticsMetrics.diff

# Fix composer dependencies for MassPasswordReset extension \
# TODO: remove when PR merged https://github.com/nischayn22/MassPasswordReset/pull/1
RUN set -x; \
    cd $MW_HOME/extensions/MassPasswordReset \
    && git apply /tmp/patches/MassPasswordReset.patch

# Cache non frequently changing core packages
# NOTE: the lockfile might need to be updated (not frequently), mainly for major core releases
# just to keep the benefits on this extra step, eg:
#   docker run -it <IMAGE_ID> bash -c 'rm -rf vendor && rm composer.lock \
#       && rm composer.local.json && composer install -q --no-scripts --no-interaction \
#       && --no-autoloader --no-dev --prefer-dist && cat composer.lock' > composer.lock
COPY composer.lock $MW_HOME/composer.lock
RUN set -x; \
    cd $MW_HOME \
    && composer install --no-scripts --no-interaction --no-autoloader --no-dev --prefer-dist

# Install 3rd party composer dependencies from composer.loca.json
# We should run composer update before patches because we also need to patch extensions installed by composer
COPY composer.local.json $MW_HOME/composer.local.json
RUN set -x; \
	cd $MW_HOME \
	&& composer update --no-dev --no-interaction --prefer-dist

# PageForms, PATCHED
RUN set -x; \
	cd $MW_HOME/extensions \
	&& git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/PageForms \
	&& cd PageForms \
	&& git checkout -b $MW_VERSION d2e48e51eef1 \
	&& git apply /tmp/patches/pageforms-xss-cherry-picked.patch

# PATCHES
# Parsoid assertValidUTF8 back-port from 0.13.1
RUN set -x; \
	cd $MW_HOME/vendor/wikimedia/parsoid/src/Utils/ \
	&& patch --verbose --ignore-whitespace --fuzz 3 PHPUtils.php /tmp/patches/parsoid.0.12.1.diff

# SemanticResultFormats, see https://github.com/WikiTeq/SemanticResultFormats/compare/master...WikiTeq:fix1_35
RUN set -x; \
	cd $MW_HOME/extensions/SemanticResultFormats \
	&& patch < /tmp/patches/semantic-result-formats.patch

# Fixes PHP parsoid errors when user replies on a flow message, see https://phabricator.wikimedia.org/T260648#6645078
RUN set -x; \
	cd $MW_HOME/extensions/Flow \
	&& git checkout d37f94241d8cb94ac96c7946f83c1038844cf7e6 \
	&& git apply /tmp/patches/flow-conversion-utils.patch

# SWM maintenance page returns 503 (Service Unavailable) status code, PR: https://github.com/SemanticMediaWiki/SemanticMediaWiki/pull/4967
RUN set -x; \
	cd $MW_HOME/extensions/SemanticMediaWiki \
	&& patch -u -b src/SetupCheck.php -i /tmp/patches/smw-maintenance-503.patch

# TODO: remove for 1.36+, see https://phabricator.wikimedia.org/T281043
RUN set -x; \
    cd $MW_HOME/extensions/SocialProfile \
    && git apply /tmp/patches/social-profile-REL1_35.44b4f89.diff

# WikiTeq's patch allowing to manage fields visibility site-wide
RUN set -x; \
    cd $MW_HOME/extensions/SocialProfile \
    && git apply /tmp/patches/SocialProfile-disable-fields.patch \

RUN set -x; \
     cd $MW_HOME/extensions/CommentStreams \
     && git apply /tmp/patches/CommentStreams.REL1_35.showSearchHitTitle.diff

RUN  set -x; \
     cd $MW_HOME/extensions/DisplayTitle \
     && git apply /tmp/patches/DisplayTitleHooks.fragment.master.patch

# Cleanup all .git leftovers
RUN set -x; \
    cd $MW_HOME \
    && find . \( -name ".git" -o -name ".gitignore" -o -name ".gitmodules" -o -name ".gitattributes" \) -exec rm -rf -- {} +

FROM base as final

COPY --from=source $MW_HOME $MW_HOME
COPY --from=source $MW_ORIGIN_FILES $MW_ORIGIN_FILES

# Default values
ENV MW_AUTOUPDATE=true \
	MW_MAINTENANCE_UPDATE=0 \
	MW_ENABLE_EMAIL=0 \
	MW_ENABLE_USER_EMAIL=0 \
	MW_ENABLE_UPLOADS=0 \
	MW_USE_IMAGE_MAGIC=0 \
	MW_USE_INSTANT_COMMONS=0 \
	MW_EMERGENCY_CONTACT=apache@invalid \
	MW_PASSWORD_SENDER=apache@invalid \
	MW_MAIN_CACHE_TYPE=CACHE_NONE \
	MW_DB_TYPE=mysql \
	MW_DB_SERVER=db \
	MW_DB_USER=root \
	MW_CIRRUS_SEARCH_SERVERS=elasticsearch \
	MW_MAINTENANCE_CIRRUSSEARCH_UPDATECONFIG=1 \
	MW_MAINTENANCE_CIRRUSSEARCH_FORCEINDEX=1 \
	MW_ENABLE_JOB_RUNNER=true \
	MW_JOB_RUNNER_PAUSE=2 \
	MW_ENABLE_TRANSCODER=true \
	MW_JOB_TRANSCODER_PAUSE=60 \
	MW_MAP_DOMAIN_TO_DOCKER_GATEWAY=0 \
	MW_ENABLE_SITEMAP_GENERATOR=false \
	MW_SITEMAP_PAUSE_DAYS=1 \
	PHP_UPLOAD_MAX_FILESIZE=2M \
	PHP_POST_MAX_SIZE=8M \
	PHP_MEMORY_LIMIT=128M \
	LOG_FILES_COMPRESS_DELAY=3600 \
	LOG_FILES_REMOVE_OLDER_THAN_DAYS=10 \
	MW_DEBUG_MODE=false

COPY conf/ssmtp.conf /etc/ssmtp/ssmtp.conf
COPY conf/scan.conf /etc/clamd.d/scan.conf
COPY conf/php/php_memory_limit.ini conf/php/php_max_execution_time.ini conf/php/php_error_reporting.ini conf/php/php_upload_max_filesize.ini /etc/php.d/
COPY conf/apache/mediawiki.conf conf/apache/log.conf /etc/httpd/conf.d/
COPY robots.txt .htaccess /var/www/html/
COPY scripts/run-apache.sh scripts/mwjobrunner.sh scripts/mwsitemapgen.sh scripts/mwtranscoder.sh scripts/monit-slack.sh scripts/rotatelogs-compress.sh scripts/getMediawikiSettings.php /
COPY DockerSettings.php $MW_HOME/DockerSettings.php

# update packages every time!
RUN set -x; \
	yum -y update \
	&& sed -i '/<Directory "\/var\/www\/html">/,/<\/Directory>/ s/AllowOverride None/AllowOverride All/' /etc/httpd/conf/httpd.conf \
	&& chmod -v +x /*.sh \
	&& mkdir $MW_HOME/sitemap \
	&& chown $WWW_USER:$WWW_GROUP $MW_HOME/sitemap \
	&& chmod g+w $MW_HOME/sitemap \
	# Install Monit & monit-slack-hook to watch low disk space
	# The hook will do nothing unless the $MONIT_SLACK_HOOK is provided
	&& echo $'set httpd port 2812 and\n\tuse address localhost\n\tallow localhost' >> /etc/monitrc \
	&& echo $'check filesystem rootfs with path /\n\tif SPACE usage > 90% then exec "/monit-slack.sh"' > /etc/monit.d/hdd \
	# Comment out ErrorLog and CustomLog parameters, we use rotatelogs in mediawiki.conf for the log files
	&& sed -i 's/^\(\s*ErrorLog .*\)/# \1/g' /etc/httpd/conf/httpd.conf \
	&& sed -i 's/^\(\s*CustomLog .*\)/# \1/g' /etc/httpd/conf/httpd.conf

CMD ["/run-apache.sh"]

EXPOSE 80

WORKDIR $MW_HOME

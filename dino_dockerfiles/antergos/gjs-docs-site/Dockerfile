FROM fedora

ENV LANG=en_US.UTF-8 \
	LANGUAGE=en_US.UTF-8 \
	LC_ALL=en_US.UTF-8

RUN dnf update -y \
	&& dnf install -y \
		rubygem-bundler \
		rubygem-thor \
		rubygem-ffi \
		ruby-devel \
		'dnf-command(builddep)' \
	&& dnf builddep -y gobject-introspection \
	&& dnf install -y \
		git \
		redhat-rpm-config \
		gcc \
		gcc-c++ \
		libxml2-devel \
		nodejs \
		python-markdown \
		glib2-devel \
		gtk3-devel \
		webkitgtk4-devel \
		clutter-gtk-devel \
		cairo-devel \
		gstreamer1-devel \
		gstreamer1-plugins-base-devel \
		pango-devel \
		vte3-devel \
		gtksourceview3-devel \
		libappstream-glib-devel \
	&& git clone https://github.com/ptomato/devdocs -b gir-redux --depth=1 /opt/devdocs \
	&& git clone https://github.com/ptomato/gobject-introspection -b wip/ptomato/devdocs --depth=1 /opt/gi \
	&& cd /opt/gi \
	&& ./autogen.sh --enable-doctool \
	&& make install \
	&& export G_IR_DOC_TOOL=/usr/local/bin/g-ir-doc-tool \
	&& cd /opt/devdocs \
	&& sed -i s/2.3.0/2.3.3/ Gemfile \
	&& bundle install \
	&& thor gir:generate_all \
	&& thor docs:list \
	&& \
		for docset in \
			appstreamglib10 atk10 atspi20 cairo10 cally10 clutter10 cluttergdk10 clutterx1110 \
			cogl20 coglpango20 fontconfig20 freetype220 gdk30 gdkpixbuf20 gdkx1130 gio20 \
			girepository20 glib20 gmodule20 gobject20 gst10 gstallocators10 gstapp10 \
			gstaudio10 gstbase10 gstcheck10 gstcontroller10 gstfft10 gstnet10 gstpbutils10 \
			gstrtp10 gstrtsp10 gstsdp10 gsttag10 gstvideo10 gtk30 gtkclutter10 gtksource30 \
			javascript json10 libxml220 pango10 pangocairo10 pangoft210 pangoxft10 soup24 \
			soupgnome24 vte290 webkit240 webkit2webextension40 win3210 xfixes40 xft20 xlib20 \
			xrandr13; \
		do thor docs:generate $docset --force; done \
	&& dnf remove -y \
		git \
		redhat-rpm-config \
		gcc \
		gcc-c++ \
		libxml2-devel \
		'dnf-command(builddep)' \
		python-markdown \
		glib2-devel \
		gtk3-devel \
		webkitgtk4-devel \
		clutter-gtk-devel \
		cairo-devel \
		gstreamer1-devel \
		gstreamer1-plugins-base-devel \
		pango-devel \
		vte3-devel \
		gtksourceview3-devel \
		libappstream-glib-devel \
	&& dnf clean -y all \
	&& rm -rf /opt/gi

EXPOSE 9292
WORKDIR /opt/devdocs
CMD rackup -o 0.0.0.0

LABEL \
	org.label-schema.schema-version="1.0" \
	org.label-schema.vendor="Antergos Linux Project" \
	org.label-schema.name="GJS DevDocs Site" \
	org.label-schema.version="1.0" \
	org.label-schema.description="GJS/GI API Documentation Site"


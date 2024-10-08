# TODO: move to gtk4-update-icon-cache
Summary:	GNOME Chess - a 2D/3D chess interface
Summary(pl.UTF-8):	GNOME Chess - dwu i trójwymiarowy interfejs do szachów
Name:		gnome-chess
Version:	47.0
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/gnome-chess/47/%{name}-%{version}.tar.xz
# Source0-md5:	d51ce935d14d646a60ba63166dfb3889
URL:		https://wiki.gnome.org/Apps/Chess
BuildRequires:	AppStream
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.44.0
BuildRequires:	gtk4-devel >= 4.10
BuildRequires:	libadwaita-devel >= 1.5
BuildRequires:	librsvg-devel >= 1:2.46.0
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.10
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.35.7
BuildRequires:	vala-libadwaita >= 1.5
BuildRequires:	vala-librsvg >= 1:2.46.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.44.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.44.0
Requires:	gtk4 >= 4.10
Requires:	hicolor-icon-theme
Requires:	libadwaita >= 1.5
Requires:	librsvg >= 1:2.46.0
Suggests:	crafty
Suggests:	gnuchess
Provides:	gnome-games-glchess = 1:%{version}-%{release}
Obsoletes:	glchess < 1.0.7
Obsoletes:	gnome-games-glchess < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Chess is a 2D/3D chess game interfacing via the Chess Engine
Communication Protocol (CECP) by Tim Mann. This means it can currently
use engines such as GNUChess, Sjeng, Faile, Amy, Crafty and Phalanx.

%description -l pl.UTF-8
GNOME Chess to dwu i trójwymiarowa gra w szachy komunikująca się za
pomocą protokołu CECP (Chess Engine Communication Protocol) Tima
Manna. Oznacza to, że aktualnie może używać silników takich jak
GNUChess, Sjeng, Faile, Amy, Crafty i Phalanx.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_bindir}/gnome-chess
%dir %{_sysconfdir}/gnome-chess
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnome-chess/engines.conf
%{_datadir}/dbus-1/services/org.gnome.Chess.service
%{_datadir}/glib-2.0/schemas/org.gnome.Chess.gschema.xml
%{_datadir}/metainfo/org.gnome.Chess.appdata.xml
%{_desktopdir}/org.gnome.Chess.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Chess.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Chess-symbolic.svg
%{_mandir}/man6/gnome-chess.6*

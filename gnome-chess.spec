Summary:	GNOME Chess - a 2D/3D chess interface
Summary(pl.UTF-8):	GNOME Chess - dwu i trójwymiarowy interfejs do szachów
Name:		gnome-chess
Version:	3.18.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-chess/3.18/%{name}-%{version}.tar.xz
# Source0-md5:	ada63751e7e0e1d843e5a4683757e0e2
URL:		https://wiki.gnome.org/Apps/Chess
BuildRequires:	appstream-glib-devel
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.40.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.15.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	librsvg-devel >= 2.32.0
BuildRequires:	libtool >= 2:2.2
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.27.1
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	glib2 >= 1:2.40.0
Requires(post,postun):	gtk-update-icon-cache
Requires:	glib2 >= 1:2.40.0
Requires:	gtk+3 >= 3.15.0
Requires:	hicolor-icon-theme
Requires:	librsvg >= 2.32.0
Suggests:	crafty
Suggests:	gnuchess
Provides:	gnome-games-glchess = 1:%{version}-%{release}
Obsoletes:	glchess
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
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc NEWS
%attr(755,root,root) %{_bindir}/gnome-chess
%{_datadir}/appdata/gnome-chess.appdata.xml
%{_datadir}/gnome-chess
%{_datadir}/glib-2.0/schemas/org.gnome.chess.gschema.xml
%dir %{_sysconfdir}/gnome-chess
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gnome-chess/engines.conf
%{_desktopdir}/gnome-chess.desktop
%{_iconsdir}/hicolor/*/apps/gnome-chess.png
%{_iconsdir}/hicolor/scalable/apps/gnome-chess-symbolic.svg
%{_mandir}/man6/gnome-chess.6*

Summary:	GNOME chess - graphical chess interface
Summary(pl.UTF-8):	GNOME chess - graficzny interfejs do programów szachowych
Name:		gnome-chess
Version:	0.4.0
Release:	0.1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-chess/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	c754bb9686d99fc0c038754963c3fea4
Patch0:		%{name}-desktop.patch
URL:		http://primates.ximian.com/~jpr/gnome-chess/
BuildRequires:	GConf2-devel >= 2.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.5
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.0.0
BuildRequires:	libgnomecanvas-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
#BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.10.15
Requires(post,postun):	GConf2 >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME Chess is part of the GNOME project and is a graphical chess
interface. It can provide and interface to GNU Chess, Crafty, chess
servers and PGN files.

%description -l pl.UTF-8
GNOME Chess to graficzny interfejs do programów szachowych. Działa z
programami GNU Chess i Crafty, obsługuje serwery szachowe i plik PGN.
GNOME Chess jest częścią projektu GNOME.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/mime-info
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gnome-chess.schemas

%postun
%gconf_schema_uninstall gnome-chess.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gnome-chess
%{_datadir}/gnome-chess
%{_sysconfdir}/gconf/schemas/gnome-chess.schemas
%{_pixmapsdir}/gnome-chess.png
%{_pixmapsdir}/gnome-chess
%{_desktopdir}/gnome-chess.desktop
# temporarily disabled
#%{_omf_dest_dir}/%{name}

Summary:	GNOME chess - graphical chess interface
Summary(pl):	GNOME chess - graficzny interfejs do programów szachowych
Name:		gnome-chess
Version:	0.3.3
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-chess/%{name}-%{version}.tar.bz2
Patch0:		%{name}-missing_sgmldocs.make.patch
Patch1:		%{name}-quit.patch
Patch2:		%{name}-mime.patch
Icon:		gnome-chess.gif
BuildRequires:	ORBit-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	libglade-devel
BuildRequires:	libtool
URL:		http://primates.ximian.com/~jpr/gnome-chess/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNOME Chess is part of the GNOME project and is a graphical chess
interface. It can provide and interface to GNU Chess, Crafty, chess
servers and PGN files.

%description -l pl
GNOME Chess to graficzny interfejs do programów szachowych. Dzia³a z
programami GNU Chess i Crafty, obs³uguje serwery szachowe i plik PGN.
GNOME Chess jest czê¶ci± projektu GNOME.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
gettextize --copy --force
aclocal -I macros
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games/Board

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_datadir}/mime-info/*
%{_applnkdir}/Games/Board/*

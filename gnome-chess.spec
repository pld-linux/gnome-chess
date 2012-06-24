Summary:	GNOME chess - graphical chess interface
Summary(pl):	GNOME chess - graficzny interfejs do program�w szachowych
Name:		gnome-chess
Version:	0.3.3
Release:	2
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Source0:	ftp://ftp.gnome.org/pub/GNOME/stable/sources/gnome-chess/%{name}-%{version}.tar.bz2
Patch0:		%{name}-missing_sgmldocs.make.patch
Patch1:		%{name}-quit.patch
Patch2:		%{name}-mime.patch
Icon:		gnome-chess.gif
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gdk-pixbuf-devel >= 0.8.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libglade-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	perl
URL:		http://primates.ximian.com/~jpr/gnome-chess/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNOME Chess is part of the GNOME project and is a graphical chess
interface. It can provide and interface to GNU Chess, Crafty, chess
servers and PGN files.

%description -l pl
GNOME Chess to graficzny interfejs do program�w szachowych. Dzia�a z
programami GNU Chess i Crafty, obs�uguje serwery szachowe i plik PGN.
GNOME Chess jest cz�ci� projektu GNOME.

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
gzip -9nf AUTHORS NEWS README TODO
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_datadir}/gnome-chess
%{_datadir}/mime-info/*
%{_datadir}/omf/*
%{_applnkdir}/Games/Board/*

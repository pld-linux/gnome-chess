Summary:	GNOME chess
Name:		gnome-chess
Version:	0.2.4
Release:	3
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.gnome.org/pub/gnome-chess/%{name}-%{version}.tar.gz
Icon:		gnome-chess.gif
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNOME Chess is part of the GNOME project and is a graphical chess
interface. It can provide and interface to GNU Chess, Crafty, chess
servers and PGN files.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_applnkdir}/Games/*

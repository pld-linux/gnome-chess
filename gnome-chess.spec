Summary:	GNOME chess
Name:		gnome-chess
Version:	0.2.4
Release:	2
License:	GPL
Group:		X11/GNOME
Group(pl):	X11/GNOME
Source:		ftp://ftp.gnome.org/pub/gnome-chess/%{name}-%{version}.tar.gz
Patch:		gnome-chess-applnk.patch
Icon:		gnome-chess.gif
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	ORBit-devel
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
GNOME Chess is part of the GNOME project and is a graphical chess
interface. It can provide and interface to GNU Chess, Crafty, chess servers
and PGN files.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
automake
LDFAGS="-s"; export LDFAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)

%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/mime-info/*
%{_datadir}/applnk/Games/*

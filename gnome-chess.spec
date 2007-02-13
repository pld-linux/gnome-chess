Summary:	GNOME chess - graphical chess interface
Summary(pl.UTF-8):	GNOME chess - graficzny interfejs do programów szachowych
Name:		gnome-chess
Version:	0.3.3
Release:	8
License:	GPL
Group:		X11/Applications/Games
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/gnome-chess/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	baca55b944140d7764af88da1167835e
Patch0:		%{name}-missing_sgmldocs.make.patch
Patch1:		%{name}-quit.patch
Patch2:		%{name}-mime.patch
Patch3:		%{name}-omf.patch
Patch4:		%{name}-desktop.patch
URL:		http://primates.ximian.com/~jpr/gnome-chess/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gdk-pixbuf-gnome-devel >= 0.8.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libglade-gnome-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _omf_dest_dir   %(scrollkeeper-config --omfdir)

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
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__gettextize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Gamesdir=%{_applnkdir}/Games/Board \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/bin/scrollkeeper-update
%postun	-p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_datadir}/gnome-chess
%{_datadir}/mime-info/*
%{_omf_dest_dir}/%{name}
%{_applnkdir}/Games/Board/*

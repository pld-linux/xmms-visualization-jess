Summary:	Plugin which draws graphic.
Summary(pl):	Plugin wizualizacji graficznej.
Name:		xmms-visualization-jess
Version:	2.0.0
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://arquier.free.fr/jess-%{version}.tar.gz
URL:		http://arquier.free.fr/
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRequires:	SDL-devel >= 1.1.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Plugin which draw lines, curves, and 3D grid moving in concordance with the music.

%description -l pl
Wtyczka rysuj±ce linie, krzywe oraz grafikê 3D w koordynacji z muzyk±.

%prep
%setup -q -n jess-%{version}

%build
%{__make} \
	COMMON_CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} \
	-ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/

./libtool install libjess.la \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config	--visualization-plugin-dir`/libjess.la
install .libs/libjess.so.*.*.* \
	$RPM_BUILD_ROOT/`%{_bindir}/xmms-config	--visualization-plugin-dir`/libjess.so

gzip -9nf AUTHORS NEWS README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%attr(755,root,root) %{_libdir}/xmms/*/*.la

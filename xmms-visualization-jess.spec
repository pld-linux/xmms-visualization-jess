Summary:	Plugin which draws graphics
Summary(pl):	Plugin wizualizacji graficznej
Name:		xmms-visualization-jess
Version:	2.0.0
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://arquier.free.fr/jess-%{version}.tar.gz
# Source0-md5:	59f2586b960b74e4259f8ca77d416a43
Patch0:		%{name}-usleep.patch
URL:		http://arquier.free.fr/
BuildRequires:	SDL-devel >= 1.1.8
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plugin which draw lines, curves, and 3D grid moving in concordance
with the music.

%description -l pl
Wtyczka rysuj±ca linie, krzywe oraz grafikê 3D w koordynacji z muzyk±.

%prep
%setup -q -n jess-%{version}
%patch0 -p1

%build
%{__make} \
	COMMON_CFLAGS="%{rpmcflags} -ffast-math `glib-config --cflags`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{xmms_visualization_plugindir}

./libtool install libjess.la \
	$RPM_BUILD_ROOT%{xmms_visualization_plugindir}/libjess.la
install .libs/libjess.so.*.*.* \
	$RPM_BUILD_ROOT%{xmms_visualization_plugindir}/libjess.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
%{xmms_visualization_plugindir}/*.la

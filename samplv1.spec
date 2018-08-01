Summary:	Old-school polyphonic sampler
Name:		samplv1
Version:	0.9.2
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://downloads.sourceforge.net/samplv1/%{name}-%{version}.tar.gz
# Source0-md5:	163d71378699a8c17affefadf52dc3ee
URL:		https://samplv1.sourceforge.io/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	liblo-devel
BuildRequires:	libsndfile-devel
BuildRequires:	lv2-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-linguist
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
samplv1 is an old-school all-digital polyphonic sampler synthesizer
with stereo fx.

Features:

    - a pure stand-alone JACK client with JACK-session, NSM (Non Session
      management) and both JACK MIDI and ALSA MIDI input support;
    - a LV2 instrument plug-in.

%package common
Summary:	Old-school polyphonic sampler - common files
Group:		Applications

%description common
samplv1 is an old-school all-digital polyphonic sampler synthesizer
with stereo fx.

%package jack
Summary:	Old-school polyphonic sampler - standalone Jack app
Group:		Applications
Requires:	%{name}-common = %{version}-%{release}

%description jack
samplv1 is an old-school all-digital polyphonic sampler synthesizer
with stereo fx.

This package provides a pure stand-alone JACK client with
JACK-session, NSM (Non Session management) and both JACK MIDI and ALSA
MIDI input support.

%package lv2
Summary:	Old-school polyphonic sampler - LV2 plug-in
Group:		Applications
Requires:	%{name}-common = %{version}-%{release}

%description lv2
samplv1 is an old-school all-digital polyphonic sampler synthesizer
with stereo fx.

This package provides an a LV2 instrument plug-in.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}

%configure \
	--with-qt5=%{_libdir}/qt5

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/fr/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.so
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/samplv1.fr.1.gz $RPM_BUILD_ROOT%{_mandir}/fr/man1/samplv1.1.gz

# enable 'Requires' detection
chmod a+x $RPM_BUILD_ROOT%{_libdir}/lv2/%{name}.lv2/*.so

%post common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsamplv1.so.0.*
%ghost %attr(755,root,root) %{_libdir}/libsamplv1.so.0
%attr(755,root,root) %{_libdir}/libsamplv1_ui.so.0.*
%ghost %attr(755,root,root) %{_libdir}/libsamplv1_ui.so.0

%files jack
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/%{name}_jack
%{_desktopdir}/samplv1.desktop
%{_iconsdir}/hicolor/*/apps/samplv1.png
%{_iconsdir}/hicolor/scalable/apps/samplv1.svg
%{_iconsdir}/hicolor/*/mimetypes/application-x-samplv1-preset.png
%{_iconsdir}/hicolor/scalable/mimetypes/application-x-samplv1-preset.svg
%{_mandir}/man1/samplv1.1*
%lang(fr) %{_mandir}/fr/man1/samplv1.1*
%{_datadir}/metainfo/samplv1.appdata.xml
%{_datadir}/mime/packages/samplv1.xml

%files lv2
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%dir %{_libdir}/lv2/%{name}.lv2
%{_libdir}/lv2/%{name}.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/%{name}.lv2/*.so

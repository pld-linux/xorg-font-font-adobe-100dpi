# $Rev: 3190 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-adobe-100dpi
Summary(pl):	font-adobe-100dpi
Name:		xorg-font-font-adobe-100dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-adobe-100dpi-%{version}.tar.bz2
# Source0-md5:	a54f67c67177d2759efe92ad1f68a162
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-adobe-100dpi-%{version}-root-%(id -u -n)

%description
font-adobe-100dpi

%description -l pl
font-adobe-100dpi


%prep
%setup -q -n font-adobe-100dpi-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/100dpi/*

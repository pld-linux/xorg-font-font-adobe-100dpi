Summary:	Adobe 100dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe Adobe 100dpi
Name:		xorg-font-font-adobe-100dpi
Version:	1.0.4
Release:	1
License:	MIT
Group:		Fonts
Source0:	https://xorg.freedesktop.org/releases/individual/font/font-adobe-100dpi-%{version}.tar.xz
# Source0-md5:	20239f6f99ac586f10360b0759f73361
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 1.4
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adobe 100dpi bitmap fonts: Courier, Helvetica, New Century Schoolbook,
Symbol and Times.

This package includes Unicode fonts as well as in ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-9, ISO-8859-10,
ISO-8859-13, ISO-8859-14 and ISO-8859-15 encodings.

%description -l pl.UTF-8
Fonty bitmapowe Adobe 100dpi: Courier, Helvetica, New Century
Schoolbook, Symbol i Times.

Ten pakiet zawiera fonty unikodowe, a także w kodowaniach ISO-8859-1,
ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-9, ISO-8859-10,
ISO-8859-13, ISO-8859-14 i ISO-8859-15.

%prep
%setup -q -n font-adobe-100dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if "%{_gnu}" != "-gnux32"
	--build=%{_host} \
	--host=%{_host} \
%endif
	--with-fontdir=%{_fontsdir}/100dpi

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst 100dpi

%postun
fontpostinst 100dpi

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%{_fontsdir}/100dpi/cour*.pcf.gz
%{_fontsdir}/100dpi/helv*.pcf.gz
%{_fontsdir}/100dpi/ncen*.pcf.gz
%{_fontsdir}/100dpi/symb*.pcf.gz
%{_fontsdir}/100dpi/tim*.pcf.gz

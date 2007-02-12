Summary:	adobe-100dpi font
Summary(pl.UTF-8):	Font adobe-100dpi
Name:		xorg-font-font-adobe-100dpi
Version:	1.0.0
Release:	0.1
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/font/font-adobe-100dpi-%{version}.tar.bz2
# Source0-md5:	443acfe70e26716282f9068730fe92c4
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util >= 0.99.2
BuildRequires:	xorg-util-util-macros
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/100dpi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
adobe-100dpi font.

%description -l pl.UTF-8
Font adobe-100dpi.

%prep
%setup -q -n font-adobe-100dpi-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
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
%doc COPYING ChangeLog
%{_fontsdir}/100dpi/*.pcf.gz

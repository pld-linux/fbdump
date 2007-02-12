Summary:	fbdump - takes screenshots using the framebuffer device
Summary(pl.UTF-8):	Narzędzie zrzucające zawartość ekranu do pliku poprzez framebuffer
Name:		fbdump
Version:	0.4.1
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.rcdrummond.net/fbdump/%{name}-src-%{version}.tar.gz
# Source0-md5:	496ac25414f2077fcc3adc62e53fb40f
URL:		http://www.rcdrummond.net/fbdump/index.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fbdump reads the framebuffer device (/dev/fb*) or a dump thereof and
saves a PPM image file. You can use it for making screenshots of
virtually any application, from traditional text applications to your
X Window System desktop, as well as framebuffer applications.

%description -l pl.UTF-8
fbdump czyta urządzenie framebuffera (/dev/fb*) lub zrzut z niego i
zapisuje zawartość do pliku graficznego PPM. Programu można używać
do robienia zrzutów ekranu z każdej aplikacji, od tradycyjnych
aplikacji tekstowych do ekranu X Window System, a także aplikacji
framebufferowych.

%prep
%setup -q

%build
%configure
#	--enable-vga16fb
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*

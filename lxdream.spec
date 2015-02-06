Name:		lxdream
Version:	0.9.1
Release:	4
Summary:	Sega Dreamcast emulator
License:	GPLv2+
Group:		Emulators
URL:		http://www.lxdream.org
Source0:	%{name}-%{version}.tar.gz
#http://www.lxdream.org/count.php?file=%{name}-%{version}.tar.gz
Patch0:		lxdream-0.9.1-plf-undefined-ok-for-plugins.patch
Patch1:		lxdream-0.9.1-glib.patch
Patch2:		lxdream-0.9.1-linking.patch
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	desktop-file-utils

%description
Lxdream is a Sega Dreamcast emulator.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%configure 
%install
%makeinstall

# xdg menus
install -m 644 lxdream.desktop \
  %{buildroot}%{_datadir}/applications/lxdream.desktop

desktop-file-install --vendor="" \
  --remove-category="Game" \
  --add-category="Emulator" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

#locales
%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog
%{_bindir}/lxdream
%{_libdir}/lxdream
%{_datadir}/applications/lxdream.desktop
%{_datadir}/pixmaps/lxdream*
%{_mandir}/man1/lxdream.1*
%config(noreplace) %{_sysconfdir}/lxdreamrc



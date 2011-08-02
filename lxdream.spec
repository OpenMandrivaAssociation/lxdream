Name:			lxdream
Version:		0.9.1
Release:		%mkrel 2

Summary:	Sega Dreamcast emulator
License:	GPLv2+
Group:		Emulators
URL:		http://www.lxdream.org
Source0:	%{name}-%{version}.tar.gz
#http://www.lxdream.org/count.php?file=%{name}-%{version}.tar.gz
Patch0:		lxdream-0.9.1-plf-undefined-ok-for-plugins.patch

BuildRequires:	SDL-devel
BuildRequires:	mesagl-devel
BuildRequires:	gtk2-devel
BuildRequires:	pulseaudio-devel
BuildRequires:	lirc-devel
BuildRequires:	zlib-devel
BuildRequires:	png-devel
BuildRequires:	alsa-lib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Lxdream is a Sega Dreamcast emulator.

%prep
%setup -q
%patch0 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
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
%defattr(-,root,root)
%doc ChangeLog
%{_bindir}/lxdream
%{_libdir}/lxdream
%{_datadir}/applications/lxdream.desktop
%{_datadir}/pixmaps/lxdream*
%{_mandir}/man1/lxdream.1*
%config(noreplace) %{_sysconfdir}/lxdreamrc

%clean
rm -rf %{buildroot}


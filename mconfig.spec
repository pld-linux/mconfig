Summary:	Tool to configure the linux kernel
Summary(pl):	Narzêdzie do konfiguracji j±dra Linuksa
Name:		mconfig
Version:	0.20
Release:	1
License:	GPL
Group:		Base/Kernel
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/hch/mconfig/%{name}-%{version}.tar.bz2
URL:		ftp://ftp.openlinux.org/pub/people/hch/mconfig/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool is used to create configuration file for compiling a Linux
kernel. It offers various different modes.

%description -l pl
To narzêdzie jest u¿ywane do tworzenia pliku konfiguracyjnego do
kompilacji j±dra Linuksa. Oferuje ró¿ne dziwne tryby.

%prep
%setup -q -b 0

%build
%{__autoconf}
%configure
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog doc/CHANGES.mec doc/TODO.mec
%attr(755,root,root) %{_bindir}/mconfig
%{_mandir}/man1/*

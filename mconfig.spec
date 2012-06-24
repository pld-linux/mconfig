Name:		mconfig
Version:	0.20
Release:	1
Group:		Base/Kernel
Group(de):	Grunds�tzlich/Kern
Group(pl):	Podstawowe/J�dro
Summary:	Tool to configure the linux kernel
Summary(pl):	Narz�dzie do konfiguracji linuxowego kernela
License:	GPL
URL:		ftp://ftp.openlinux.org/pub/people/hch/mconfig/
Source0:	ftp://ftp.kernel.org/pub/linux/kernel/people/hch/mconfig/%{name}-%{version}.tar.bz2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This tool is used to create configuration file for compiling a Linux
kernel. It offers various different modes.

%description -l pl
To narz�dzie jest u�ywane do tworzenia pliku konfiguracyjnego do kompilacji
j�dra Linux'a. Oferuje r�ne dziwne tryby.

%prep
%setup -q -b 0

%build
autoconf
%configure
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS COPYING INSTALL NEWS README ChangeLog doc/CHANGES.mec doc/TODO.mec

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mconfig
%{_mandir}/man1/*
%doc {AUTHORS,COPYING,INSTALL,NEWS,README,ChangeLog,doc/CHANGES.mec,doc/TODO.mec}.gz

%clean
rm -rf $RPM_BUILD_ROOT

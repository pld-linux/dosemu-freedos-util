Summary:	Utilities for FreeDOS
Summary(pl.UTF-8):	Programy użytkowe dla DOS-a
Name:		dosemu-freedos-util
Version:	beta7h03
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/%{version}/EN/disksets/util1.zip
# Source0-md5:	fdeb5faa6e0f4f3a925901daaa2ef4ea
Source1:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/%{version}/EN/disksets/util2.zip
# Source1-md5:	f18cdd08a2ac3418e037aae97ceead09
URL:		http://www.freedos.org/
BuildRequires:	unzip
Obsoletes:	dosemu-freedos
Requires:	dosemu
Requires:	dosemu-freedos-minimal
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various utilities for DOS.

%description -l pl.UTF-8
Różne programy użytkowe dla DOS-a.

%prep
%setup -q -c -a1

rm -rf freedos
mkdir freedos
for i in *.ZIP ; do
	unzip -L -o $i -d freedos
done
rm -f freedos/copying freedos/bin/cwsdpmi.exe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

cp -Rf freedos $RPM_BUILD_ROOT/var/lib/dosemu/bootdir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/var/lib/dosemu/bootdir/freedos/bin/*
/var/lib/dosemu/bootdir/freedos/doc/*
/var/lib/dosemu/bootdir/freedos/help/*
/var/lib/dosemu/bootdir/freedos/nls/*

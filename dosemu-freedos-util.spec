Summary:	Utilities for FreeDOS
Summary(pl):	Programy u¿ytkowe dla DOSa
Name:		dosemu-freedos-util
Version:	beta7h01
Release:	2
Epoch:		1
License:	GPL
Group:		Applications/Emulators
Group(de):	Applikationen/Emulators
Group(pl):	Aplikacje/Emulatory
Source0:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/beta7h01/EN/full/disksets/util1.zip
Source1:	ftp://ftp.task.gda.pl/pub/dos/freedos/files/distributions/ripcord/beta7h01/EN/full/disksets/util2.zip
URL:		http://www.freedos.org/
BuildRequires:	unzip
Obsoletes:	dosemu-freedos
Requires:	dosemu
Exclusivearch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Various utilities for DOS.

%description -l pl
Ró¿ne u¿ytki dla DOSa.

%prep
%setup -c %{name} -q -a1

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
/var/lib/dosemu/bootdir/freedos/*

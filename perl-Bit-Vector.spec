%include	/usr/lib/rpm/macros.perl
Summary:	Bit-Vector perl module
Summary(pl):	Modu� perla Bit-Vector
Name:		perl-Bit-Vector
Version:	6.0
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bit/Bit-Vector-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit-Vector - efficient base class implementing bit vectors.

%description -l pl
Modu� perla Bit-Vector.

%prep
%setup -q -n Bit-Vector-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/Bit/Vector.pm
%dir %{perl_sitearch}/auto/Bit/Vector
%{perl_sitearch}/auto/Bit/Vector/Vector.bs
%attr(755,root,root) %{perl_sitearch}/auto/Bit/Vector/Vector.so
%{_mandir}/man3/*

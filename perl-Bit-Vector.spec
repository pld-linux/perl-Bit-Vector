%include	/usr/lib/rpm/macros.perl
Summary:	Bit-Vector perl module
Summary(pl):	Modu³ perla Bit-Vector
Name:		perl-Bit-Vector
Version:	5.7
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Bit/Bit-Vector-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit-Vector - efficient base class implementing bit vectors.

%description -l pl
Modu³ perla Bit-Vector.

%prep
%setup -q -n Bit-Vector-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/Bit/Vector/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Bit/Vector
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        *txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES.txt,CREDITS.txt,README.txt}.gz

%{perl_sitearch}/Bit/Vector.pm

%dir %{perl_sitearch}/auto/Bit/Vector
%{perl_sitearch}/auto/Bit/Vector/.packlist
%{perl_sitearch}/auto/Bit/Vector/Vector.bs
%attr(755,root,root) %{perl_sitearch}/auto/Bit/Vector/Vector.so

%{_mandir}/man3/*

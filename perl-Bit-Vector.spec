#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Bit
%define		pnam	Vector
Summary:	Bit::Vector Perl module
Summary(cs):	Modul Bit::Vector pro Perl
Summary(da):	Perlmodul Bit::Vector
Summary(de):	Bit::Vector Perl Modul
Summary(es):	Módulo de Perl Bit::Vector
Summary(fr):	Module Perl Bit::Vector
Summary(it):	Modulo di Perl Bit::Vector
Summary(ja):	Bit::Vector Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Bit::Vector ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Bit::Vector
Summary(pl):	Modu³ Perla Bit::Vector
Summary(pt):	Módulo de Perl Bit::Vector
Summary(pt_BR):	Módulo Perl Bit::Vector
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Bit::Vector
Summary(sv):	Bit::Vector Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Bit::Vector
Summary(zh_CN):	Bit::Vector Perl Ä£¿é
Name:		perl-Bit-Vector
Version:	6.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6.1
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit::Vector - efficient base class implementing bit vectors.

%description -l pl
Modu³ perla Bit::Vector - wydajna klasa bazowa do implementowania
wektorów bitowych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm -f GNU_{,L}GPL.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt
%{perl_sitearch}/Bit/Vector.pm
%dir %{perl_sitearch}/Bit/Vector
%{perl_sitearch}/Bit/Vector/Overload.pm
%dir %{perl_sitearch}/Carp
%{perl_sitearch}/Carp/Clan.pm
%dir %{perl_sitearch}/auto/Bit/Vector
%{perl_sitearch}/auto/Bit/Vector/Vector.bs
%attr(755,root,root) %{perl_sitearch}/auto/Bit/Vector/Vector.so
%{_mandir}/man3/*

#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Bit
%define		pnam	Vector
Summary:	Bit::Vector - efficient base class implementing bit vectors
Summary(cs):	Bit::Vector - modul pro vysoce vıkonné manipulace bitovıch vektorù v Perlu
Summary(da):	Bit::Vector - et modul for højydelsehåndtering af bitvektorer i Perl
Summary(de):	Bit::Vector - ein Modul für das leistungsstarke Bearbeiten von bit-Vektoren durch Perl
Summary(es):	Bit::Vector - módulo para la manipulación Perl de alta ejecución de muchos vectores
Summary(fr):	Bit::Vector - module de manipulation Perl à haute performance de vecteurs bits
Summary(it):	Bit::Vector - modulo per la gestione dei vettori bit ad alte prestazioni con Perl
Summary(ja):	Bit::Vector ¥Ó¥Ã¥È¥Ù¥¯¥È¥ë¤Î¥Ï¥¤¥Ñ¥Õ¥©¡¼¥Ş¥ó¥¹PerlÁàºî¤Î°Ù¤Î¥â¥¸¥å¡¼¥ë¤Ç¤¹¡£
Summary(ko):	Bit::Vector bit º¤ÅÍ¸¦ °í¼º´É Perl Á¶ÀÛÇÏ´Âµ¥ »ç¿ëµÇ´Â ¸ğµâ
Summary(pl):	Bit::Vector - wydajna klasa bazowa implementuj±ca wektory bitowe
Summary(pt):	Bit::Vector - um módulo para a manipulação rápida em Perl de vectores de "bits"
Summary(pt_BR):	Bit::Vector - um módulo para a manipulação rápida em Perl de vectores de "bits"
Summary(sv):	Bit::Vector - en modul för högprestandahantering av bitvektorer i Perl
Summary(tr):	Bit::Vector - bit matrislerinin yüksek başarımlı hesaplamaları için bir Perl modülü
Summary(zh_CN):	Bit::Vector - ¶ÔÎ»ÏòÁ¿½øĞĞ¸ßĞÔÄÜ Perl ²Ù×÷µÄÄ£¿é¡£
Name:		perl-Bit-Vector
Version:	6.3
Release:	3
# same as perl or (C library only) LGPL
License:	GPL v1+ or Artistic or (C library only) LGPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8b2bd3bf6fe5b0de4cbeaf0621b969f5
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit::Vector is an efficient C library which allows you to handle bit
vectors, sets (of integers), "big integer arithmetic" and boolean
matrices, all of arbitrary sizes.

The library is efficient (in terms of algorithmical complexity) and
therefore fast (in terms of execution speed) for instance through the
widespread use of divide-and-conquer algorithms.

%description -l cs
Bit::Vector je efektivní knihovna v C, která vám umo¾òuje zpracovávat
vektory bitù, mno¾iny (celıch èísel), "aritmetiku velkıch èísel" a
matice booleovskıch hodnot, v¹e pro libovolné velikosti.

Knihovna je efektivní (my¹lena slo¾itost algoritmù) a proto rychlá
(my¹lena rychlost provádìní) napøíklad roz¹íøenım pou¾itím algoritmù
rozdìl a panuj.

%description -l da
Bit::Vector er et effekivt C-bibliotek som lader dig håndtere
bitvektorer, mængder (af heltal), aritmetik for store heltal og
booleske matricer, alt med vilkårlige størrelser.

Biblioteket er effektivt (forstået som algoritmkompleksitet) og derfor
hurtigt (forstået som eksekveringshastighed) blandt andet ved en
omfattende brug af del-og-hersk-algoritmer.

%description -l de
Bit::Vector ist eine leistungsfähige C-Bibliothek, mit der Sie bit-
Vektoren, Sätze (von ganzen Zahlen), "große, ganze arithmetische" und
boolesche Matrizen einer beliebigen Größe bearbeiten können.

Diese Bibliothek ist sehr leistungsstark (in Bezug auf ihre
algorithmische Komplexität) und daher auch sehr schnell (in Bezug auf
die Ausführungsgeschwindigkeit), beispielsweise im verbreiteten
Gebrauch von divide-and-conquer Algorithmen.

%description -l es
Bit::Vector es una librería C eficiente que le permiten gestionar
muchos vectores, grupos (de números enteros), "big integer arithmetic"
y matrices boolean, todos los tamaños arbitrarios.

La librería es eficiente ( en términos de complejidad algoritmica) y
rápido (en términos de ejecución) por ejemplo a través de uso de los
algoritmos divide-and-conquer.

%description -l fr
Bit::Vector est une bibliothèque C efficace qui vous permet de gérer
des vecteurs bit, des ensembles (d'entiers), "arithmétique de grand
entier" et des matrices booléennes, toutes de taille arbitraire.

La bibliothèque est efficace (en termes de complexité d'algoritme) et
donc rapide (en termes de vitesse d'exécution), par exemple pour
l'usage large desalgorithmes par division et conquête.

%description -l it
Bit::Vector è una libreria C altamente efficiente che permette di
gestire vettori bit, set (di interi), matrici "aritmetiche di interi"
e booleane di dimensioni arbitrarie.

La libreria è efficiente (in termini di complessità algoritmica) e
rapida (in termini di velocità di esecuzione), per esempio con l'uso
degli algoritmi divide-and-conquer.

%description -l pl
Bit::Vector jest wydajn± bibliotek± w C, implementuj±c± wektory
bitowe, zbiory (liczb ca³kowitych), "arytmetykê wielkich liczb" oraz
tablice bitowe, wszystko o dowolnych rozmiarach.

Biblioteka ta jest wydajna (w terminach z³o¿ono¶ci algorytmu) i, w
zwi±zku z tym, szybka (w terminach szybko¶ci wykonywania) m.in. dziêki
szerokiemu wykorzystaniu algorytmów "dziel i rz±d¼".

%description -l pt
O Bit::Vector é uma biblioteca eficiente em C que lhe permite lidar
com os vectores e conjuntos de "bits", a "aritmética com inteiros
grandes" e matrizes booleanas, tudo isto com tamanhos arbitrários.

A biblioteca é eficiente (em termos de complexidade algorítmica) e,
como tal, é rápida (em termos de tempos de execução), por exemplo,
através da utilização vasta de algoritmos de divisão-e-conquista.

%description -l pt_BR
O Bit::Vector é uma biblioteca eficiente em C que lhe permite lidar
com os vectores e conjuntos de "bits", a "aritmética com inteiros
grandes" e matrizes booleanas, tudo isto com tamanhos arbitrários.

A biblioteca é eficiente (em termos de complexidade algorítmica) e,
como tal, é rápida (em termos de tempos de execução), por exemplo,
através da utilização vasta de algoritmos de divisão-e-conquista.

%description -l sv
Bit::Vector är ett effekivt C-bibliotek som låter dig hantera
bitvektorer, mängder (av heltal), aritmetik för stora heltal och
booleska matriser, allt med godtyckliga storlekar.

Biblioteket är effektivt (i termer av algoritmkomplexitet) och därför
snabbt (i termer av exekveringshastighet) bland annat genom det
omfattande användandet av söndra-och-härska-algoritmer.

%description -l zh_CN
Bit::Vector ÊÇÒ»¸ö¸ßĞ§µÄ C ¿â¡£ËüÔÊĞíÄú´¦Àí
Î»ÏòÁ¿¡¢(ÕûÊı)¼¯ºÏ¡¢¡°´óÕûÊıËãÊõ¡±ÒÔ¼° boolean
·½Õó¡£ËüÃÇ¿ÉÒÔÊÇÈÎÒâ´óĞ¡¡£

¸Ã¿âÊÇ¸ßĞ§ÂÊµÄ(Õë¶ÔËãÊ½¸´ÔÓĞÔ¶øÑÔ)£¬Òò¶øÔËĞĞ
ËÙ¶ÈÒ²½Ï¿ì(Õë¶ÔÖ´ĞĞËÙ¶È¶øÑÔ)¡£ËüÍ¨¹ı¹ã·ºÀûÓÃ
¡°·Ö¶ø¿ËÖ®¡±µÄËãÊ½À´´ïµ½ÕâÒ»Ä¿µÄ¡£

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
rm -f GNU_{,L}GPL.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *txt
%{perl_vendorarch}/Bit/Vector.pm
%dir %{perl_vendorarch}/Bit/Vector
%{perl_vendorarch}/Bit/Vector/Overload.pm
%dir %{perl_vendorarch}/Carp
%{perl_vendorarch}/Carp/Clan.pm
%dir %{perl_vendorarch}/auto/Bit/Vector
%{perl_vendorarch}/auto/Bit/Vector/Vector.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Bit/Vector/Vector.so
%{_mandir}/man3/*

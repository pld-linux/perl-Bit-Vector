#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Bit
%define		pnam	Vector
Summary:	Bit::Vector - efficient base class implementing bit vectors
Summary(cs.UTF-8):	Bit::Vector - modul pro vysoce výkonné manipulace bitových vektorů v Perlu
Summary(da.UTF-8):	Bit::Vector - et modul for højydelsehåndtering af bitvektorer i Perl
Summary(de.UTF-8):	Bit::Vector - ein Modul für das leistungsstarke Bearbeiten von bit-Vektoren durch Perl
Summary(es.UTF-8):	Bit::Vector - módulo para la manipulación Perl de alta ejecución de muchos vectores
Summary(fr.UTF-8):	Bit::Vector - module de manipulation Perl à haute performance de vecteurs bits
Summary(it.UTF-8):	Bit::Vector - modulo per la gestione dei vettori bit ad alte prestazioni con Perl
Summary(ja.UTF-8):	Bit::Vector ビットベクトルのハイパフォーマンスPerl操作の為のモジュールです。
Summary(ko.UTF-8):	Bit::Vector bit 벡터를 고성능 Perl 조작하는데 사용되는 모듈
Summary(pl.UTF-8):	Bit::Vector - wydajna klasa bazowa implementująca wektory bitowe
Summary(pt.UTF-8):	Bit::Vector - um módulo para a manipulação rápida em Perl de vectores de "bits"
Summary(pt_BR.UTF-8):	Bit::Vector - um módulo para a manipulação rápida em Perl de vectores de "bits"
Summary(sv.UTF-8):	Bit::Vector - en modul för högprestandahantering av bitvektorer i Perl
Summary(tr.UTF-8):	Bit::Vector - bit matrislerinin yüksek başarımlı hesaplamaları için bir Perl modülü
Summary(zh_CN.UTF-8):	Bit::Vector - 对位向量进行高性能 Perl 操作的模块。
Name:		perl-Bit-Vector
Version:	7.4
Release:	2
# same as perl or (C library only) LGPL
License:	GPL v1+ or Artistic or (C library only) LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Bit/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bf67f144e5be5327ed79d4c69e6e0086
URL:		http://search.cpan.org/dist/Bit-Vector/
%if %{with tests}
BuildRequires:	perl-Carp-Clan >= 5.3
BuildRequires:	perl-Storable >= 2.21
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bit::Vector is an efficient C library which allows you to handle bit
vectors, sets (of integers), "big integer arithmetic" and boolean
matrices, all of arbitrary sizes.

The library is efficient (in terms of algorithmical complexity) and
therefore fast (in terms of execution speed) for instance through the
widespread use of divide-and-conquer algorithms.

%description -l cs.UTF-8
Bit::Vector je efektivní knihovna v C, která vám umožňuje zpracovávat
vektory bitů, množiny (celých čísel), "aritmetiku velkých čísel" a
matice booleovských hodnot, vše pro libovolné velikosti.

Knihovna je efektivní (myšlena složitost algoritmů) a proto rychlá
(myšlena rychlost provádění) například rozšířeným použitím algoritmů
rozděl a panuj.

%description -l da.UTF-8
Bit::Vector er et effekivt C-bibliotek som lader dig håndtere
bitvektorer, mængder (af heltal), aritmetik for store heltal og
booleske matricer, alt med vilkårlige størrelser.

Biblioteket er effektivt (forstået som algoritmkompleksitet) og derfor
hurtigt (forstået som eksekveringshastighed) blandt andet ved en
omfattende brug af del-og-hersk-algoritmer.

%description -l de.UTF-8
Bit::Vector ist eine leistungsfähige C-Bibliothek, mit der Sie bit-
Vektoren, Sätze (von ganzen Zahlen), "große, ganze arithmetische" und
boolesche Matrizen einer beliebigen Größe bearbeiten können.

Diese Bibliothek ist sehr leistungsstark (in Bezug auf ihre
algorithmische Komplexität) und daher auch sehr schnell (in Bezug auf
die Ausführungsgeschwindigkeit), beispielsweise im verbreiteten
Gebrauch von divide-and-conquer Algorithmen.

%description -l es.UTF-8
Bit::Vector es una librería C eficiente que le permiten gestionar
muchos vectores, grupos (de números enteros), "big integer arithmetic"
y matrices boolean, todos los tamaños arbitrarios.

La librería es eficiente ( en términos de complejidad algoritmica) y
rápido (en términos de ejecución) por ejemplo a través de uso de los
algoritmos divide-and-conquer.

%description -l fr.UTF-8
Bit::Vector est une bibliothèque C efficace qui vous permet de gérer
des vecteurs bit, des ensembles (d'entiers), "arithmétique de grand
entier" et des matrices booléennes, toutes de taille arbitraire.

La bibliothèque est efficace (en termes de complexité d'algoritme) et
donc rapide (en termes de vitesse d'exécution), par exemple pour
l'usage large desalgorithmes par division et conquête.

%description -l it.UTF-8
Bit::Vector è una libreria C altamente efficiente che permette di
gestire vettori bit, set (di interi), matrici "aritmetiche di interi"
e booleane di dimensioni arbitrarie.

La libreria è efficiente (in termini di complessità algoritmica) e
rapida (in termini di velocità di esecuzione), per esempio con l'uso
degli algoritmi divide-and-conquer.

%description -l pl.UTF-8
Bit::Vector jest wydajną biblioteką w C, implementującą wektory
bitowe, zbiory (liczb całkowitych), "arytmetykę wielkich liczb" oraz
tablice bitowe, wszystko o dowolnych rozmiarach.

Biblioteka ta jest wydajna (w terminach złożoności algorytmu) i, w
związku z tym, szybka (w terminach szybkości wykonywania) m.in. dzięki
szerokiemu wykorzystaniu algorytmów "dziel i rządź".

%description -l pt.UTF-8
O Bit::Vector é uma biblioteca eficiente em C que lhe permite lidar
com os vectores e conjuntos de "bits", a "aritmética com inteiros
grandes" e matrizes booleanas, tudo isto com tamanhos arbitrários.

A biblioteca é eficiente (em termos de complexidade algorítmica) e,
como tal, é rápida (em termos de tempos de execução), por exemplo,
através da utilização vasta de algoritmos de divisão-e-conquista.

%description -l pt_BR.UTF-8
O Bit::Vector é uma biblioteca eficiente em C que lhe permite lidar
com os vectores e conjuntos de "bits", a "aritmética com inteiros
grandes" e matrizes booleanas, tudo isto com tamanhos arbitrários.

A biblioteca é eficiente (em termos de complexidade algorítmica) e,
como tal, é rápida (em termos de tempos de execução), por exemplo,
através da utilização vasta de algoritmos de divisão-e-conquista.

%description -l sv.UTF-8
Bit::Vector är ett effekivt C-bibliotek som låter dig hantera
bitvektorer, mängder (av heltal), aritmetik för stora heltal och
booleska matriser, allt med godtyckliga storlekar.

Biblioteket är effektivt (i termer av algoritmkomplexitet) och därför
snabbt (i termer av exekveringshastighet) bland annat genom det
omfattande användandet av söndra-och-härska-algoritmer.

%description -l zh_CN.UTF-8
Bit::Vector 是一个高效的 C 库。它允许您处理
位向量、(整数)集合、“大整数算术”以及 boolean
方阵。它们可以是任意大小。

该库是高效率的(针对算式复杂性而言)，因而运行
速度也较快(针对执行速度而言)。它通过广泛利用
“分而克之”的算式来达到这一目的。

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/Bit/Vector{,/*}.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt CREDITS.txt README.txt
%{perl_vendorarch}/Bit/Vector.pm
%dir %{perl_vendorarch}/Bit/Vector
%{perl_vendorarch}/Bit/Vector/*.pm
%dir %{perl_vendorarch}/auto/Bit/Vector
%attr(755,root,root) %{perl_vendorarch}/auto/Bit/Vector/Vector.so
%{_mandir}/man3/Bit::Vector*.3pm*

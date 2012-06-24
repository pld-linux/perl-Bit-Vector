#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Bit
%define		pnam	Vector
Summary:	Bit::Vector - efficient base class implementing bit vectors
Summary(cs):	Bit::Vector - modul pro vysoce v�konn� manipulace bitov�ch vektor� v Perlu
Summary(da):	Bit::Vector - et modul for h�jydelseh�ndtering af bitvektorer i Perl
Summary(de):	Bit::Vector - ein Modul f�r das leistungsstarke Bearbeiten von bit-Vektoren durch Perl
Summary(es):	Bit::Vector - m�dulo para la manipulaci�n Perl de alta ejecuci�n de muchos vectores
Summary(fr):	Bit::Vector - module de manipulation Perl � haute performance de vecteurs bits
Summary(it):	Bit::Vector - modulo per la gestione dei vettori bit ad alte prestazioni con Perl
Summary(ja):	Bit::Vector �ӥåȥ٥��ȥ�Υϥ��ѥե����ޥ�Perl���ΰ٤Υ⥸�塼��Ǥ���
Summary(ko):	Bit::Vector bit ���͸� ���� Perl �����ϴµ� ���Ǵ� ���
Summary(pl):	Bit::Vector - wydajna klasa bazowa implementuj�ca wektory bitowe
Summary(pt):	Bit::Vector - um m�dulo para a manipula��o r�pida em Perl de vectores de "bits"
Summary(pt_BR):	Bit::Vector - um m�dulo para a manipula��o r�pida em Perl de vectores de "bits"
Summary(sv):	Bit::Vector - en modul f�r h�gprestandahantering av bitvektorer i Perl
Summary(tr):	Bit::Vector - bit matrislerinin y�ksek ba�ar�ml� hesaplamalar� i�in bir Perl mod�l�
Summary(zh_CN):	Bit::Vector - ��λ�������и����� Perl ������ģ�顣
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
Bit::Vector je efektivn� knihovna v C, kter� v�m umo��uje zpracov�vat
vektory bit�, mno�iny (cel�ch ��sel), "aritmetiku velk�ch ��sel" a
matice booleovsk�ch hodnot, v�e pro libovoln� velikosti.

Knihovna je efektivn� (my�lena slo�itost algoritm�) a proto rychl�
(my�lena rychlost prov�d�n�) nap��klad roz���en�m pou�it�m algoritm�
rozd�l a panuj.

%description -l da
Bit::Vector er et effekivt C-bibliotek som lader dig h�ndtere
bitvektorer, m�ngder (af heltal), aritmetik for store heltal og
booleske matricer, alt med vilk�rlige st�rrelser.

Biblioteket er effektivt (forst�et som algoritmkompleksitet) og derfor
hurtigt (forst�et som eksekveringshastighed) blandt andet ved en
omfattende brug af del-og-hersk-algoritmer.

%description -l de
Bit::Vector ist eine leistungsf�hige C-Bibliothek, mit der Sie bit-
Vektoren, S�tze (von ganzen Zahlen), "gro�e, ganze arithmetische" und
boolesche Matrizen einer beliebigen Gr��e bearbeiten k�nnen.

Diese Bibliothek ist sehr leistungsstark (in Bezug auf ihre
algorithmische Komplexit�t) und daher auch sehr schnell (in Bezug auf
die Ausf�hrungsgeschwindigkeit), beispielsweise im verbreiteten
Gebrauch von divide-and-conquer Algorithmen.

%description -l es
Bit::Vector es una librer�a C eficiente que le permiten gestionar
muchos vectores, grupos (de n�meros enteros), "big integer arithmetic"
y matrices boolean, todos los tama�os arbitrarios.

La librer�a es eficiente ( en t�rminos de complejidad algoritmica) y
r�pido (en t�rminos de ejecuci�n) por ejemplo a trav�s de uso de los
algoritmos divide-and-conquer.

%description -l fr
Bit::Vector est une biblioth�que C efficace qui vous permet de g�rer
des vecteurs bit, des ensembles (d'entiers), "arithm�tique de grand
entier" et des matrices bool�ennes, toutes de taille arbitraire.

La biblioth�que est efficace (en termes de complexit� d'algoritme) et
donc rapide (en termes de vitesse d'ex�cution), par exemple pour
l'usage large desalgorithmes par division et conqu�te.

%description -l it
Bit::Vector � una libreria C altamente efficiente che permette di
gestire vettori bit, set (di interi), matrici "aritmetiche di interi"
e booleane di dimensioni arbitrarie.

La libreria � efficiente (in termini di complessit� algoritmica) e
rapida (in termini di velocit� di esecuzione), per esempio con l'uso
degli algoritmi divide-and-conquer.

%description -l pl
Bit::Vector jest wydajn� bibliotek� w C, implementuj�c� wektory
bitowe, zbiory (liczb ca�kowitych), "arytmetyk� wielkich liczb" oraz
tablice bitowe, wszystko o dowolnych rozmiarach.

Biblioteka ta jest wydajna (w terminach z�o�ono�ci algorytmu) i, w
zwi�zku z tym, szybka (w terminach szybko�ci wykonywania) m.in. dzi�ki
szerokiemu wykorzystaniu algorytm�w "dziel i rz�d�".

%description -l pt
O Bit::Vector � uma biblioteca eficiente em C que lhe permite lidar
com os vectores e conjuntos de "bits", a "aritm�tica com inteiros
grandes" e matrizes booleanas, tudo isto com tamanhos arbitr�rios.

A biblioteca � eficiente (em termos de complexidade algor�tmica) e,
como tal, � r�pida (em termos de tempos de execu��o), por exemplo,
atrav�s da utiliza��o vasta de algoritmos de divis�o-e-conquista.

%description -l pt_BR
O Bit::Vector � uma biblioteca eficiente em C que lhe permite lidar
com os vectores e conjuntos de "bits", a "aritm�tica com inteiros
grandes" e matrizes booleanas, tudo isto com tamanhos arbitr�rios.

A biblioteca � eficiente (em termos de complexidade algor�tmica) e,
como tal, � r�pida (em termos de tempos de execu��o), por exemplo,
atrav�s da utiliza��o vasta de algoritmos de divis�o-e-conquista.

%description -l sv
Bit::Vector �r ett effekivt C-bibliotek som l�ter dig hantera
bitvektorer, m�ngder (av heltal), aritmetik f�r stora heltal och
booleska matriser, allt med godtyckliga storlekar.

Biblioteket �r effektivt (i termer av algoritmkomplexitet) och d�rf�r
snabbt (i termer av exekveringshastighet) bland annat genom det
omfattande anv�ndandet av s�ndra-och-h�rska-algoritmer.

%description -l zh_CN
Bit::Vector ��һ����Ч�� C �⡣������������
λ������(����)���ϡ����������������Լ� boolean
�������ǿ����������С��

�ÿ��Ǹ�Ч�ʵ�(�����ʽ�����Զ���)���������
�ٶ�Ҳ�Ͽ�(���ִ���ٶȶ���)����ͨ���㷺����
���ֶ���֮������ʽ���ﵽ��һĿ�ġ�

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

%define		_vendor_name	gregoriandate
Summary:	Gregoriandate for Ocaml
Summary(pl):	Data w kalendarzu gregoria�skim dla Ocamla
Name:		ocaml-%{_vendor_name}
Version:	1.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://merjis.com/_file/%{_vendor_name}-%{version}.tar.gz
# Source0-md5:	fab990962055f38720d4e626b796db8d
BuildRequires:	ocaml >= 3.04-7
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gregorian Date is a pure OCaml library for performing calculations
based on the Gregorian calendar.

This is a library of useful date calculations using the Gregorian
calendar, as used in most Western countries, and increasingly in the
East. Although the Gregorian calendar was adopted in 1582, this
library extends it back through to 1 AD.

It is inspired and derived from Perl's Date::Calc

%description -l pl
Gregorian Date jest napisan� w ocamlu bibliotek� dla ocamla wykonuj�c�
podstawowe obliczenia w kalendarzu gregoria�skim.

Jest to biblioteka cz�sto u�ywanych oblicze� przy u�yciu kalendarza
gregoria�skiego, u�ywanego na p�kuli zachodniej, a i coraz cz�ciej
na wschodniej. Mimo �e kalendarz gregoria�ski zosta� przyj�ty w 1582
roku, biblioteka ta potrafi wykonywa� obliczenia od 1 roku naszej ery.

Powsta�a ona w wyniku inspiracji modu�em Perla Date::Calc i na nim si�
opiera.

%package devel
Summary:	Gregoriandate for Ocaml - development part
Summary(pl):	Data w kalendarzu gregoria�skim dla Ocamla - cz�� programistyczna
Group:		Development/Libraries
%requires_eq	ocaml

%description devel
Gregorian Date is a pure OCaml library for performing calculations
based on the Gregorian calendar.

This is a library of useful date calculations using the Gregorian
calendar, as used in most Western countries, and increasingly in the
East. Although the Gregorian calendar was adopted in 1582, this
library extends it back through to 1 AD.

It is inspired and derived from Perl's Date::Calc This package
contains files needed to develop OCaml programs using this library.

%description devel -l pl
Gregorian Date jest napisan� w ocamlu bibliotek� dla ocamla wykonuj�c�
podstawowe obliczenia w kalendarzu gregoria�skim.

Jest to biblioteka cz�sto u�ywanych oblicze� przy u�yciu kalendarza
gregoria�skiego, u�ywanego na p�kuli zachodniej, a i coraz cz�ciej
na wschodniej. Mimo �e kalendarz gregoria�ski zosta� przyj�ty w 1582
roku, biblioteka ta potrafi wykonywa� obliczenia od 1 roku naszej ery.
Pakiet zawiera pliki niezb�dne do tworzenia program�w u�ywaj�cych tej
biblioteki.

%prep
%setup -q -n %{_vendor_name}-%{version}

%build
%{__make} all \
	CC="%{__cc} %{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/gregoriandate
install *.cm[ixa]* *.a $RPM_BUILD_ROOT%{_libdir}/ocaml/gregoriandate

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/gregoriandate
cat > $RPM_BUILD_ROOT%{_libdir}/ocaml/site-lib/gregoriandate/META <<EOF
requires = ""
version = "%{version}"
directory = "+gregoriandate"
archive(byte) = "gregoriandate.cma"
archive(native) = "gregoriandate.cmxa"
linkopts = ""
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING.LIB *.mli
%dir %{_libdir}/ocaml/gregoriandate
%{_libdir}/ocaml/gregoriandate/*.cm[ixa]*
%{_libdir}/ocaml/gregoriandate/*.a
%{_examplesdir}/%{name}-%{version}
%{_libdir}/ocaml/site-lib/gregoriandate

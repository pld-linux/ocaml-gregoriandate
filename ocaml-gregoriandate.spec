%define         _short_name gregoriandate
Summary:	Gregoriandate for Ocaml
Summary(pl):	Data w kalendazu gregorianskim dla Ocamla
Name:		ocaml-%{_short_name}
Version:	1.0.1
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://merjis.com/_file/%{_short_name}-%{version}.tar.gz
#Source0-md5:   fab990962055f38720d4e626b796db8d
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


%package devel
Summary:	Gregoriandate for Ocaml - development part
Summary(pl):	Data w kalendazu gregorianskim dla Ocamla - cze¶æ programistyczna
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
Gregorian Date jest napisana w ocamlu biblioteka dla ocamla wykonujaca
podstawowe obliczenia w kalendarzu Gregorianskim.

To biblioteka czesto uzywanych obliczen przy uzyciu kalendarza
Gregorianskiego, uzywanego na Zahodniej polkuli, a i coraz czesciej na
wschodniej. Mimo ze kaledaz Gregorianski zostal przyjety do uzycia w
1582 roku, ta biblioteka potrafi wykonywac obliczenia do 1 roku naszej
ery. Pakiet ten zawiera pliki niezbêdne do tworzenia programów
u¿ywaj±cych tej biblioteki.

%prep
%setup -q -n %{_short_name}-%{version}

%build
%{__make} CC="%{__cc} %{rpmcflags} -fPIC" all

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/gregoriandate
install *.cm[ixa]* *.a  $RPM_BUILD_ROOT%{_libdir}/ocaml/gregoriandate

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

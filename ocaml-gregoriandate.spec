%define		_vendor_name	gregoriandate
%define		ocaml_ver	1:3.09.2
Summary:	Gregoriandate for Ocaml
Summary(pl.UTF-8):	Data w kalendarzu gregoriańskim dla Ocamla
Name:		ocaml-%{_vendor_name}
Version:	1.0.1
Release:	5
License:	GPL
Group:		Libraries
Source0:	http://merjis.com/_file/%{_vendor_name}-%{version}.tar.gz
# Source0-md5:	fab990962055f38720d4e626b796db8d
BuildRequires:	ocaml >= %{ocaml_ver}
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

%description -l pl.UTF-8
Gregorian Date jest napisaną w ocamlu biblioteką dla ocamla wykonującą
podstawowe obliczenia w kalendarzu gregoriańskim.

Jest to biblioteka często używanych obliczeń przy użyciu kalendarza
gregoriańskiego, używanego na półkuli zachodniej, a i coraz częściej
na wschodniej. Mimo że kalendarz gregoriański został przyjęty w 1582
roku, biblioteka ta potrafi wykonywać obliczenia od 1 roku naszej ery.

Powstała ona w wyniku inspiracji modułem Perla Date::Calc i na nim się
opiera.

%package devel
Summary:	Gregoriandate for Ocaml - development part
Summary(pl.UTF-8):	Data w kalendarzu gregoriańskim dla Ocamla - część programistyczna
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

%description devel -l pl.UTF-8
Gregorian Date jest napisaną w ocamlu biblioteką dla ocamla wykonującą
podstawowe obliczenia w kalendarzu gregoriańskim.

Jest to biblioteka często używanych obliczeń przy użyciu kalendarza
gregoriańskiego, używanego na półkuli zachodniej, a i coraz częściej
na wschodniej. Mimo że kalendarz gregoriański został przyjęty w 1582
roku, biblioteka ta potrafi wykonywać obliczenia od 1 roku naszej ery.
Pakiet zawiera pliki niezbędne do tworzenia programów używających tej
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

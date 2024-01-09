Name:		texlive-srdp-mathematik
Version:	69288
Release:	1
Summary:	Typeset Austrian SRDP in mathematics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/srdp-mathematik
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srdp-mathematik.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/srdp-mathematik.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides basic commands for the defined formats of
the Austrian sRDP (Standardisierte Reife- und Diplomprufung) in
mathematics. Furthermore, it includes ways to implement answers
in the tex file which can optionally be displayed in the pdf
file, and it offers a way to vary the answers in order to
create different groups (e. g. for tests) easily.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/srdp-mathematik
%doc %{_texmfdistdir}/doc/latex/srdp-mathematik

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

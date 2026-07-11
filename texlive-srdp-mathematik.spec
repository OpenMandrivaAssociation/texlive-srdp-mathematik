%global tl_name srdp-mathematik
%global tl_revision 76697

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.14.0
Release:	%{tl_revision}.1
Summary:	Typeset Austrian SRDP in mathematics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/srdp-mathematik
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srdp-mathematik.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/srdp-mathematik.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides basic commands for the defined formats of the
Austrian sRDP (Standardisierte Reife- und Diplomprufung) in mathematics.
Furthermore, it includes ways to implement answers in the tex file which
can optionally be displayed in the pdf file, and it offers a way to vary
the answers in order to create different groups (e. g. for tests)
easily.


%global tl_name authoraftertitle
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Make author, etc., available after \maketitle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/authoraftertitle
License:	cc0
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This jiffy package makes the author, title and date of the package
available to the user (as \MyAuthor, etc) after the \maketitle command
has been executed.


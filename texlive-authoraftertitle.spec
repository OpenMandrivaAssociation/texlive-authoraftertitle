# revision 17063
# category Package
# catalog-ctan /macros/latex/contrib/authoraftertitle
# catalog-date 2010-02-23 16:03:07 +0100
# catalog-license other-free
# catalog-version 0.9
Name:		texlive-authoraftertitle
Version:	0.9
Release:	1
Summary:	Make author, etc., available after \maketitle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/authoraftertitle
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This jiffy package makes the author, title and date of the
package available to the user (as \MyAuthor, etc) after the
\maketitle command has been executed.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/authoraftertitle/authoraftertitle.sty
%doc %{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.pdf
%doc %{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}

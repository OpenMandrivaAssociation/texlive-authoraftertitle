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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/authoraftertitle/authoraftertitle.sty
%doc %{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.pdf
%doc %{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
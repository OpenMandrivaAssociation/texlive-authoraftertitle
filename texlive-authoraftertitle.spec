Name:		texlive-authoraftertitle
Version:	55889
Release:	1
Summary:	Make author, etc., available after \maketitle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/authoraftertitle
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.r55889.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.doc.r55889.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This jiffy package makes the author, title and date of the
package available to the user (as \MyAuthor, etc) after the
\maketitle command has been executed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/authoraftertitle
%doc %{_texmfdistdir}/doc/latex/authoraftertitle

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}

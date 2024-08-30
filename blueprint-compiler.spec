%define _empty_manifest_terminate_build 0

Summary:	A markup language for GTK user interface files
Name:		blueprint-compiler
Version:	0.14.0
Release:	1
License:	GPLv3+
Group:		Development/GNOME and GTK+
Url:		https://gitlab.gnome.org/jwestman/blueprint-compiler
Source0:	https://gitlab.gnome.org/jwestman/blueprint-compiler/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:	meson
BuildRequires:  pkgconfig(python)

%description
A markup language for GTK user interface files.

#----------------------------------------------------------------------------

%package -n python-%{name}
Summary:	A markup language for GTK user interface files
Group:		Development/Python

%description -n python-%{name}
A markup language for GTK user interface files.

%files -n python-%{name}
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{python_sitelib}/blueprintcompiler

#----------------------------------------------------------------------------

%package -n %{name}-devel
Summary:	Devel file for %{name}
Group:		Development/Python
Requires:	python-%{name} = %{EVRD}

%description -n %{name}-devel
Devel file for %{name}.

%files -n %{name}-devel
%{_datadir}/pkgconfig/%{name}.pc

#------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

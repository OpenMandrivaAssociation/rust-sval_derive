%bcond_without check
%global debug_package %{nil}

%global crate sval_derive

Name:           rust-%{crate}
Version:        1.0.0~alpha.5
Release:        1%{?dist}
Summary:        Custom derive for sval

# Upstream license specification: Apache-2.0 OR MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/sval_derive
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging
%if ! %{__cargo_skip_build}
BuildRequires:  (crate(proc-macro2/default) >= 1.0.0 with crate(proc-macro2/default) < 2.0.0)
BuildRequires:  (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0)
BuildRequires:  (crate(syn/default) >= 1.0.0 with crate(syn/default) < 2.0.0)
%endif

%global _description %{expand:
Custom derive for sval.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval_derive) = 1.0.0~alpha.5
Requires:       cargo
Requires:       (crate(proc-macro2/default) >= 1.0.0 with crate(proc-macro2/default) < 2.0.0)
Requires:       (crate(quote/default) >= 1.0.0 with crate(quote/default) < 2.0.0)
Requires:       (crate(syn/default) >= 1.0.0 with crate(syn/default) < 2.0.0)

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       crate(sval_derive/default) = 1.0.0~alpha.5
Requires:       cargo
Requires:       crate(sval_derive) = 1.0.0~alpha.5

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

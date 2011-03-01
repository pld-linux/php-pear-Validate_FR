%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Validate_FR
Summary:	%{_pearname} - Validation class for FR
Summary(pl.UTF-8):	%{_pearname} - Klasa walidacji dla FR
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	3
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9750f7b210b753f7ddacd9748da427c3
URL:		http://pear.php.net/package/Validate_FR/
BuildRequires:	php-pear-PEAR >= 1:1.7.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.6.2
Obsoletes:	php-pear-Validate_FR-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'pear(FR_insee_country_codes.php)'

%description
Package containes locale validation for FR such as:
 - SSN
 - Postal Code
 - RIB
 - SIREN
 - SIRET
 - Region (Departements)

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet dostarcza metody do sprawdzania poprawności dla Francji danych
takich jak:
 - SSN
 - Kod pocztowy
 - RIB
 - SIREN
 - SIRET
 - region (departement)

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/LICENSE
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/FR.php

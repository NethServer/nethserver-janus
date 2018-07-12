Name:    nethserver-janus
Version: 1.0.2
Release: 1%{?dist}
Summary: Janus WebRTC Gateway NethServer configuration
Group: Network
License: GPLv3
BuildArch: noarch
Packager: Nethesis <info@nethesis.it>
Source0: %{name}-%{version}.tar.gz
Requires: janus-gateway >= 0.4.1
BuildRequires: nethserver-devtools

%description
Janus is an open source, general purpose, WebRTC gateway designed and developed by Meetecho.
nethserver-janus configure Janus for NethServer

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%clean
rm -rf %{buildroot}

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root,-)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jun 28 2018 Stefano Fancello <stefano.fancello@nethesis.it> - 1.0.2-1
- Don't start Janus Gateway by default nethesis/dev#5420

* Mon Nov 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- nethserver-janus: allow to change NAT behaviour - NethServer/dev#5373

* Thu Aug 31 2017 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0.0-1
Release 1.0.0


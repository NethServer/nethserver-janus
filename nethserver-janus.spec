Name:    nethserver-janus
Version: 1.0.1
Release: 1%{?dist}
Summary: Janus WebRTC Gateway NethServer configuration
Group: Network
License: GPLv3
BuildArch: noarch
Packager: Nethesis <info@nethesis.it>
Source0: %{name}-%{version}.tar.gz
Requires: janus-gateway
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
* Mon Nov 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- nethserver-janus: allow to change NAT behaviour - NethServer/dev#5373

* Thu Aug 31 2017 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0.0-1
Release 1.0.0


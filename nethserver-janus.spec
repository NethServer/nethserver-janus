Name:    nethserver-janus
Version: 1.2.4
Release: 1%{?dist}
Summary: Janus WebRTC Gateway NethServer configuration
License: GPLv3
BuildArch: noarch
Source0: %{name}-%{version}.tar.gz
Requires: janus-gateway >= 0.12.3
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
%license LICENSE
%defattr(-,root,root,-)
%dir %{_nseventsdir}/%{name}-update

%changelog
* Tue Oct 24 2023 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.4-1
- Bump version to restart janus after upstream nss update - NethServer/dev#6766

* Thu Oct 24 2023 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.3-2
- Bump version to force restart - NethServer/dev#6766

* Fri Sep 30 2022 Stefano Fancello <stefano.fancello@nethesis.it> - 1.2.3-1
- Update Janus Gateway to 0.12.3 - nethesis/dev#6178

* Mon Mar 01 2021 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.2.2-1
- Janus-Gateway: upgrade to 0.10.10 (7732127) - NethServer/dev#6416

* Fri Nov 06 2020 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.2.1-1
- Janus-Gateway: upgrade to 0.10.6 (cc204a5) - NethServer/dev#6313

* Mon Jul 06 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.2.0-1
- Enable Janus Admin Api as default on localhost - NethServer/dev#6217
- Development builds for Janus and sofia-sip - nethesis/dev#5836
- Janus-Gateway: upgrade to 922b392 - NethServer/dev#6195

* Thu May 28 2020 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.1.1-1
- Janus-Gateway: upgrade to v0.9.4 - NethServer/dev#6135

* Mon Dec 02 2019 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.1.0-1
- Nethserver-janus: allow to configure ICE gathering candidate interfaces - NethServer/dev#5960

* Thu Nov 21 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.0.18-1
- spec: inc version only to restart new janus v 0.7.6.1 (#19)

* Mon Nov 18 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.0.16-1
- Janus-Gateway: update to the latest commit on master a71354b (> 0.7.6) - nethserver/dev#5914

* Wed Oct 30 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.0.15-1
- Require janus 0.7.4.0: aligned with upstream 262e997 (> 0.7.4) (#17)

* Wed Sep 04 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.0.14-1
- Janus-Gateway: update to the latest commit on master (dca6fec) - NethServer/dev#5786

* Tue Jul 02 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.0.13-1
- Janus-Gateway: update to the latest commit on master (f86597c) - NethServer/dev#5774

* Tue May 28 2019 Alessandro Polidori <alessandro.polidori@nethesis.it> - 1.0.12-1
- Janus-Gateway: update to the latest commit on master (a16862) - NethServer/dev#5757
- Janus: enable all plugins - nethserver/dev#5749
- Janus-Gateway: update to the latest commit on master (0b80a02) - nethserver/dev#5757

* Fri Apr 19 2019 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.11-1
- Fix Janus to support DTLS 1.2 needed by new Chrome M74 release - Bug NethServer/dev#5740

* Tue Mar 26 2019 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.10-1
- Upgrade janus-gateway to v0.6.3 - nethserver/dev#5735

* Fri Mar 15 2019 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.9-1
- Upgrade janus-gateway to v0.6.2 - nethserver/dev#5728

* Thu Mar 07 2019 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.8-1
- Upgrade janus-gateway to v0.6.1 - nethserver/dev#5723

* Thu Feb 28 2019 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.7-1
- Upgrade janus-gateway to v0.6.0 - nethserver/dev#5694

* Fri Dec 07 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.6-1
- Update janus-gateway to 0.5.0 - Bug nethserver/dev#5648

* Mon Nov 05 2018 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.5-1
- Update janus-gateway to 0.4.5 - nethserver/dev#5609

* Thu Sep 06 2018 Stefano Fancello <stefano.fancello@nethesis.it> - 1.0.4-1
- Janus gateway: logfile no more written after logrotate - Bug NethServer/dev#5576

* Tue Jul 24 2018 Alessandro Polidori <alessandro.polidori@gmail.com> - 1.0.3-1
- Update janus-gateway to 0.4.3 - NethServer/dev#5511

* Thu Jun 28 2018 Stefano Fancello <stefano.fancello@nethesis.it> - 1.0.2-1
- Don't start Janus Gateway by default nethesis/dev#5420

* Mon Nov 20 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- nethserver-janus: allow to change NAT behaviour - NethServer/dev#5373

* Thu Aug 31 2017 Edoardo Spadoni <edoardo.spadoni@nethesis.it> - 1.0.0-1
Release 1.0.0


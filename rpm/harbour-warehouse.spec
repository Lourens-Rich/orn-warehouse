# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       harbour-warehouse

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    Warehouse application
Version:    0.3
Release:    26
Group:      Qt/Qt
License:    GPLv3
URL:        https://openrepos.net/
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-warehouse.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
Requires:   PackageKit >= 0.8.9
Requires:   PackageKit-Qt5 >= 0.8.8
BuildRequires:  pkgconfig(packagekit-qt5)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(sailfishapp) >= 0.0.10
BuildRequires:  ssu-devel
BuildRequires:  desktop-file-utils
Obsoletes:   harbour-warehouse-installer

%description
Warehouse is a native client for OpenRepos.net


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}/qml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{_datadir}/%{name}
%{_sysconfdir}/zypp/repos.d
%{_sharedstatedir}/polkit-1/localauthority/50-local.d/50-net.openrepos.warehouse-packagekit.pkla
# >> files
#%defattr(-,nemo,privileged,-)
%dir %{_sysconfdir}/zypp/repos.d
%{_sysconfdir}/zypp/repos.d/openrepos.enabled
# << files

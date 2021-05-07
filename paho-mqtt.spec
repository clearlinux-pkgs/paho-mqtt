#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paho-mqtt
Version  : 1.5.1
Release  : 21
URL      : https://files.pythonhosted.org/packages/32/d3/6dcb8fd14746fcde6a556f932b5de8bea8fedcb85b3a092e0e986372c0e7/paho-mqtt-1.5.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/32/d3/6dcb8fd14746fcde6a556f932b5de8bea8fedcb85b3a092e0e986372c0e7/paho-mqtt-1.5.1.tar.gz
Summary  : MQTT version 5.0/3.1.1 client class
Group    : Development/Tools
License  : BSD-3-Clause EPL-1.0
Requires: paho-mqtt-license = %{version}-%{release}
Requires: paho-mqtt-python = %{version}-%{release}
Requires: paho-mqtt-python3 = %{version}-%{release}
Requires: PySocks
BuildRequires : PySocks
BuildRequires : buildreq-distutils3

%description
================================

%package license
Summary: license components for the paho-mqtt package.
Group: Default

%description license
license components for the paho-mqtt package.


%package python
Summary: python components for the paho-mqtt package.
Group: Default
Requires: paho-mqtt-python3 = %{version}-%{release}

%description python
python components for the paho-mqtt package.


%package python3
Summary: python3 components for the paho-mqtt package.
Group: Default
Requires: python3-core
Provides: pypi(paho_mqtt)

%description python3
python3 components for the paho-mqtt package.


%prep
%setup -q -n paho-mqtt-1.5.1
cd %{_builddir}/paho-mqtt-1.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609886087
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/paho-mqtt
cp %{_builddir}/paho-mqtt-1.5.1/LICENSE.txt %{buildroot}/usr/share/package-licenses/paho-mqtt/ce0053083d3761c5b4d0e15b8ae3182034fe3138
cp %{_builddir}/paho-mqtt-1.5.1/edl-v10 %{buildroot}/usr/share/package-licenses/paho-mqtt/a8709c8c7e056d82845a30d21f075912aa8a0129
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/paho-mqtt/a8709c8c7e056d82845a30d21f075912aa8a0129
/usr/share/package-licenses/paho-mqtt/ce0053083d3761c5b4d0e15b8ae3182034fe3138

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

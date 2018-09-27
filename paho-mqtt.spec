#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : paho-mqtt
Version  : 1.4.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/25/63/db25e62979c2a716a74950c9ed658dce431b5cb01fde29eb6cba9489a904/paho-mqtt-1.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/25/63/db25e62979c2a716a74950c9ed658dce431b5cb01fde29eb6cba9489a904/paho-mqtt-1.4.0.tar.gz
Summary  : MQTT version 3.1.1 client class
Group    : Development/Tools
License  : BSD-3-Clause EPL-1.0
Requires: paho-mqtt-python = %{version}-%{release}
Requires: paho-mqtt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pylama
BuildRequires : pytest-runner

%description
================================

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

%description python3
python3 components for the paho-mqtt package.


%prep
%setup -q -n paho-mqtt-1.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538089896
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

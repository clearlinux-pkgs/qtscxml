#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtscxml
Version  : 5.15.2
Release  : 29
URL      : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtscxml-everywhere-src-5.15.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.15/5.15.2/submodules/qtscxml-everywhere-src-5.15.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GFDL-1.3 GPL-3.0 LGPL-3.0
Requires: qtscxml-lib = %{version}-%{release}
Requires: qtscxml-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
Patch1: qtscxml-stable-branch.patch

%description
No detailed description available

%package dev
Summary: dev components for the qtscxml package.
Group: Development
Requires: qtscxml-lib = %{version}-%{release}
Provides: qtscxml-devel = %{version}-%{release}
Requires: qtscxml = %{version}-%{release}

%description dev
dev components for the qtscxml package.


%package examples
Summary: examples components for the qtscxml package.
Group: Default
Requires: qtscxml-dev = %{version}-%{release}

%description examples
examples components for the qtscxml package.


%package lib
Summary: lib components for the qtscxml package.
Group: Libraries
Requires: qtscxml-license = %{version}-%{release}

%description lib
lib components for the qtscxml package.


%package license
Summary: license components for the qtscxml package.
Group: Default

%description license
license components for the qtscxml package.


%prep
%setup -q -n qtscxml-everywhere-src-5.15.2
cd %{_builddir}/qtscxml-everywhere-src-5.15.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export GCC_IGNORE_WERROR=1
%qmake QMAKE_CFLAGS+=-fno-lto QMAKE_CXXFLAGS+=-fno-lto
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1646410710
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtscxml
cp %{_builddir}/qtscxml-everywhere-src-5.15.2/LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtscxml/61907422fefcd2313a9b570c31d203a6dbebd333
cp %{_builddir}/qtscxml-everywhere-src-5.15.2/LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtscxml/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
cp %{_builddir}/qtscxml-everywhere-src-5.15.2/LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtscxml/f45ee1c765646813b442ca58de72e20a64a7ddba
cp %{_builddir}/qtscxml-everywhere-src-5.15.2/tests/3rdparty/scion-tests/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtscxml/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/qtscxml-everywhere-src-5.15.2/tests/3rdparty/scion-tests/scxml-test-framework/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtscxml/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/bin/qscxmlc
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlcompiler_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlcppdatamodel_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmldatamodel_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlecmascriptplatformproperties_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlevent_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlexecutablecontent_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlglobals_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlinvokableservice_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlstatemachine_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmlstatemachineinfo_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qscxmltabledata_p.h
/usr/include/qt5/QtScxml/5.15.2/QtScxml/private/qtscxml-config_p.h
/usr/include/qt5/QtScxml/QScxmlCompiler
/usr/include/qt5/QtScxml/QScxmlCppDataModel
/usr/include/qt5/QtScxml/QScxmlDataModel
/usr/include/qt5/QtScxml/QScxmlDynamicScxmlServiceFactory
/usr/include/qt5/QtScxml/QScxmlEcmaScriptDataModel
/usr/include/qt5/QtScxml/QScxmlError
/usr/include/qt5/QtScxml/QScxmlEvent
/usr/include/qt5/QtScxml/QScxmlInvokableService
/usr/include/qt5/QtScxml/QScxmlInvokableServiceFactory
/usr/include/qt5/QtScxml/QScxmlNullDataModel
/usr/include/qt5/QtScxml/QScxmlStateMachine
/usr/include/qt5/QtScxml/QScxmlStaticScxmlServiceFactory
/usr/include/qt5/QtScxml/QScxmlTableData
/usr/include/qt5/QtScxml/QtScxml
/usr/include/qt5/QtScxml/QtScxmlDepends
/usr/include/qt5/QtScxml/QtScxmlVersion
/usr/include/qt5/QtScxml/qscxmlcompiler.h
/usr/include/qt5/QtScxml/qscxmlcppdatamodel.h
/usr/include/qt5/QtScxml/qscxmldatamodel.h
/usr/include/qt5/QtScxml/qscxmlecmascriptdatamodel.h
/usr/include/qt5/QtScxml/qscxmlerror.h
/usr/include/qt5/QtScxml/qscxmlevent.h
/usr/include/qt5/QtScxml/qscxmlexecutablecontent.h
/usr/include/qt5/QtScxml/qscxmlglobals.h
/usr/include/qt5/QtScxml/qscxmlinvokableservice.h
/usr/include/qt5/QtScxml/qscxmlnulldatamodel.h
/usr/include/qt5/QtScxml/qscxmlstatemachine.h
/usr/include/qt5/QtScxml/qscxmltabledata.h
/usr/include/qt5/QtScxml/qtscxml-config.h
/usr/include/qt5/QtScxml/qtscxmlversion.h
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfig.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfigExtras.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfigVersion.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlMacros.cmake
/usr/lib64/libQt5Scxml.prl
/usr/lib64/libQt5Scxml.so
/usr/lib64/pkgconfig/Qt5Scxml.pc
/usr/lib64/qt5/mkspecs/features/qscxmlc.prf
/usr/lib64/qt5/mkspecs/modules/qt_lib_scxml.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_scxml_private.pri

%files examples
%defattr(-,root,root,-)
/usr/share/qt5/examples/scxml/calculator-qml/Button.qml
/usr/share/qt5/examples/scxml/calculator-qml/calculator-qml.cpp
/usr/share/qt5/examples/scxml/calculator-qml/calculator-qml.pro
/usr/share/qt5/examples/scxml/calculator-qml/calculator-qml.qml
/usr/share/qt5/examples/scxml/calculator-qml/calculator-qml.qrc
/usr/share/qt5/examples/scxml/calculator-widgets/calculator-widgets.cpp
/usr/share/qt5/examples/scxml/calculator-widgets/calculator-widgets.pro
/usr/share/qt5/examples/scxml/calculator-widgets/mainwindow.cpp
/usr/share/qt5/examples/scxml/calculator-widgets/mainwindow.h
/usr/share/qt5/examples/scxml/calculator-widgets/mainwindow.ui
/usr/share/qt5/examples/scxml/ftpclient/ftpclient.pro
/usr/share/qt5/examples/scxml/ftpclient/ftpcontrolchannel.cpp
/usr/share/qt5/examples/scxml/ftpclient/ftpcontrolchannel.h
/usr/share/qt5/examples/scxml/ftpclient/ftpdatachannel.cpp
/usr/share/qt5/examples/scxml/ftpclient/ftpdatachannel.h
/usr/share/qt5/examples/scxml/ftpclient/main.cpp
/usr/share/qt5/examples/scxml/invoke-dynamic/invoke-dynamic.cpp
/usr/share/qt5/examples/scxml/invoke-dynamic/invoke-dynamic.pro
/usr/share/qt5/examples/scxml/invoke-dynamic/invoke-dynamic.qml
/usr/share/qt5/examples/scxml/invoke-dynamic/invoke-dynamic.qrc
/usr/share/qt5/examples/scxml/invoke-static/invoke-static.cpp
/usr/share/qt5/examples/scxml/invoke-static/invoke-static.pro
/usr/share/qt5/examples/scxml/invoke-static/invoke-static.qml
/usr/share/qt5/examples/scxml/invoke-static/invoke-static.qrc
/usr/share/qt5/examples/scxml/mediaplayer-qml-cppdatamodel/mediaplayer-qml-cppdatamodel.cpp
/usr/share/qt5/examples/scxml/mediaplayer-qml-cppdatamodel/mediaplayer-qml-cppdatamodel.pro
/usr/share/qt5/examples/scxml/mediaplayer-qml-cppdatamodel/mediaplayer-qml-cppdatamodel.qml
/usr/share/qt5/examples/scxml/mediaplayer-qml-cppdatamodel/mediaplayer-qml-cppdatamodel.qrc
/usr/share/qt5/examples/scxml/mediaplayer-qml-cppdatamodel/thedatamodel.cpp
/usr/share/qt5/examples/scxml/mediaplayer-qml-cppdatamodel/thedatamodel.h
/usr/share/qt5/examples/scxml/mediaplayer-qml-dynamic/mediaplayer-qml-dynamic.cpp
/usr/share/qt5/examples/scxml/mediaplayer-qml-dynamic/mediaplayer-qml-dynamic.pro
/usr/share/qt5/examples/scxml/mediaplayer-qml-dynamic/mediaplayer-qml-dynamic.qml
/usr/share/qt5/examples/scxml/mediaplayer-qml-dynamic/mediaplayer-qml-dynamic.qrc
/usr/share/qt5/examples/scxml/mediaplayer-qml-static/mediaplayer-qml-static.cpp
/usr/share/qt5/examples/scxml/mediaplayer-qml-static/mediaplayer-qml-static.pro
/usr/share/qt5/examples/scxml/mediaplayer-qml-static/mediaplayer-qml-static.qml
/usr/share/qt5/examples/scxml/mediaplayer-qml-static/mediaplayer-qml-static.qrc
/usr/share/qt5/examples/scxml/mediaplayer-widgets-dynamic/mediaplayer-widgets-dynamic.cpp
/usr/share/qt5/examples/scxml/mediaplayer-widgets-dynamic/mediaplayer-widgets-dynamic.pro
/usr/share/qt5/examples/scxml/mediaplayer-widgets-dynamic/mediaplayer.qrc
/usr/share/qt5/examples/scxml/mediaplayer-widgets-static/mediaplayer-widgets-static.cpp
/usr/share/qt5/examples/scxml/mediaplayer-widgets-static/mediaplayer-widgets-static.pro
/usr/share/qt5/examples/scxml/pinball/main.cpp
/usr/share/qt5/examples/scxml/pinball/mainwindow.cpp
/usr/share/qt5/examples/scxml/pinball/mainwindow.h
/usr/share/qt5/examples/scxml/pinball/mainwindow.ui
/usr/share/qt5/examples/scxml/pinball/pinball.pro
/usr/share/qt5/examples/scxml/scxml.pro
/usr/share/qt5/examples/scxml/sudoku/data/nearly-solved-sudoku.data
/usr/share/qt5/examples/scxml/sudoku/data/sudoku.data
/usr/share/qt5/examples/scxml/sudoku/main.cpp
/usr/share/qt5/examples/scxml/sudoku/mainwindow.cpp
/usr/share/qt5/examples/scxml/sudoku/mainwindow.h
/usr/share/qt5/examples/scxml/sudoku/sudoku.js
/usr/share/qt5/examples/scxml/sudoku/sudoku.pro
/usr/share/qt5/examples/scxml/sudoku/sudoku.qrc
/usr/share/qt5/examples/scxml/trafficlight-qml-dynamic/trafficlight-qml-dynamic.cpp
/usr/share/qt5/examples/scxml/trafficlight-qml-dynamic/trafficlight-qml-dynamic.pro
/usr/share/qt5/examples/scxml/trafficlight-qml-dynamic/trafficlight-qml-dynamic.qml
/usr/share/qt5/examples/scxml/trafficlight-qml-dynamic/trafficlight-qml-dynamic.qrc
/usr/share/qt5/examples/scxml/trafficlight-qml-simple/Light.qml
/usr/share/qt5/examples/scxml/trafficlight-qml-simple/TrafficLight.qml
/usr/share/qt5/examples/scxml/trafficlight-qml-simple/trafficlight-qml-simple.cpp
/usr/share/qt5/examples/scxml/trafficlight-qml-simple/trafficlight-qml-simple.pro
/usr/share/qt5/examples/scxml/trafficlight-qml-simple/trafficlight-qml-simple.qrc
/usr/share/qt5/examples/scxml/trafficlight-qml-static/trafficlight-qml-static.cpp
/usr/share/qt5/examples/scxml/trafficlight-qml-static/trafficlight-qml-static.pro
/usr/share/qt5/examples/scxml/trafficlight-qml-static/trafficlight-qml-static.qml
/usr/share/qt5/examples/scxml/trafficlight-qml-static/trafficlight-qml-static.qrc
/usr/share/qt5/examples/scxml/trafficlight-widgets-dynamic/trafficlight-widgets-dynamic.cpp
/usr/share/qt5/examples/scxml/trafficlight-widgets-dynamic/trafficlight-widgets-dynamic.pro
/usr/share/qt5/examples/scxml/trafficlight-widgets-dynamic/trafficlight-widgets-dynamic.qrc
/usr/share/qt5/examples/scxml/trafficlight-widgets-static/trafficlight-widgets-static.cpp
/usr/share/qt5/examples/scxml/trafficlight-widgets-static/trafficlight-widgets-static.pro
/usr/share/qt5/examples/scxml/trafficlight-widgets-static/trafficlight-widgets-static.qrc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Scxml.so.5
/usr/lib64/libQt5Scxml.so.5.15
/usr/lib64/libQt5Scxml.so.5.15.2
/usr/lib64/qt5/qml/QtScxml/libdeclarative_scxml.so
/usr/lib64/qt5/qml/QtScxml/plugins.qmltypes
/usr/lib64/qt5/qml/QtScxml/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtscxml/61907422fefcd2313a9b570c31d203a6dbebd333
/usr/share/package-licenses/qtscxml/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/qtscxml/e93757aefa405f2c9a8a55e780ae9c39542dfc3a
/usr/share/package-licenses/qtscxml/f45ee1c765646813b442ca58de72e20a64a7ddba

Name:           kibana
Version:        4.1.6
Release:        1.vortex%{?dist}
Summary:        open source data visualization platform

Group:          System Environment/Daemons
License:        Apache
URL:            https://www.elastic.co/downloads/kibana
Vendor:		Vortex RPM
Source0:        %{name}-%{version}-linux-x64.tar.gz
Source3:	%{name}.init
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires(post):	    chkconfig
Requires(preun):    chkconfig, initscripts


%description
Kibana is an open source data visualization platform that allows you to
interact with your data through stunning, powerful graphics that can be
combined into custom dashboards that help you share insights from your
data far and wide.


%prep
%setup -q -n %{name}-%{version}-linux-x64


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt
install -d -D -m 0755 bin $RPM_BUILD_ROOT/opt/%{name}/bin
cp -R bin/* $RPM_BUILD_ROOT/opt/%{name}/bin/
install -d -D -m 0755 config $RPM_BUILD_ROOT/opt/%{name}/config
cp -R config/* $RPM_BUILD_ROOT/opt/%{name}/config/
install -d -D -m 0755 node $RPM_BUILD_ROOT/opt/%{name}/node
cp -R node/* $RPM_BUILD_ROOT/opt/%{name}/node/
install -d -D -m 0755 plugins $RPM_BUILD_ROOT/opt/%{name}/plugins
cp -R plugins/* $RPM_BUILD_ROOT/opt/%{name}/plugins/
install -d -D -m 0755 src $RPM_BUILD_ROOT/opt/%{name}/src
cp -R src/* $RPM_BUILD_ROOT/opt/%{name}/src/
install -D -m 0755 %{SOURCE3} $RPM_BUILD_ROOT/%{_initddir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/opt/%{name}
%{_initddir}/%{name}


%post
/sbin/chkconfig --add %{name}


%preun
if [ $1 -eq 0 ] ; then
	/sbin/service %{name} stop >/dev/null 2>&1
	/sbin/chkconfig --del %{name}
fi


%postun
if [ "$1" -ge "1" ] ; then
	/sbin/service %{name} restart >/dev/null 2>&1
fi


%changelog
* Tue May 17 2016 Ilya Otyutskiy <ilya.otyutskiy@icloud.com> - 4.1.6-1.vortex
- Initial packaging.

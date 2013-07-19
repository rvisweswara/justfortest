Name: das-xml2sql-sink
Version: 956
Release: 1%{?dist}
Summary: Expedia flume extensions
#Group: Applications/Internet
Group: Applications/Internet
License: EPLv1
URL: http://project.net
Source: das-xml2sql-sink-956.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
#Requires:      
%description
flume extensions developed at expedia

%prep
%setup -q

# This SPEC build is Only Packaging.
%build

%install
# Clean out any previous builds not on slash (lol)
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

# Copy the flume-extension jars to the right places
%{__mkdir_p} %{buildroot}/tmp/usr/lib/flume-ng/plugins.d/lib
%{__mkdir_p} %{buildroot}/tmp/usr/lib/flume-ng/plugins.d/libext
%{__cp} expedia/lib/*.jar %{buildroot}/tmp/usr/lib/flume-ng/plugins.d/lib
%{__cp} expedia/libext/*.jar %{buildroot}/tmp/usr/lib/flume-ng/plugins.d/libext

# Form a list of files for the files directive
echo $(cd %{buildroot} && find . -type f | cut -c 2-) | tr ' ' '\n' > files.txt
# Grab the symlinks too
echo $(cd %{buildroot} && find . -type l | cut -c 2-) | tr ' ' '\n' >> files.txt

%clean
[ "%{buildroot}" != "/" ] && %{__rm} -rf %{buildroot}

%files -f files.txt
%defattr(-,root,root,-)

%changelog
* Tue Jul 18 2013 expedia
- flume-0.1.1 Packaging

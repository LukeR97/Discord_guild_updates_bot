Name:           Discord_guild_updates_bot
Version:        1.0.0
Release:        1%{?dist}
Summary:        Discord bot for showing member join/leave updates

License:        MIT
URL:            https://github.com/LukeR97/%{name}
Source0:        https://github.com/LukeR97/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
      

%description
RPM package to build bot on cloud instance

%prep
%setup -q 

%build
make %{?_smp_mflags}


%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Sat Sep 30 2023 LukeR97
- first rpm package
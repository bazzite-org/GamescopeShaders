Name:           gamescope-shaders
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Reshade shaders packaged with Gamescope

License:        GPLv3
URL:            https://github.com/KyleGospo/GamescopeShaders

VCS:            {{{ git_dir_vcs }}}
Source:        	{{{ git_dir_pack }}}
BuildArch:      noarch

Requires:       gamescope

BuildRequires:  systemd-rpm-macros

%description
Reshade shaders packaged with Gamescope

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build

%install
mkdir -p %{buildroot}%{_datadir}/gamescope/reshade/Shaders
cp -rv Shaders/* %{buildroot}%{_datadir}/gamescope/reshade/Shaders
mkdir -p %{buildroot}%{_datadir}/gamescope/reshade/Textures
cp -rv Textures/* %{buildroot}%{_datadir}/gamescope/reshade/Textures

# Do post-installation
%post

# Do before uninstallation
%preun

# Do after uninstallation
%postun

# This lists all the files that are included in the rpm package and that
# are going to be installed into target system where the rpm is installed.
%files
%license LICENSE_Lilium
%{_datadir}/gamescope/reshade/Shaders/*
%{_datadir}/gamescope/reshade/Textures/*

# Finally, changes from the latest release of your application are generated from
# your project's Git history. It will be empty until you make first annotated Git tag.
%changelog
{{{ git_dir_changelog }}}

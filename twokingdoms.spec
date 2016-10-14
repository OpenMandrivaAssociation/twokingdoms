Summary:	A Tale of Two Kingdoms - an adventure game
Name:		twokingdoms
Version:	1.0.0
Release:	1
Source0:	http://download1948.mediafire.com/clx5xy4yc8cg/e9djjuiqup41hjj/twokingdoms.zip
License:	distributable
Group:		Games/Adventure
Url:		http://crystalshard.net/?g=3
BuildArch:	noarch
Requires:	ags
BuildRequires:	icoutils

%description
The ancient kingdom of Theylinn is beset by enemies. Within the castle walls,
nobles vie for the old King's favor, and not everybody is happy with the sole
heir to the throne, princess Rhiannon.

Meanwhile, danger approaches, in the form of an invading army, a hostile
giant, and a mercenary troop who are ancient enemies of the Theylann king...

A Tale of Two Kingdoms is a graphical adventure in the world of Celtic
mythology and fairy tales, with many sidequests and alternate endings. It was
named Game of the Month by PC Zone UK, and won four AGS Awards including
Best Animation and Best Puzzles. 

%prep
%setup -qcn %{name}

%build
wrestool -x --all ATOTK.exe >atotk.ico
icotool -x atotk.ico

%install
mkdir -p %{buildroot}%{_prefix}/games/%{name} \
	%{buildroot}%{_bindir} \
	%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/icons/hicolor/48x48/apps
cp -a acsetup.cfg ATOTK.exe Hungarian.tra Music.vox Sound.vox %{buildroot}%{_prefix}/games/%{name}
cp -a atotk*.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
cat >%{buildroot}%{_bindir}/%{name} <<'EOF'
#!/bin/sh
cd %{_prefix}/games/%{name}
exec %{_bindir}/ags ATOTK.exe
EOF
cat >%{buildroot}%{_datadir}/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Type=Application
Name=A Tale of Two Kingdoms
GenericName=Adventure Game
Exec=%{name}
Icon=%{name}
Categories=Game;AdventureGame;
EOF
chmod +x %{buildroot}%{_bindir}/%{name} %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/%{name}
%{_prefix}/games/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop

# -*- coding: utf-8 -*-

_CONTENT = """
#!/usr/bin/env xdg-open

[Desktop Entry]
Version=1.0

Type=Application
Categories=Development;Video;Utility;
Keywords=OpenCV;
Name=cvpm
Name[ko]=cvpm
GenericName=Computer Vision Player Agent
GenericName[ko]=Computer Vision Player Agent
Comment=Computer Vision Player Agent
Comment[ko]=Computer Vision Player Agent

TryExec=%HOME%/.cvpm/run
Exec=%HOME%/.cvpm/run
Path=%HOME%/.cvpm
Icon=%HOME%/.cvpm/icon.svg
MimeType=application/yaml

Terminal=false
Hidden=false
NoDisplay=false

StartupNotify=true
# StartupWMClass=cvpm

X-LXQt-Need-Tray=true
X-GNOME-Autostart-enabled=true
"""

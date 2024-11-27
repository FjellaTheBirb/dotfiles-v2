#!/bin/sh
xbindkeys &
#picom -b &
#feh --bg-scale ~/wallpapers/gnu_wall.png &
sh ~/.config/scripts/lemonbar_script.sh | lemonbar -g x20+0+10 -B "#000000" -f "JetBrains Mono:size=10" -p &

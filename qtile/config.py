from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.backend.wayland.inputs import InputConfig

mod = "mod4"
terminal = "xfce4-terminal"

keys = [
    # Переключение фокуса между окнами
    Key([mod], "left", lazy.layout.left(), desc="фокус в левое окно"),
    Key([mod], "right", lazy.layout.right(), desc="фокус в правое окно"),
    Key([mod], "down", lazy.layout.down(), desc="фокус в нижнее окно"),
    Key([mod], "up", lazy.layout.up(), desc="фокус в верхнее окно"),
    Key([mod], "space", lazy.layout.next(), desc="фокус на следующее окно"),
   
    # Перемещает окна
    Key([mod, "shift"], "left", lazy.layout.shuffle_left(), desc="переместит окно в лево"),
    Key([mod, "shift"], "right", lazy.layout.shuffle_right(), desc="переместит окно в право"),
    Key([mod, "shift"], "down", lazy.layout.shuffle_down(), desc="переместит окно в низ"),
    Key([mod, "shift"], "up", lazy.layout.shuffle_up(), desc="переместит окно вверх"),
   
    # Изменение размера окна
    Key([mod, "control"], "left", lazy.layout.grow_left()),
    Key([mod, "control"], "right", lazy.layout.grow_right()),
    Key([mod, "control"], "down", lazy.layout.grow_down()),
    Key([mod, "control"], "up", lazy.layout.grow_up()),
    Key([mod], "n", lazy.layout.normalize(), desc="Возвращает окно в прежнее состояние после изменения размера"),
    
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="split окна",),
    Key([mod], "Return", lazy.spawn(terminal), desc="старт терминала"),
    
    Key([mod], "Tab", lazy.next_layout(), desc="не понятно"),

    Key([mod], "q", lazy.window.kill(), desc="закрыть окно"),
    Key([mod, "control"], "f", lazy.window.toggle_fullscreen(), desc="окно во весь экран"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="окно в плавающий режим"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="перезагрузка конфига"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Выход из Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="типо dmenu запуск чего то"),

    # Аудио + - и mute
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

    # Яркость
    Key([], "XF86MonBrightnessUp", lazy.spawn("/river/.config/qtile/scripts/./brightness up")),

    # Приложения
    Key([mod, "shift"], "t", lazy.spawn("telegram-desktop"), desc="запуск телеги"),
    Key([mod, "shift"], "b", lazy.spawn("chromium --ozone-platform=wayland"), desc="запуск браузера")
]


groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    #Screen(
    #  wallpaper="$HOME/.config/sway/wallpapers/wallpaper.png",
    #  wallpaper_mode="stretch",
    #),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Volume(),
                widget.Clock(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),

        wallpaper='/home/river/.config/qtile/wallpapers/wallpaper1.png',
        wallpaper_mode='fill'
   ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False

floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# если прога хочет свернутся то пусть делает это
auto_minimize = True

########### ПЕРЕКЛЮЧЕНИЕ РАСКЛАДКИ ##########
wl_input_rules = True

wl_input_rules = {
    "type:keyboard": InputConfig(
        kb_layout="us,ru",
        kb_variant=",winkeys",
        kb_options="grp:alt_shift_toggle",
    ),
}
#############################################

# нужно если java прога не работает нормально
wmname = "LG3D"

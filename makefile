install: uninstall
	mkdir ~/.mm_FontSwitcher
	cp -fv mm_FontSwitcher.py ~/.mm_FontSwitcher
	cp -fv tharlon.ttf ~/.fonts
	cp -fv .fonts.conf ~/
	cp -fv ./install/mm_fontswitcher_icon.desktop ~/.local/share/applications
	./install/traylist add

uninstall:
	rm -rfv ~/.mm_FontSwitcher
	rm -fv ~/.local/share/applications/mm_fontswitcher_icon.desktop
	./install/traylist remove

.PHONY: install uninstall

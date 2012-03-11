install: uninstall
	mkdir ~/.mm_FontSwitcher
	cp -fv mm_FontSwitcher.py ~/.mm_FontSwitcher
	mkdir -p ~/.fonts
	cp -fv tharlon.ttf ~/.fonts
	cp -fv .fonts.conf ~/
	cp -fv ./install/mm-fontswitcher-icon.desktop ~/.local/share/applications
	./install/traylist add

uninstall:
	rm -rfv ~/.mm_FontSwitcher
	rm -fv ~/.local/share/applications/mm-fontswitcher-icon.desktop
	./install/traylist remove

.PHONY: install uninstall

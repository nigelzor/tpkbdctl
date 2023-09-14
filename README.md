# tpkbdctl

Simple configurator for the "Lenovo ThinkPad USB Keyboard with TrackPoint". 
By default, the TrackPoint is very, very slow. Under Linux I can modify sensitivity through sysfs, but in MacOS a helper is needed.

Consider this a much-simplified copy of https://github.com/bseibold/tpkbdctl.

```sh
# setup:
brew install hidapi
python3 -m venv venv
venv/bin/pip install hid
# after plugging in the keyboard:
venv/bin/python configure.py
```

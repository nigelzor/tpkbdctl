# tpkbdctl

Simple configurator for the "Lenovo ThinkPad USB Keyboard with TrackPoint". 
By default, the TrackPoint is very, very slow. Under Linux I can modify sensitivity through sysfs, but in MacOS a helper is needed.

Consider this a much-simplified copy of https://github.com/bseibold/tpkbdctl.

## macOS

```sh
python3 -m venv venv
venv/bin/pip install hidapi
# after plugging in the keyboard:
venv/bin/python configure.py
```

## Windows

```powershell
# requires uv (https://docs.astral.sh/uv/)
uv venv --python cpython-3.12-windows-x86_64
uv pip install hidapi
# after plugging in the keyboard:
.venv\Scripts\python.exe configure.py
```

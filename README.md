# Wanhao D12 Marlin Firmware

Important this repository use git-lfs to store binary data please take this is mind when you clone / pull  push

## How to install build environment
- System Requirements : 
  - python3
  - pipenv
### Install system requirements
#### Debian/Ubuntu 
```
  # As root (with or without sudo)
  apt update && apt install --no-install-recommends python3 python3-pip
  # As normal user
  pip3 install --user -U pipenv
  # After this make sure $HOME/.local/bin is in your path, usually this is done when you open a terminal / session
  # you can check with echo $PATH | grep .local/bin
```
#### Centos/Redhat/Fedora
```
  # As root (with or without sudo)
  dnf install python3 python3-pip
  # As normal user
  pip3 install --user -U pipenv
  # After this make sure $HOME/.local/bin is in your path, usually this is done when you open a terminal / session
  # you can check with echo $PATH | grep .local/bin
```

### Instalation of platformio environment
```
  > git clone <repository>
  > cd MarlinFirmware
  > PIPENV_VENV_IN_PROJECT="enabled" pipenv install
  > pipenv shell
```

### First compilation (Sanity Build)
This command should install ststm32 and the toolchain
```
  > platformio run -e wanhao__d12__230
```
# Wanhao D12 Marlin Firmware
---
Important this repository use git-lfs to store binary data please take this is mind when you clone / pull  push

## First Big Thanks !
- Ludo from Youtube channel <https://www.youtube.com/c/LeLudoLab> from its 1st firmware try and assets bundle
- Cidrixx, Jonathan06 from LesImprimantes3D.fr for the time he spends on discord to help me deal with this, and the first tuto available here 
  - <https://www.lesimprimantes3d.fr/forum/topic/40717-tuto-firmware-personnalis%C3%A9-wanhao-d12-comment-compiler-son-firmware/>
- Wanhao Teams to make vendors firmware available
- MKS Teams <https://github.com/makerbase-mks/MKS-Robin-Nano-Firmware>

## I just wan't an OOTB Firmware
You don't wan't to build your own firmware ?

You can download easily our releases or Vendor / Community here :
- https://github.com/jynolen/WanhaoD12/releases
  - Go [here](#Environment-Predifined) to be sure which one you want
- https://github.com/jynolen/WanhaoD12/tree/master/Firmware/Community_Firmware
- https://github.com/jynolen/WanhaoD12/tree/master/Firmware/Wanhao_Firmware

If you download Community or Vendor be sure to grab:
  - mks_font directory
  - mks_pic directory
  - Robin_nano35.bin file
  - robin_nano35_cfg.txt file

## How to flash your Wanhao

1. Pick the firmware of your dream it can be download from github releases or directly in Firmware Folder
2. Pick the assets bundle you want, goto releases and look for Assets.%%.zip
3. Copy content of zip onto your sd
4. Copy Firmware on your SD-Card
5. Insert SD Card into Wanhao D12
6. Wait and Enjoy


## How to convert Assets for my Wanhao
You will see that Assets folder contains png image.
This is not images suitable for your printer you will have to convert them.
- First choose the bundle you want 
- Download and extract the zip somewhere
- Go to https://baizhongyun.cn/home/mkstoolview
  - Board Series : MKS Robin Series
  - Board Type: MKS Robin Nano V1.x-TFT32
  - Firmware Type: MKS Robin Nano-V1.x-TFT35-Marlin-2.0.6
- Import the folder you just extract
  - Make sure all image load perfectly
- Go to Export
  - Select Display UI
  - Font Family
- Export And Extract mksbin.zip on your sd card

## How to install build environment
- System Requirements : 
  - git
  - python3
  - pipenv
  - libcairo2 (for svg convertion)

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
Those commands will download current project and install all dependencies
```
  > git clone https://github.com/jynolen/WanhaoD12.git
  > cd WanhaoD12
  > PIPENV_VENV_IN_PROJECT="enabled" pipenv install
```

## How to compile your own firmware
### First compilation (Sanity Build)
First you should check that what you just cloned works Out of the box. If not you probably have an issue seting up the environement

This command will install ststm32 platforme (the board CPU), toolchain (what is needed to compile)
```
  > pipenv run platformio run -e wanhao__d12__230
```
7
After few minutes you should see at the end of the output
```
====== [SUCCESS] Took 70.88 seconds ======

Environment       Status    Duration
----------------  --------  ------------
wanhao__d12__230  SUCCESS   00:01:10.883
====== 1 succeeded in 00:01:10.883 ======
```

Congratulation you successfully build your first firmware !
You can find it directly in folder 
`WanhaoD12/AutoBuild-MarlinFirware/.pio/build/wanhao__d12__230/out/Robin_nano35.bin`

### How to select a custom firmware
If you don't have a D12/230 but a D12/300 you want the 300 flavor of the firmware.
No worries we covered you !
Just replace 230 by 300 in the following CLI
```
  > pipenv run platformio run -e wanhao__d12__230
  > # Replaced by 
  > pipenv run platformio run -e wanhao__d12__300
```
Firmware will be available in folder
`WanhaoD12/AutoBuild-MarlinFirware/.pio/build/wanhao__d12__300/out/Robin_nano35.bin`

### Environment Predifined

Here the list of all predefined firmware that are build by the repository

|         Environment / Features        | Bed Size | BLtouch | Marlin Stock UI | MKS UI | Clean Nozzles | Materials Preheat | Custom User Commands | GCode Macros | Skew Compensation |
|:-------------------------------------:|----------|---------|-----------------|--------|---------------|-------------------|----------------------|--------------|-------------------|
| wanhao__d12__230                      | 230      |         | yes             |        |               |                   |                      |              |                   |
| wanhao__d12__230__bltouch             | 230      | Yes     | yes             |        |               |                   |                      |              |                   |
| wanhao__d12__230__full                | 230      |         | yes             |        | yes           | yes               | yes                  | yes          |                   |
| wanhao__d12__230__full                | 300      | Yes     | yes             |        | yes           | yes               | yes                  | yes          |                   |
| wanhao__d12__230                      | 300      |         | yes             |        |               |                   |                      |              |                   |
| wanhao__d12__230__bltouch             | 300      | Yes     | yes             |        |               |                   |                      |              |                   |
| wanhao__d12__230__full                | 300      |         | yes             |        | yes           | yes               | yes                  | yes          |                   |
| wanhao__d12__230__full                | 300      | Yes     | yes             |        | yes           | yes               | yes                  | yes          |                   |
|                                       |          |         |                 |        |               |                   |                      |              |                   |
| wanhao__d12__lvgl__230                | 230      |         |                 | yes    |               |                   |                      |              |                   |
| wanhao__d12__lvgl__230__bltouch       | 230      | Yes     |                 | yes    |               |                   |                      |              |                   |
| wanhao__d12__lvgl__230__full          | 230      |         |                 | yes    | yes           | yes               | yes                  | yes          |                   |
| wanhao__d12__lvgl__230__full__bltouch | 230      |         |                 | yes    | yes           | yes               | yes                  | yes          |                   |
| wanhao__d12__lvgl__300                | 300      | Yes     |                 | yes    | yes           | yes               | yes                  | yes          |                   |
| wanhao__d12__lvgl__300__bltouch       | 300      |         |                 | yes    |               |                   |                      |              |                   |
| wanhao__d12__lvgl__300__full          | 300      | Yes     |                 | yes    |               |                   |                      |              |                   |
| wanhao__d12__lvgl__300__full__bltouch | 300      |         |                 | yes    | yes           | yes               | yes                  | yes          |                   |

### Extra Features
- Clean Nozzles
  - Enable GCODE G12 - <https://marlinfw.org/docs/gcode/G012.html>
  - Check WanhaoD12.h `#ifdef WD12_CLEAN_NOZZLE <settings> #endif` block
- BLtouch
  - Enable Z Sensor and Autobed leveling
  - Check WanhaoD12.h `#ifdef WD12_BLTOUCH <settings> #endif` block  
- MKS UI
  - Enable The Makerbase UI (with icons)
  - Check WanhaoD12.h `#ifdef WD12_BLTOUCH <settings> #endif` block    
- Marlin Stock UI
  - Enable the Marlin Stock UI
  - Enable GCode M600 as a bonus effect
- Materials Preheat
  - Enable Preheat Button on the UI (PLA & ABS)
- Custom User Commands
  - Enable Custom Menus options
-  GCode Macros
  - Enable Gcode M810-M819 to defined macros

### How to build your custom the firmware
Just put the hand into WanhaoD12.h, Configuration.h or Configuration_adv.h
#### Edit platformio.ini
You can add the following snippet to platformio.ini
```
[env:custom]
extends         = mks_robin_nano35
build_flags     = ${mks_robin_nano35.build_flags} -DD12230
```

#### Define variables
You might want to define some constants. You can do it directly within the code by removing / adding "//" characters 
Or you can defined build flags in platformio

```
/**
 * If you want to enable the following variable without touching anythin in the .h file
 */
//#define FOOBAR

Just open platformio.ini
And edit your env
[env:custom]
extends         = mks_robin_nano35
build_flags     = ${mks_robin_nano35.build_flags} -DFOOBAR
```

#### Built it !
You can now built it with 
```
  > pipenv run platformio run -e custom
```


## How to contribute to this project

Collaboration is welcome ! Just fork the repository make your change and pull request.
"Ok not so simple"
1. Create a github account
2. Click Fork on top right of the repository landing page
3. Cloned your forked repo
4. Create a branch with command
   1. `git checkout -b <name of your branch>`
5. Make whatever you want
6. Create a pull requests

## Next things to do
- Include Slicers Profiles
- ...
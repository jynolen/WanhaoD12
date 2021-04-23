# Wanhao D12 Marlin Firmware

Important this repository use git-lfs to store binary data please take this is mind when you clone / pull  push

## I just wan't an OOTB Firmware
You don't wan't to build your own firmware ?
You can download easily our releases OR browse into CommunityFirmware / Vendor-Firmware to download them
If you download Community or Vendor be sure to grab (mks_font, mks_pic, Robin_nano35.bin and robin_nano35_cfg.txt)

## How to install build environment
- System Requirements : 
  - git
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
Those commands will download current project and install all dependencies
```
  > git clone https://github.com/jynolen/WanhaoD12.git
  > cd WanhaoD12/AutoBuild-MarlinFirware
  > PIPENV_VENV_IN_PROJECT="enabled" pipenv install
  > pipenv shell
```

### First compilation (Sanity Build)
This command should install ststm32 platforme (the board CPU), toolchain (what is needed to compile)
```
  > platformio run -e wanhao__d12__230
```
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
If you don't have a D12/230 but a D12/300 you want this specific firmware.
No worries we covered you !
Just replace 230 by 300 in the following CLI
```
  > platformio run -e wanhao__d12__230
  > # Replaced to 
  > platformio run -e wanhao__d12__300
```
Firmware will be available in folder
`WanhaoD12/AutoBuild-MarlinFirware/.pio/build/wanhao__d12__300/out/Robin_nano35.bin`

### How to flash your Wanhao
Pick the firmware of your dream (Community, Vendor, Releases, Selfbuild)
Be sure to have 
  - mks_font (not needed for Marlin Stock UI)
  - mks_pic (not needed for Marlin Stock UI)
  - Robin_nano35.bin
  - robin_nano35_cfg.txt  (not needed for Marlin Firware)

Next
   - Copy each on the root of a SDCard. Please use a good quality SDCard, you don't want to brick your board because of bad SDCard
   - Be sure to eject it normally
   - Insert SD into your Power Off Wanhao
   - Power up
   - Wait
   - Enjoy

### Environment Predifined
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
#### Buit it !
You can now built it with 
```
  > platformio run -e custom
```
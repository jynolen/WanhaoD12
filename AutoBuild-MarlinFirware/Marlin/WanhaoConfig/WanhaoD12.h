/**
 * WanhaoD12.h
 *
 * Basic settings such as:
 *
 * - Specific Configuration of Wanhao
 *
 * Advanced settings can be found in Configuration_adv.h
 */

/** If we do our job correctly you should have only to comment / uncomment 
 *  options here
 *  you still can override values we put b default
 */
#pragma once


#define STRING_CONFIG_H_AUTHOR "(MagicTeam, Wanhao D12 dual)" // Jonathan06, remibora, fmelle, jynolen

//#define D12230 // Only if you have a D12/230
//#define D12300 // Only if you have a D12/300

#if defined(D12230) && defined(D12300)
    #error "Enable only one of D12230 or D12300."
#endif

#if !defined(D12230) && !defined(D12300)
    #error "Exactly one of D12230 or D12300 should be defined"
#endif


//#define WD12_BLTOUCH // Only if you have a BLTouch

// Those two options are mutually exclusive (you can only choose one)

//#define WD12_UI_TYPE_MARLIN_STOCK // Stock Marlin like with LCD only - Can use M600 GCODE
//#define WD12_UI_TYPE_TFT_LVGL // Nice UI with icons text etc. - Cannot use M600 GCODE

#if defined(WD12_UI_TYPE_MARLIN_STOCK) && defined(WD12_UI_TYPE_TFT_LVGL)
    #error "Enable only one of WD12_UI_TYPE_MARLIN_STOCK or WD12_UI_TYPE_TFT_LVGL."
#endif

#if !defined(WD12_UI_TYPE_MARLIN_STOCK) && !defined(WD12_UI_TYPE_TFT_LVGL)
    #error "Exactly one of WD12_UI_TYPE_MARLIN_STOCK or WD12_UI_TYPE_TFT_LVGL should be defined"
#endif

// If you done a Skew Compensation (After a first build without)
//#define WD12_SKEW_COMPENSATION

// If you want to have some Materials Preset
//#define WD12_MATERIALS

// If you want to Enable clean nozzle feature (experimental)
//#define WD12_CLEAN_NOZZLE

//If you want to use GCode Macros
//#define WD12_GCODE_MACROS

//If you want to use Custom Menus
//#define WD12_CUSTOM_USER_MENUS

/**
 * Commons
 */
#if defined(D12230) || defined(D12300)
#include "WanhaoD12-Common.h"
#endif

/**
 * BL Touch
 */
#include "WanhaoD12-Bltouch.h"

/**
 * Bed Size
 */
#ifdef D12230
#include "WanhaoD12-230.h"
#endif

#ifdef D12300
#include "WanhaoD12-300.h"
#endif

/**
 * Display
 */
#ifdef WD12_UI_TYPE_MARLIN_STOCK
#include "WanhaoD12-ClassicUI.h"
#endif

#ifdef WD12_UI_TYPE_TFT_LVGL
#include "WanhaoD12-LVGL.h"
#endif

/**
 * Extra Features
 */
#include "WanhaoD12-Features.h"
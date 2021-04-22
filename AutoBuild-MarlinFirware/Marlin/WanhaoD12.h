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
// Please pay attention here of LANGUAGE
#define WD12_LCD_LANGUAGE fr
#define WD12_DISPLAY_CHARSET WESTERN

#define WD12_SERIALPORT 3
#define WD12_BAUDRATE 250000
#define WD12_MOTHERBOARD BOARD_MKS_ROBIN_NANO
#define WD12_EXTRUDERS 2 // #WD12 Wanhao D12-230 has 2 extruders
#define SINGLENOZZLE // #WD12 Wanhao D12-230 has a shared nozzle
#define WD12_TEMP_SENSOR_0 1
#define WD12_TEMP_SENSOR_BED 1 // #WD12 Wanhao D12-230 has a heated bed 
#define WD12_HEATER_0_MAXTEMP 245 // #WD12 Wanhao D12-230 has a heated bed 
#define WD12_BED_MAXTEMP 100 // #WD12 Wanhao D12-230 has a heated bed 

#define WD12_DEFAULT_Kp_LIST {  17.54,  17.54 }
#define WD12_DEFAULT_Ki_LIST {   0.73,   0.73 }
#define WD12_DEFAULT_Kd_LIST { 105.35, 105.35 }

#define WD12_DEFAULT_Kp 17.54
#define WD12_DEFAULT_Ki 0.73
#define WD12_DEFAULT_Kd 105.35

#define WD12_EXTRUDE_MAXLENGTH 600 // #Bowden

#define PIDTEMPBED // If you want to be able to PID tune the Bed
#define WD12_DEFAULT_bedKp  18.24 	// #WD12
#define WD12_DEFAULT_bedKi  3.45 	// #WD12
#define WD12_DEFAULT_bedKd  64.36	// #WD12

#define WD12_X_DRIVER_TYPE TMC2209_STANDALONE // #WD12 TMC2209_STANDALONE on stock D12-230
#define WD12_Y_DRIVER_TYPE TMC2209_STANDALONE // #WD12 TMC2209_STANDALONE on stock D12-230
#define WD12_Z_DRIVER_TYPE A4988				// #WD12
#define WD12_E0_DRIVER_TYPE A4988			// #WD12
#define WD12_E1_DRIVER_TYPE A4988			// #WD12

#define DISTINCT_E_FACTORS // If you want to have different values for each extruder
#define WD12_DEFAULT_AXIS_STEPS_PER_UNIT   { 80.00, 80.00, 400.50, 381, 381 }
#define WD12_DEFAULT_MAX_FEEDRATE  { 200, 200, 4, 70, 70 } // #WD12 M203 X500.00 Y500.00 Z10.00 / M203 T0 E60.00
#define WD12_DEFAULT_MAX_ACCELERATION { 500, 500, 100, 1000, 1000 }

// Limit edit via M203 or LCD to DEFAULT_MAX_FEEDRATE * 2
#define WD12_MAX_FEEDRATE_EDIT_VALUES { 600, 600, 10, 70 }
// Limit edit via M203 or LCD to DEFAULT_MAX_FEEDRATE * 2
#define WD12_MAX_ACCEL_EDIT_VALUES { 6000, 6000, 500, 20000 }

#define WD12_DEFAULT_ACCELERATION          500    // #WD12 X, Y, Z and E acceleration for printing moves
#define WD12_DEFAULT_RETRACT_ACCELERATION  500    // #WD12 E acceleration for retracts
#define WD12_DEFAULT_TRAVEL_ACCELERATION   500    // #WD12 X, Y, Z acceleration for travel (non printing) moves

#define CLASSIC_JERK
#define WD12_DEFAULT_XJERK 20.0 // #WD12
#define WD12_DEFAULT_YJERK 20.0 // #WD12
#define WD12_DEFAULT_ZJERK 0.4  // #WD12
#define WD12_DEFAULT_EJERK 5.0  // #WD12 May be used by Linear Advance

#define WD12_NUM_RUNOUT_SENSORS 2
#define WD12_FIL_RUNOUT_PIN PA4
#define WD12_FIL_RUNOUT2_PIN PE6
#define WD12_FIL_RUNOUT_STATE LOW

#define LEVEL_BED_CORNERS //#WD12
#define Z_SAFE_HOMING

#define EEPROM_SETTINGS
#define EEPROM_AUTO_INIT

#define NOZZLE_PARK_FEATURE
#define WD12_NOZZLE_PARK_POINT { (X_MIN_POS + 5), (Y_MAX_POS - 5), 20 }

#define SDSUPPORT
#define WD12_SPI_SPEED SPI_HALF_SPEED
//#define SD_CHECK_AND_RETRY

#define MKS_ROBIN_TFT35
#define SERVO_DELAY { 750 }

/**
 * Materials
 */
#define WD12_PREHEAT_1_LABEL       "PLA"
#define WD12_PREHEAT_1_TEMP_HOTEND 200
#define WD12_PREHEAT_1_TEMP_BED     70
#define WD12_PREHEAT_1_FAN_SPEED     0 // Value from 0 to 255

#define WD12_PREHEAT_2_LABEL       "ABS"
#define WD12_PREHEAT_2_TEMP_HOTEND 220
#define WD12_PREHEAT_2_TEMP_BED     90
#define WD12_PREHEAT_2_FAN_SPEED     0 // Value from 0 to 255

//Configuration Advanced
#define WD12_THERMAL_PROTECTION_HYSTERESIS 10
#define WD12_WATCH_TEMP_PERIOD 40
#define WD12_THERMAL_PROTECTION_BED_PERIOD 40 
#define WD12_DEFAULT_STEPPER_DEACTIVE_TIME 600
#define LIN_ADVANCE
#define WD12_LIN_ADVANCE_K 0
#endif

/**
 * BL Touch
 */
#ifdef WD12_BLTOUCH
#define BLTOUCH
#define Z_MIN_PROBE_USES_Z_MIN_ENDSTOP_PIN 
#define USE_PROBE_FOR_Z_HOMING
#define WD12_Z_MIN_PROBE_PIN PC4
#define WD12_NOZZLE_TO_PROBE_OFFSET { -45.5, -5.0, 0 }
#define MULTIPLE_PROBING 3  // #WD12 if BLT
#define EXTRA_PROBING    1  // #WD12 if BLT

#define AUTO_BED_LEVELING_BILINEAR
#define G26_MESH_VALIDATION
#define WD12_GRID_MAX_POINTS_X 7
#define WD12_GRID_MAX_POINTS_Y 7
#define LEVEL_CORNERS_USE_PROBE
#define WD12_BLTOUCH_DELAY 1000
#endif

/**
 * Bed Size
 */
#ifdef D12230
#define WD12_CUSTOM_MACHINE_NAME "Wanhao D12-230"
#define WD12_X_BED_SIZE 230 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_Y_BED_SIZE 230 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_X_MAX_POS 256   // WD12 X_BED_SIZE
#define WD12_Z_MAX_POS 240
#define WD12_LEVEL_CORNERS_INSET_LFRB { 30, 30, 30, 30 } // (mm) Left, Front, Right, Back insets
#define WD12_NOZZLE_CLEAN_START_POINT { {  5, 5, (Z_MIN_POS + 1) } }
#define WD12_NOZZLE_CLEAN_END_POINT { { 60, 20, (Z_MIN_POS + 1) } }
#endif

#ifdef D12300
#define WD12_CUSTOM_MACHINE_NAME "Wanhao D12-300"
#define WD12_X_BED_SIZE 300 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_Y_BED_SIZE 300 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_X_MAX_POS 300   // WD12 X_BED_SIZE
#define WD12_Z_MAX_POS 400
#define WD12_LEVEL_CORNERS_INSET_LFRB { 40, 40, 40, 40 } // (mm) Left, Front, Right, Back insets
#define WD12_NOZZLE_CLEAN_START_POINT { {  5, 5, (Z_MIN_POS + 1) } }
#define WD12_NOZZLE_CLEAN_END_POINT { { 80, 30, (Z_MIN_POS + 1) } }
#endif

/**
 * Display
 */
#ifdef WD12_UI_TYPE_MARLIN_STOCK
#define WD12_FILAMENT_RUNOUT_SCRIPT "M600"
#define TFT_COLOR_UI
#define TOUCH_SCREEN
#define ADVANCED_PAUSE_FEATURE
#define FILAMENT_RUNOUT_SENSOR
#endif

#ifdef WD12_UI_TYPE_TFT_LVGL
#define WD12_FILAMENT_RUNOUT_SCRIPT "M600"
#define TFT_LVGL_UI
#endif

/**
 * Skew Compensation
 */
#ifdef WD12_SKEW_COMPENSATION
#define SKEW_CORRECTION
#define SKEW_CORRECTION_FOR_Z
#define SKEW_CORRECTION_GCODE

#define WD12_XY_DIAG_AC 282.8427124746
#define WD12_XY_DIAG_BD 282.8427124746
#define WD12_XZ_DIAG_AC 282.8427124746
#define WD12_XZ_DIAG_BD 282.8427124746
#define WD12_YZ_DIAG_AC 282.8427124746
#define WD12_YZ_DIAG_BD 282.8427124746

#define WD12_XY_SIDE_AD 200
#define WD12_YZ_SIDE_AD 200

#define WD12_XY_SKEW_FACTOR 0.0
#define WD12_XZ_SKEW_FACTOR 0.0
#define WD12_YZ_SKEW_FACTOR 0.0
#endif

/**
 * Clean Nozzle
 */
#ifdef WD12_CLEAN_NOZZLE
#define NOZZLE_CLEAN_FEATURE
#define WD12_NOZZLE_CLEAN_STROKES 12
#define WD12_NOZZLE_CLEAN_TRIANGLES 3
#define WD12_NOZZLE_CLEAN_CIRCLE_RADIUS 4
#define WD12_NOZZLE_CLEAN_CIRCLE_FN 10
#define WD12_NOZZLE_CLEAN_MIN_TEMP 185
#endif

/**
 * Gcode Macros
 */
#ifdef WD12_GCODE_MACROS
#define GCODE_MACROS
#define WD12_GCODE_MACROS_SLOTS       5  // Up to 10 may be used
#define WD12_GCODE_MACROS_SLOT_SIZE  50  // Maximum length of a single macro
#endif

/**
 * Custom Menus
 */
#ifdef WD12_CUSTOM_USER_MENUS
#define WD12_CUSTOM_USER_MENU_TITLE "Custom WD12 Commands"
#define WD12_USER_SCRIPT_DONE "M117 User Script Done"

#ifdef WD12_MATERIALS
#define USER_CMD_1_ENABLE
#define WD12_USER_DESC_1 WD12_PREHEAT_1_LABEL                         //PLA
#define WD12_USER_GCODE_1 "M140 S" STRINGIFY(WD12_PREHEAT_1_TEMP_BED) "\nM104 S" STRINGIFY(WD12_PREHEAT_1_TEMP_HOTEND)

#define USER_CMD_2_ENABLE
#define WD12_USER_DESC_2 WD12_PREHEAT_2_LABEL                         //ABS
#define WD12_USER_GCODE_2 "M140 S" STRINGIFY(WD12_PREHEAT_2_TEMP_BED) "\nM104 S" STRINGIFY(WD12_PREHEAT_2_TEMP_HOTEND)
#endif
#endif
#pragma once


// Please pay attention here of LANGUAGE
#define WD12_LCD_LANGUAGE fr
#define WD12_DISPLAY_CHARSET WESTERN

#define WD12_SERIALPORT 3
#define WD12_BAUDRATE 250000
#define MOTHERBOARD BOARD_MKS_ROBIN_NANO
#define WD12_EXTRUDERS 2 // #WD12 Wanhao D12-230 has 2 extruders
#define SINGLENOZZLE // #WD12 Wanhao D12-230 has a shared nozzle
#define WD12_TEMP_SENSOR_0 1
#define WD12_TEMP_SENSOR_BED 1 // #WD12 Wanhao D12-230 has a heated bed 
#define WD12_HEATER_0_MAXTEMP 245 // #WD12 Wanhao D12-230 has a heated bed 
#define WD12_BED_MAXTEMP 100 // #WD12 Wanhao D12-230 has a heated bed 

#define WD12_EXTRUDE_MAXLENGTH 600 // #Bowden

//#define PIDTEMPBED // If you want to be able to PID tune the Bed

#define WD12_X_DRIVER_TYPE TMC2209_STANDALONE // #WD12 TMC2209_STANDALONE on stock D12-230
#define WD12_Y_DRIVER_TYPE TMC2209_STANDALONE // #WD12 TMC2209_STANDALONE on stock D12-230

#define DISTINCT_E_FACTORS // If you want to have different values for each extruder
#define WD12_DEFAULT_AXIS_STEPS_PER_UNIT   { 80.00, 80.00, 400.50, 385, 385 }
#define WD12_DEFAULT_MAX_FEEDRATE  { 200, 200, 5, 50, 50 } // #WD12 M203 X500.00 Y500.00 Z10.00 / M203 T0 E60.00
#define WD12_DEFAULT_MAX_ACCELERATION { 500, 500, 100, 1000, 1000 }

// Limit edit via M203 or LCD to DEFAULT_MAX_FEEDRATE * 2
#define WD12_MAX_FEEDRATE_EDIT_VALUES { 600, 600, 10, 70 }
// Limit edit via M203 or LCD to DEFAULT_MAX_FEEDRATE * 2
#define WD12_MAX_ACCEL_EDIT_VALUES { 6000, 6000, 500, 20000 }

#define WD12_DEFAULT_ACCELERATION          500    // #WD12 X, Y, Z and E acceleration for printing moves
#define WD12_DEFAULT_RETRACT_ACCELERATION  500    // #WD12 E acceleration for retracts
#define WD12_DEFAULT_TRAVEL_ACCELERATION   500    // #WD12 X, Y, Z acceleration for travel (non printing) moves


#define WD12_DEFAULT_Kp_LIST {  27.35,  27.35 }
#define WD12_DEFAULT_Ki_LIST {   1.71,   1.71 }
#define WD12_DEFAULT_Kd_LIST { 109.14, 109.14 }

#define WD12_DEFAULT_Kp 27.35
#define WD12_DEFAULT_Ki 1.71
#define WD12_DEFAULT_Kd 109.14

#define CLASSIC_JERK
#define WD12_DEFAULT_XJERK 10.0 // #WD12
#define WD12_DEFAULT_YJERK 10.0 // #WD12
#define WD12_DEFAULT_ZJERK 0.4  // #WD12
#define WD12_DEFAULT_EJERK 1.0  // #WD12 May be used by Linear Advance

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
#define WD12_TOUCH_ORIENTATION TOUCH_LANDSCAPE

#define MKS_ROBIN_TFT35
#define WD12_SERVO_DELAY { 750 }

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

#define WD12_INVERT_ENDSTOP true
#define WD12_INVERT_E0_DIR  true
#define WD12_INVERT_E1_DIR  true

#define TOUCH_SCREEN
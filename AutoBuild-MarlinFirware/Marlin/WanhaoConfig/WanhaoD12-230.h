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
#define WD12_CUSTOM_MACHINE_NAME "Wanhao D12-230"
#define WD12_X_BED_SIZE 230 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_Y_BED_SIZE 230 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_X_MAX_POS 256   // WD12 X_BED_SIZE
#define WD12_Y_MAX_POS WD12_Y_BED_SIZE
#define WD12_Z_MAX_POS 240
#define WD12_LEVEL_CORNERS_INSET_LFRB { 50, 50, 50, 50 } // (mm) Left, Front, Right, Back insets
#define WD12_NOZZLE_CLEAN_START_POINT { {  5, 5, (Z_MIN_POS + 1) } }
#define WD12_NOZZLE_CLEAN_END_POINT { { 60, 20, (Z_MIN_POS + 1) } }
#define WD12_INVERT_X_DIR false
#define WD12_INVERT_Y_DIR true
#define WD12_INVERT_Z_DIR true


#define WD12_Z_DRIVER_TYPE A4988				// #WD12
#define WD12_E0_DRIVER_TYPE A4988			// #WD12
#define WD12_E1_DRIVER_TYPE A4988			// #WD12


#define WD12_DEFAULT_bedKp  10.00 	// #WD12-230
#define WD12_DEFAULT_bedKi  0.023 	// #WD12-230
#define WD12_DEFAULT_bedKd  305.4	// #WD12-230

#pragma once

#define WD12_CUSTOM_MACHINE_NAME "Wanhao D12-300"
#define WD12_X_BED_SIZE 300 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_Y_BED_SIZE 300 // #WD12 Wanhao D12-230 has a 230mm x 230mm Bed
#define WD12_X_MAX_POS 300   // WD12 X_BED_SIZE
#define WD12_Y_MAX_POS WD12_Y_BED_SIZE
#define WD12_Z_MAX_POS 400
#define WD12_LEVEL_CORNERS_INSET_LFRB { 50, 50, 50, 50 } // (mm) Left, Front, Right, Back insets
#define WD12_NOZZLE_CLEAN_START_POINT { {  5, 5, (Z_MIN_POS + 1) } }
#define WD12_NOZZLE_CLEAN_END_POINT { { 80, 30, (Z_MIN_POS + 1) } }
#define WD12_INVERT_X_DIR false
#define WD12_INVERT_Y_DIR true
#define WD12_INVERT_Z_DIR false
#define WD12_DEFAULT_bedKp  10.00 	// #WD12
#define WD12_DEFAULT_bedKi  0.023 	// #WD12
#define WD12_DEFAULT_bedKd  305.4	// #WD12
#define WD12_Z_DRIVER_TYPE TMC2209_STANDALONE
#define WD12_E0_DRIVER_TYPE TMC2209_STANDALONE			// #WD12
#define WD12_E1_DRIVER_TYPE TMC2209_STANDALONE			// #WD12
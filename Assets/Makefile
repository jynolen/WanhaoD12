TARGET_DIR=.build

SRC_DIR_ASSETS=$(shell find Assets -maxdepth 1 -mindepth 1 -type d -not -name Community) $(shell find Assets/Community -maxdepth 1 -mindepth 1 -type d)
TARGET_NAME=$(subst Assets/,,$(SRC_DIR_ASSETS))
TARGET_DIRS=$(addsuffix /,$(addprefix $(TARGET_DIR)/,$(TARGET_NAME)))
SRC_FILES=$(foreach src_dir,$(SRC_DIR_ASSETS), $(wildcard $(src_dir)/svg/*.svg ))
TGT_FILES=$(subst .svg,.bin,$(subst /svg,,$(subst Assets/,.build/,$(SRC_FILES))))

.PHONY:all
all:

$(TARGET_DIRS):
	mkdir -p $@

$(TGT_FILES):
	$(eval S_FILE=$(notdir $(patsubst %.bin,%.svg,$@)))
	$(eval S_FOLDER=$(dir $(subst $(TARGET_DIR),,$@)))
	$(eval S_FILE=$(shell find -name $(S_FILE)|grep $(S_FOLDER) ))
	pipenv run python -m lvgl.converter --output_format bin_565 --color_format true_color $(S_FILE)
	@mv $(notdir $@) $@

.SECONDEXPANSION:
$(TARGET_NAME): $(TARGET_DIR)/$$@/ $$(filter $(TARGET_DIR)/$$@/%, $(TGT_FILES))
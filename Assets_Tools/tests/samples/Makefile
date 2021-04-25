
FULL_CF=true_color true_color_alpha true_color_chroma alpha_1 alpha_2 alpha_4 alpha_8 indexed_1 indexed_2 indexed_4 indexed_8
RAW_CF=raw raw_alpha raw_chroma
FULL_FORMAT=c_array bin_332 bin_565 bin_565_swap bin_888
COMPUTE_FULL=$(foreach img_file, $(IMG_FILES), $(RESULT_DIR)/$(notdir $(basename $(img_file))).${cf}.$(format).$(if ($(format) "c_array"), ".c",".bin"))
COMPUTE_CF=$(foreach cf, $(FULL_CF), $cf $format)

EXTENSION=$(if $(filter c_array, $(format)),c,bin)

result_dir = ./result
source_dir=sample_png
IMG_FILES = $(wildcard ./*.png) $(wildcard ./*.bmp)

COMPUTE_SOURCE=$(foreach format, $(FULL_FORMAT),										\
					$(foreach cf, $(FULL_CF),											\
						$(foreach img, $(IMG_FILES),									\
							$(result_dir)/$(notdir $(img)).$(cf).$(format).$(EXTENSION)	\
						)																\
					)																	\
				)
COMPUTE_RAW=	$(foreach format, c_array,												\
					$(foreach cf, $(RAW_CF),											\
						$(foreach img, $(IMG_FILES),									\
							$(result_dir)/$(notdir $(img)).$(cf).$(format).$(EXTENSION)	\
						)																\
					)																	\
				)				
TARGET=$(COMPUTE_SOURCE) $(COMPUTE_RAW)

split = $(subst /, ,$(subst ., ,$(1)))

F_CF = $(word 4,$(call split,$(1)))
F_FORMAT = $(word 5,$(call split,$(1)))
F_IMG=$(source_dir)/$(word 2,$(call split,$(1))).$(word 3,$(call split,$(1)))
F_NAME=$(word 2,$(call split,$(1)))
$(TARGET):
	$(eval CF=$(call F_CF,$@))
	$(eval FORMAT=$(call F_FORMAT,$@))
	$(eval IMG=$(call F_IMG,$@))
	$(eval NAME=$(call F_NAME,$@))
	php converter.php "name=$(NAME)&img=$(IMG)&cf=$(CF)&format=$(FORMAT)"
	mv $(NAME) $@


.PHONY: all
all: $(TARGET)

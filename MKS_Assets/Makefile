SRC = $(wildcard mks_pic/*.bin)
TGT = $(subst bin,png,$(subst mks_pic,result,$(SRC)))

$(TGT): $(SRC)
	python3 convert.py -o $@ mks_pic/$(subst png,bin,$(notdir $@))

.PHONY: all
all: $(TGT)
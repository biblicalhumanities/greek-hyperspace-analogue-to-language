EMDROS_PREFIX = /usr/bin
#EMDROS_PREFIX = /home/ulrikp/Ongoing/emdros/trunk/emdros/examples/HAL

HAL_BUILD_DB = $(EMDROS_PREFIX)/hal_build_db
MQLHAL = $(EMDROS_PREFIX)/mqlhal

CLEANFILES = nestle1904_strongs \
             haltest.out.txt \
             output_data/nestle1904.strongs.wordlist.txt \
             sql.txt HALSpace.cxt haltest.csv.txt \
             *~ *.pyc

all: input_data/nestle1904.strongs.txt nestle1904_strongs haltest.out.txt output_data/nestle1904.strongs.HAL.txt

clean:
	rm -f $(CLEANFILES)

#
# Useful for seeing how input_data/nestle1904.strongs.txt was built.
#
#input_data/nestle1904.strongs.txt: ../../Nestle1904/nestle1904.wpl.morph.txt
#	awk -F '\t' '{print $$5;}' $<  | awk -F '&' '{print $$1 + 0;}' > $@



# Requires at least Emdros 3.4.1.pre12 from 2015-06-20 or later,
# because we need the new --add-numbers switch
nestle1904_strongs: input_data/nestle1904.strongs.txt
	$(HAL_BUILD_DB) -b 3 -d $@ -f $< -o output_data/nestle1904.strongs.wordlist.txt  --add-numbers


haltest.out.txt: nestle1904_strongs hal.cfg
	$(MQLHAL) -b 3 -d $< -c hal.cfg 

output_data/nestle1904.strongs.HAL.txt: haltest.out.txt gather_hal.py input_data/stopwords.strongs.txt
	python gather_hal.py


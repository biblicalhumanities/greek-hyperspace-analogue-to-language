EMDROS_PREFIX = /usr/bin
#EMDROS_PREFIX = /home/ulrikp/Ongoing/emdros/trunk/emdros/examples/HAL

HAL_BUILD_DB = $(EMDROS_PREFIX)/hal_build_db
MQLHAL = $(EMDROS_PREFIX)/mqlhal

CLEANFILES = \
             nestle1904_strongs nestle1904_strongs.out.txt \
             output_data/nestle1904.strongs.wordlist.txt \
             nestle1904_strongs.csv.txt \
             nestle1904_nostopwords nestle1904_nostopwords.out.txt \
             output_data/nestle1904.nostopwords.wordlist.txt \
             nestle1904_nostopwords.csv.txt \
             output_data/nestle1904.nostopwords.txt \
             sql.txt HALSpace.cxt \
             *~ *.pyc

TARGETS_FULLHAL = \
     input_data/nestle1904.strongs.txt \
     nestle1904_strongs nestle1904_strongs.out.txt \
     output_data/nestle1904.strongs.HAL.txt

TARGETS_NOSTOPWORDSHAL = \
     nestle1904_nostopwords nestle1904_nostopwords.out.txt \
     output_data/nestle1904.nostopwords.HAL.txt


all: $(TARGETS_FULLHAL) $(TARGETS_NOSTOPWORDSHAL)


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

# Requires at least Emdros 3.4.1.pre12 from 2015-06-20 or later,
# because we need the new --add-numbers switch
nestle1904_nostopwords: output_data/nestle1904.nostopwords.txt
	$(HAL_BUILD_DB) -b 3 -d $@ -f $< -o output_data/nestle1904.nostopwords.wordlist.txt  --add-numbers

output_data/nestle1904.nostopwords.txt: input_data/nestle1904.strongs.txt input_data/stopwords.strongs.txt reduce.py
	python reduce.py input_data/stopwords.strongs.txt $< $@

nestle1904_strongs.out.txt: nestle1904_strongs hal.cfg
	$(MQLHAL) -b 3 -d $< -c hal.cfg 

nestle1904_nostopwords.out.txt: nestle1904_nostopwords hal_nostopwords.cfg
	$(MQLHAL) -b 3 -d $< -c hal_nostopwords.cfg 

output_data/nestle1904.strongs.HAL.txt: nestle1904_strongs.out.txt gather_hal.py input_data/stopwords.strongs.txt
	python gather_hal.py input_data/stopwords.strongs.txt $< $@

output_data/nestle1904.nostopwords.HAL.txt: nestle1904_nostopwords.out.txt gather_hal.py input_data/stopwords.strongs.txt
	python gather_hal.py input_data/stopwords.strongs.txt $< $@


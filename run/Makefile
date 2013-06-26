### 1.1 BIN INSTALLATION
bin:
	cd ../bin; make
### 1.2 COMMON OPTIONS
SRILM_PATH=/opt/srilm/bin/i686-m64
export PATH := ../../bin:.:${SRILM_PATH}:${PATH} # Binaries in the bin directory

SEED=1  # Random seed
BIN=../bin/
DATA=train.trc.tok.gz # wc = 39595781 491195991 3592903739
LIMIT=100000


### 2.2 SRILM options:/matl
LM_NGRAM=4# n-gram order
LM_VOCAB=230 # words seen less than this in GETTRAIN will be replaced with <unk>
LM_MTYPE=i686-m64 # architecture for compiling srilm

train.vocab-all.gz: ${DATA}
	zcat $< | head -n -${LIMIT} | awk 'length($$0) < 1001' | \
	ngram-count -write-order 1 -text - -write - | gzip > $@

train.vocab.gz: train.vocab-all.gz
	zcat $< | awk '{if ($$2 >= ${LM_VOCAB}) print $$1}' | gzip > $@
	zcat $@ | wc -l

train.vocab-no-punct.gz: train.vocab-all.gz
	zcat $< | awk '{if ($$2 >= ${LM_VOCAB}) print $$1}' | \
	tr -cd 'a-zA-ZöüşİıŞÇÜĞÖğç0-9#/\\\n' |\
	tr '[:upper:]' '[:lower:]' | sort | uniq | gzip > $@
	zcat $@ | wc -l

train.lm.gz: ${DATA} train.vocab.gz # wc=128821128 570627415 4735429610
	zcat $< | head -n -${LIMIT} | awk 'length($$0) < 1001' | \
	ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab train.vocab.gz -text - -lm $@

train.lm-no-punct.gz: ${DATA} train.vocab-no-punct.gz
	zcat $< | awk 'length($$0) < 1001' | \
	ngram-count -order ${LM_NGRAM} -kndiscount -interpolate -unk -vocab train.vocab-no-punct.gz -text - -lm $@

%.ppl.gz:
	#test.ppl.gz trial.ppl.gz
	zcat $*.tok.gz | ngram -order ${LM_NGRAM} \
	-unk -lm ukwac.lm.gz -ppl - -debug 2 | gzip > $@

tweets.shuffle: tweets.txt data-sampler.py
	./data-sampler.py $< ${SEED}

divide-data: tweets-shuffle.txt
	head -1000 $< | head -600 | cut -f1 -d ' '  > training.ids.txt
	head -1000 $< | head -600 | cut -f2- -d ' ' > training.tweets.txt
	head -1000 $< | tail -400 | cut -f1 -d ' '  > test.ids.txt
	head -1000 $< | tail -400 | cut -f2- -d ' ' > test.tweets.txt
	

# Greek Hyperspace Analogue to Language (HAL)

Hyperspace Analogue to Language (HAL space) data for various Greek
texts.

## What is a HAL space?

A HAL space is a high-dimensional vector representation of
co-occurrence of words in some text corpus.

## Why can HAL spaces be interesting?

The basic premise of HAL is that words which have similar meaning tend
to occur together.  A HAL space is a quantification of that idea.

A HAL space constructed over some corpus can help identify words that
occur together often.

## What does this repo contain?

This repo contains some HAL spaces constructed over the Nestle 1904
Greek New Testament.

It also contains the data and code to produce and massage the data.

In particular, two kinds of HAL spaces are provided:

- A HAL space containing all of the words (based on Strong's numbers)
  in the Nestle 1904 text.

- A HAL space containing all words not found in the
  input_data/stopwords.strongs.txt file.  That is, the stop words are
  stripped out of the text before constructing the HAL space, and so
  do not contribute to the HAL space counts or distances at all.

## What software actually produces the HAL spaces?

The implementation of the HAL method used is implemented in the
"Emdros" package:

http://emdros.org/download.html


# Data and formats

## Where is the output data?

In Nestle-1904-HAL/output_data/ ... there are two files in there:

- nestle1904.strongs.HAL.txt
- nestle1904.nostopwords.HAL.txt

The former contains the HAL space constructed over the full text,
including stopwords.

The latter contains the HAL space constructed over the reduced text,
excluding the stopwords in
Nestle-1904-HAL/input_data/stopwords.strongs.txt.


## What is the format of the *.HAL.txt files?

Basically, each line is a tab-delimited record with three columns:

- Head word (Strong's number)
- Related word (Strong's number)
- Relation score (an integer)

The higher the Relation score (column 3), the more closely the Related
word (column 2) is collocated with the Head word (column 1).

Notice that the same Head word (column 1) will most likely have more
than one related word (column 2), so the primary key (in relational
database parlance) is a combination of columns 1 and 2.


# Going further

## Where can I learn more about HAL?

Here is a good place to start:

http://www.semantikoz.com/blog/hyperspace-analogue-to-language-hal-introduction/

The original paper is here:

http://link.springer.com/article/10.3758%2FBF03204766

The citation for the article is:

Lund, Kevin and Burgess, Curt (1996): "Producing high-dimensional
semantic spaces from lexical co-occurrence", Behavior Research
Methods, Instruments, & Computers, Vol. 28 Number 2, pp. 203-208.



# Whodunnit?

Dr. Ulrik Sandborg-Petersen of Scripture Systems ApS, Denmark, and Aalborg University, Denmark.
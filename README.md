ghalib-concordance
==================

##Ghalib Concordance Project

The original data from this project comes from (our)
Professor Emerita Frances Pritchett’s carefully transcribed work:
http://www.columbia.edu/itc/mealac/pritchett/00ghalib.

This is a work in progress in very early stages. If you are interested in
helping out, please be in touch. There is a substantial amount of proof
reading and “data munging” that has to happen, so we
need many eyes and ears.

We also want this to be an entirely open digital humanities project, so all data
and source code will be available at all stages of production. The code/data is
licensed under an MIT license. There has not yet been an official release.

Much like programming scientists, we are both programming humanists and not
professional coders, so suggestions for best practices are always welcome (e.g.
‘use collections’).

##Overview of Code

The main program here is in the iPython Notebook `generate_urdu.ipynb`. It reads the text from `input/verses.csv`.  creates Urdu-(....-ur.html) and devanagari-script (....-hi.html) statistics file output based on earlier transliteration-only versions in `output/statistics`. (Devanagari is still rather messy)
* izafat-freq.csv ––> izafat-freq-ur.csv

##Description of Files
* `README.md`:  this file
* `bin`:  binary files directory
  * `fw xxx`: finds word xxx in text
  * `load_notebooks`: loads the ipython notebooks with --script parameter to generate .py files
  * `og #`: opens ghazal # on the web
* `generate_urdu.ipynb`:  creates Urdu- and devanagari-script statistics output based on earlier transliteration-only versions in `output/statistics`.
* `generator.ipynb`: x
* `generator.py`: x
* `/graphparser`: submodule of [graphparser](https://github.com/seanpue/graphparser)
* `/input`: input file directory
  * `README.md`: some notes on input
  * `okay.csv`: okay (as x), token, lemma
  * `verses-orig.csv`: original input file
  * `verses.csv`: verses file in use (###.##.#), transliterate verse,meter
* `license.txt`: license
* `/old_code`: old code not in use now
* `/output`: output directory (all are generated)
  * `conc_details.csv`: lemma (transliteration),words from lemma (in transliteration)
  * `hiur-lemmas-by-size-ul.html`: HTML of transliteration, urdu, devanagari, hyperlinks (sorted by instances of lemma)
  * `hiur-lemmas.html`:  HTML of transliteration, urdu, devanagari, hyperlinks (sorted by instances of transliteration)
  * `izafats.csv`: izafats,count
  * `izafatsastokens.csv`: token (izafats are token), count
  * `lemmas-by-size.txt`: lemmas (sorted by instances), tokens (with count)
* `/statistics`: directory of various statistical details
  * `izafat-freq-ur.csv`: just izafats with Urdu
  * `izafat-freq.csv`: izafats in transliteration
  * `izafatastoken-freq.csv`: tokens where izafat phrases are considered tokens
  * `izafatastokens-freq-hiur.csv` : tokens with Urdu, messy nagari where izafat phrases are considered tokens
  * `izafatastoken-freq-ur.csv`   : tokens where izafat phrases are considered tokens with Urdu
  * `lemmas-beta-freq-ur.csv`: just lemmas with Urdu (very beta)
  * `lemmas-beta-freq.csv`: just lemmas (very beta)
  * `uniquetokens-freq-ur.csv`: unique tokens with urdu
  * `uniquetokens-freq.csv`: unique tokens in transliteration
* `tocheck.csv`: transliterations to check

texts

Project Managers
================

A. Sean Pue (@seanpue)

Taimoor Shahid (@MohJeMa)

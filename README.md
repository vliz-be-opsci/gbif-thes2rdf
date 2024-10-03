# Intro

This little project provides an automated strategy to build RDF serialisations for the various thesaurus-xml files provided at [https://rs.gbif.org/vocabulary/](https://rs.gbif.org/vocabulary/)

These gbif-vocabularies introduce decent and stable URI for curated terms lists in use in the domain. 
Currently these are made available only in a gbif-specific [thesaurus-xml-format](http://rs.gbif.org/schema/thesaurus.xsd")


# Scope
To provide a - make a script that converts thesaurus xml into ttl and jsonld representations


# Usage

Python-Dependency management for this depends on [python-poetry](https://python-poetry.org/docs/)

Have some local `./data` folder around that has the thesaurus-xml-files to be converted. (These can be nested in subdirs: `**/*.xml`)

Then simply run

```sh
$ poetry install          # only once to install python package dependencies locally ina virtual environment
$ poetry shell            # to activate the virtual environment where said dependencies are available
$ ./bin/gbif_thes2rdf.py  # to actually run the conversion -- can be ran multiple times, will overwrite ttl and jsonld 
```

The resulting `**/*.ttl` (text/turlte) and `** /*.jsonld` (application/ld+json) files will be placed next to their xml source.


# Ref
- see [some selection](urls.txt) of thesauri to consider.
- a local `./bin/get_thes_from_urls.sh` script will download them to a local `./data` folder


# TODO

Have dialogue with gbif people and/or site admins on 
1. how to integrate this in the rs.gbif.org workflow for these vocabs (they appear to be managed in [this github repo](https://github.com/gbif/rs.gbif.org/ )) and 
2. how to publish them over there via Content Negotiation


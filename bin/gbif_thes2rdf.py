#! /usr/bin/env python

from sema.subyt import Subyt
from dotenv import load_dotenv
import os
from pathlib import Path
from logging import getLogger
from xmlasdict import parse
from rdflib import Graph

log = getLogger(__name__)


def config():
    load_dotenv()
    my_dir = Path(__file__).parent.absolute()
    data_dir = Path(os.getenv("DATA_DIR", my_dir / "../data")).resolve().absolute()
    fname_pattern = os.getenv("FNAME_PATTERN", "**/*.xml")
    template_dir = Path(os.getenv("TEMPLATE_DIR", my_dir / "../template")).resolve().absolute()
    template_name = os.getenv("TEMPLATE_NAME", "thes2skos.ttl")
    return (data_dir, fname_pattern, template_dir, template_name)


def convert_files(data_dir, fname_pattern, template_dir, template_name):
    assert data_dir.is_dir(), f"{data_dir} does not exist or is no folder"

    files = data_dir.glob(fname_pattern)
    processed = list()

    for inf in files:
        ouf = inf.with_suffix(".ttl")
        # parse the xml ourselves to get the root info (as subyt does an unpack on the xml)
        thesaurus = parse(inf)
        vars = {
            k: thesaurus['@{http://purl.org/dc/terms/}' + k]
            for k in ('URI', 'title', 'description', 'issued')
        }

        subyt = Subyt(
            template_folder=template_dir,
            template_name=template_name,
            source=str(inf),
            extra_sources=dict(thesaurus=str(inf)),
            sink=str(ouf),
            mode="no-it",
            variables=vars,
        )
        res = subyt.process()
        if res:
            # convert to jsonld
            jsf = ouf.with_suffix(".jsonld")
            g = Graph().parse(ouf, format="turtle")
            g.serialize(destination=jsf, format="json-ld")
            processed.append(dict(input_xml=inf, out_turtle=ouf, out_json_ld=jsf))

    print(f"done working on {len(processed)} files in folder {data_dir} matching {fname_pattern}")

    
def main():
    convert_files(*config())


if __name__ == "__main__":
    main()

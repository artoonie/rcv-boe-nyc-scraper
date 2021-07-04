# NYC Board of Elections Ranked Choice VOting Data
Scrapers for the BOE website to get the RCV data in a reasonable format. See the parsed data in `outdir`.

# Data format
The data is converted to the Universal Tabulator format and validated with the python library [RCVformats](https://rcvformats.readthedocs.io/en/latest/).

The latest data is placed in `outdir`. We will update the data in this repository as newer data is released, or you can clear the cache and re-run the code yourself.

# A note on code quality
THIS IS BAD CODE

It is not meant for you to enjoy. It is meant for me to quickly hack something together and midnight, throw away the code, and never look at it again.

The data is placed in `outdir` for your convenience, so you may enjoy downloading the data and never looking at the code.

# Uploading data to RCVis
There is a script to upload data to [RCVis](https://rcvis.com). Please don't run it. I have already uploaded all the data, and the links are available on this Google Spreadsheet: https://twitter.com/rcvisdotcom/status/1411188410900004866?s=20

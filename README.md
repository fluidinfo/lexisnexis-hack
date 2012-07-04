Contains a single Python script that was used on 2012-07-03 to put lexisnexis.com metadata onto various objects in Fluidinfo.

What it does
------------

The `dataset` variable in `lexisnexis.py` holds a list of dicts. Each dict contains `about` and `data`:

  `about`: a list of about values for Fluidinfo objects.
  `data`: a string (a JSON dump of a dict) to be put onto each of the about values

Once the data is on all the about values, anyone using the latest version
of the Fluidinfo Chrome extension will see the `data` pop up (formatted
into a list of LexisNexis links) if they visit any of the `about` values or
select text containing one of the about value. So the about lists each
contain a phrase (e.g., `audit`) and a set of URLs. This gives the two ways
to trigger the display of the relevant LexisNexis links. To see the
information pop up, you'll need to be following lexisnexis.com on
Fluidinfo.com (i.e., have a username/follows tag on the Fluidinfo object
whose about value is lexisnexis.com).

Running
-------

In a virtualenv:

    $ pip install -r requirements.txt
    $ export FLUIDINFO_LEXISNEXIS_PASSWORD=<password>  # ask Terry for this.
    $ python lexisnexis.py

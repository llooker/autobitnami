## What this is

This is a small script to download the latest Bitnami LAMP stack installer to make upgrading PHP easier.

## Why does this exist

It's a stop-gap until we can either get rid of having to use Bitnami or we start deploying Bitnami images in easier-to-upgrade containers instead of an install on a bare EC2 instance.

## How do I use it

1. Clone this repository.
2. Install requirements: `pip install -r requirements.txt`
3. When you need a new installer, run `php72.py`. This will automatically fetch the latest and greatest PHP 7.2.x from Bitnami's website.

## Improvements that could be made

Different scripts or arguments to let you select the minor version oh PHP (in case you are on 7.1 or 7.3 instead).

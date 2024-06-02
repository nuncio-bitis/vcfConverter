# vcfConverter

Convert a VCF (vCard) address book file to either JSON or CSV.

[VCF Converter on GitHub](https://github.com/nuncio-bitis/vcfConverter)

## Usage

```bash
python3 vcfConvert.py <vcf_file> [options]
```

By default this prints a json object to stdout if no options are specified.

### Options

`-json <json file>` : export to json file, must specify file name

`-csv <csv file>` : export to csv file, must specify file name

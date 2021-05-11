
# RDAP and Geo IP Look Up

### Running the CLI
In order to use the CLI, you have to pip install requirements in the project source directory.

```sh
pip install -r requirements.txt
```

The CLI receives a path to a txt file as a positional parameter. There are two optional flags in case you want to return only RDAP `--rdap` or only Geo IP results `--geo`.

##### Examples
```sh
python main.py list_of_ips.txt --rdap # only rdap
python main.py list_of_ips.txt --geo # only geo ip
python main.py list_of_ips.txt # all results

The look up may take a while, since it hits an external API in order to fetch data.

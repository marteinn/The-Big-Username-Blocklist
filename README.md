# The-Big-Username-Blacklist
This is a opinionated blacklist of words that you might not like to see used as usernames in your service.

The editable blacklist can be found in [list_raw.txt](list_raw.txt) and is categorized into six sections:

- **Privileges** User privilege terms to prevent faked authority. Example: _root_, _super_
- **Code**: Programming terms that you might want to avoid in a url. Example: _void_, _null_
- **Terms**: Various technical terms. Example: _request_, _system_
- **Financial**: This is for the spammers/scammers. Example: _payment_, _invoice_
- **Sections**: Common website pages and sections. Example: _faq_, _help_
- **Actions**: User actions. Example: _delete_, _create_

Please note that this list does not contain any curse words, there are [other lists](https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) for that.


## How it works
This repro contains standard data files, just pick the format of your choosing.

- newline: [list.txt](list.txt)
- json: [list.json](list.json)
- python: [list.py](list.py)


## Packages

The blacklist has both a [python](https://github.com/marteinn/the-big-username-blacklist-python) and [node](https://github.com/marteinn/the-big-username-blacklist-js) library available.


## Contributing

Want to contribute? Awesome.

- First edit `list_row.txt`
- When you are done, run `python scripts/generate.py`.
- ... This script will update `list.txt`, `list.json` and `list.py`
- Done? Send a pull request.


## License

The-Big-Username-Blacklist is released under the [MIT License](http://www.opensource.org/licenses/MIT).

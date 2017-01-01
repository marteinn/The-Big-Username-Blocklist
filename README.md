# The-Big-Username-Blacklist
This is a opinionated blacklist of words that you might not like to see used as usernames in your service (think **username**.domain.com, domain.com/**username** or **username**@domain.com).

The editable blacklist can be found in [list_raw.txt](list_raw.txt) and is categorized into six sections:

- **Privileges** User privilege terms to prevent faked authority. Example: _root_, _super_
- **Code**: Programming terms that you might want to avoid in a url. Example: _void_, _null_
- **Terms**: Various technical terms. Example: _request_, _system_
- **Financial**: This is for the spammers/scammers. Example: _payment_, _invoice_
- **Sections**: Common website pages and sections. Example: _faq_, _help_
- **Actions**: User actions. Example: _delete_, _create_

You can try the blacklist using the tool [Username checker](http://marteinn.github.io/The-Big-Username-Blacklist-JS/).

Please note that this list does not contain any curse words, there are [other lists](https://github.com/shutterstock/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words) for that.


## How it works

This repro contains standard data files, just pick the format of your choosing.

- newline: [list.txt](list.txt)
- json: [list.json](list.json)
- python: [list.py](list.py)
- javascript (es6): [list.js](list.js)
- javascript (commonjs): [list-commonjs.js](list-commonjs.js)
- php: [list.php](list.php)


## Packages

The blacklist has both a [python](https://github.com/marteinn/the-big-username-blacklist-python) and [node](https://github.com/marteinn/the-big-username-blacklist-js) library available.


## Contributing

Want to contribute? Awesome.

- First edit `list_row.txt`
- When you are done, run `python scripts/generate.py`.
- ... This script will update the various list files.
- Done? Send a pull request.


### Release start

These hooks will automatically bump the application version when using `git flow release ...`

```bash
chmod +x $PWD/git-hooks/bump-version.sh
ln -nfs $PWD/git-hooks/bump-version.sh .git/hooks/post-flow-release-start
ln -nfs $PWD/git-hooks/bump-version.sh .git/hooks/post-flow-hotfix-start
```


## License

The-Big-Username-Blacklist is released under the [MIT License](http://www.opensource.org/licenses/MIT).

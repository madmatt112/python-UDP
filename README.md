# Project Name

_The project that can be named is not the pythonic project_

## Installation

`git clone https://github.com/madmatt112/python-UDP.git`

## Usage

1. Invoke `receiveudp.py` and send it to the background (`./receiveudp.py &`)
2. Invoke `sendudp.py` with any number of arguments, *being careful of shell intepretation/expansion*: `./sendudp.py Hi Mom!` or `./sendudp.py "Emoticons rule! ;)"`
3. Watch your UDP message appear before your very eyes:

  sendudp.py output:
```
UDP target IP: 127.0.0.1
UDP target port: 5005
message: Hi Mom!
```
  receiveudp.py output:
```
received message:  Hi Mom!
```
## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## License and Author

Absolutely no rights reserved, although a mention of my authorship would be appreciated.
Author: Matthew Field

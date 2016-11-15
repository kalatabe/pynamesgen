# Name Generator

Python 3 implementation of docker's "nonsensical names" generator.
Can be used standalone or imported as a module and used in other projects.

## Standalone usage
`./names_generator $NUM` where `$NUM` is an optional number of names you want to get.
If not provided or equal to 1, a single name will be echoed to the shell.

With `$NUM` > 1, a JSON list containing that many random names will be printed, for example:

`["desperate_goldberg", "cranky_golick", "ecstatic_shirley"]`

## Module usage
Import the module and call `names_generator.get()`

## Parameters for `get()`
- `unique` - if `True`, guarantees that every word in every name will only appear once. If one of the lists is exhausted, will print a warning to STDOUT and return all names generated up to that point.

  Default: `False`

- `number` - number of names to generate. Will return a simple string if `number == 1` or a JSON list if `number > 1`

  Default: `1`

- `separator` - what symbol to separate the left and right side of the name with.

  Default:`_` (underscore)

## Credits

[Docker](https://github.com/docker/docker) for the original implementation

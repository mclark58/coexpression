# CoExpression
---

This is the basic readme for this module. 
This module contains coex_filter and coex_cluster methods.

Build status:</br>
master:  [![Build Status](https://travis-ci.org/arfathpasha/coexpression.svg?branch=master)](https://travis-ci.org/arfathpasha/coexpression)</br>
staging: [![Build Status](https://travis-ci.org/arfathpasha/coexpression.svg?branch=staging)](https://travis-ci.org/arfathpasha/coexpression)</br>
develop: [![Build Status](https://travis-ci.org/arfathpasha/coexpression.svg?branch=develop)](https://travis-ci.org/arfathpasha/coexpression)</br>

Code coverage: (master branch)
[![Coverage Status](https://coveralls.io/repos/github/arfathpasha/coexpression/badge.svg?branch=master)](https://coveralls.io/github/arfathpasha/coexpression?branch=master)</br>

Notes:</br>
The module expects to utilize a workspace with name args['workspace_name']+user_id for its input and output operations, where args contains the input object meta data parameters. This is to ensure that all data is read and written from a workspace that is local to the user of the module.

TODO: It is anticipated that in the future, `ltest/script_test/*_input.json` files will be converted to template files in order to make the workspace name along with its user_id suffix more explicit. 

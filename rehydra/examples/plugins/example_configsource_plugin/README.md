# Rehydra example config source
Use this as the template a Rehydra config source plugin

Config source plugins are allowing Rehydra to recognize other search path schemas in addition to the built in 
`file://` (which provides access to configs in the file system) and 
`pkg://` (which provides access to configs installed with a Python package) 

This config source hard codes all the responses so it's not very useful.
Please base your tests on the data in  rehydra_root/tests/test_apps/config_source_test/dir.

All config sources need to pass the ConfigSourceTestSuite tests, which are expecting those specific responses.
When implementing a new config source, be sure to run it through the test suite to ensure it always behaves the same
as the other config sources.

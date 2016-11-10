#knowstests
knowstests initializes a pydevd remote debugging session when invoked - all other debugging related features and options come directly from [nose](https://nose.readthedocs.io/en/latest/index.html)

In order to configure your remote debugging session to connect to your debugging server, ensure that the following environment variables are set:

DDBUG - set to to 1 to enable the pydevd connection from the remote; without this option set, knowstests behaves the same as nosetests

DDBUG_HOST - the host address of the pydevd server

DDBUG_PORT - the port number of the pydevd service on the debugging server; defaults to 51500

knowstests can be invoked from the command line in the same manner as nosetests.

You can also start testing by invoking run or main, or by instantiating TestProgram.

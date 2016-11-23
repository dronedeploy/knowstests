#!/usr/bin/env python

import os
import re
import sys

import nose


class TestProgram(nose.core.TestProgram):
    """TestProgram class that initiates a pydevd connection.

    See nose.core.TestProgram for more information.
    """
    def __init__(self, *args, **kwargs):
        connect_debugger()
        super(TestProgram, self).__init__(*args, **kwargs)


connected = False
def connect_debugger():
    global connected
    server_ip = os.environ.get('DDBUG_HOST')
    ddbug = os.environ.get('DDBUG')
    if not connected and server_ip and ddbug:
        # TODO: move more of these parameters into DDBUG environment variables
        import pydevd
        pydevd.settrace(os.environ['DDBUG_HOST'], port=int(os.environ.get('DDBUG_PORT') or 51500),
                        stdoutToServer=True, stderrToServer=True, suspend=False,
                        trace_only_current_thread=False, patch_multiprocessing=True)
        connected = True


# maintain backwards compatibility with nosetests
run_exit = main = TestProgram

# following code excerpted from nose

def run(*args, **kwargs):
    """Collect and run tests, returning success or failure.

    The arguments to `run()` are the same as to `main()`:

    * module: All tests are in this module (default: None)
    * defaultTest: Tests to load (default: '.')
    * argv: Command line arguments (default: None; sys.argv is read)
    * testRunner: Test runner instance (default: None)
    * testLoader: Test loader instance (default: None)
    * env: Environment; ignored if config is provided (default: None;
      os.environ is read)
    * config: :class:`nose.config.Config` instance (default: None)
    * suite: Suite or list of tests to run (default: None). Passing a
      suite or lists of tests will bypass all test discovery and
      loading. *ALSO NOTE* that if you pass a unittest.TestSuite
      instance as the suite, context fixtures at the class, module and
      package level will not be used, and many plugin hooks will not
      be called. If you want normal nose behavior, either pass a list
      of tests, or a fully-configured :class:`nose.suite.ContextSuite`.
    * plugins: List of plugins to use; ignored if config is provided
      (default: load plugins with DefaultPluginManager)
    * addplugins: List of **extra** plugins to use. Pass a list of plugin
      instances in this argument to make custom plugins available while
      still using the DefaultPluginManager.

    With the exception that the ``exit`` argument is always set
    to False.
    """
    kwargs['exit'] = False
    return TestProgram(*args, **kwargs).success


if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    sys.exit(main())

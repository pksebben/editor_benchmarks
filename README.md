# Editor Benchmarks

These projects don't work.  On purpose.

Editor Benchmarks are a series of projects meant to benchmark your
editor's linting and code-analysis capabilities.  You load one up, and
make sure it's throwing all the appropriate error classes so you know
your editor is going to catch you when you mess up.

Because some languages require a whole language server to really test,
each one is it's own project with it's own set of venvs, env vars, and
other ancillary kit.  We want to check all the possible vectors that
an editor _can_ catch.

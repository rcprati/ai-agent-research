# Before accepting the agent's result

1. **Does it reproduce something I already know?** Run the same method on a case with a known answer
   (published value, analytical case, data from a previous experiment).
2. **Is the number plausible?** Order of magnitude, sign, units. Compare with what you expected.
3. **Did it use all the data?** Ask: "how many rows/files did you read, and which did you discard? Why?"
4. **Did it really run?** Ask for the command that was run and the actual output. "It should work" is not evidence.
5. **Did it do something I did not ask for?** Look at the list of changed files. Changes outside the
   scope are a warning sign.
6. **Did I check a sample by hand?** Redo one or two calculations or data points independently.
7. **Did I ask for a second opinion?** Another session (or another tool) reviewing the result
   without seeing the first one's reasoning.

**Golden rule:** "the agent said it is done" is not a verification.

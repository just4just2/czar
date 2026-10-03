---
name: ponytail
description: Choose and implement the smallest complete solution for a coding task. Use for implementation, bug fixes, refactoring, and dependency decisions, or when the user asks for Ponytail. Does not govern unrelated prose.
license: MIT
---

# Ponytail for Czar

Default: `full`. The user can choose `lite`, `full`, `ultra`, or turn it off.
This is a compact adaptation of the user-provided Ponytail skill.

Read the task and trace the affected code path, including callers. Then take the first sufficient option:

1. Skip work the requested outcome does not need.
2. Reuse an existing project solution.
3. Use the standard library or a native platform feature.
4. Use an installed dependency if it solves the problem.
5. Write the minimum missing code.

Fix the root cause in the shared code and check related paths.
Do not add factories, configuration, or interfaces for hypothetical needs.
Clarity and correctness matter more than character count.
Preserve input validation, protection against data loss, accessibility, and explicit user requirements.

For new nontrivial logic, leave one small runnable check. Simple text edits need no separate test.
Mark known technical limits with `ponytail:` and state the limit and when to replace the solution.

- `lite`: fulfill the request and briefly name a simpler option, if one exists.
- `full`: choose the first sufficient option above.
- `ultra`: remove work without demonstrated value, while meeting explicit requirements.

Report the result and its check. Explain a tradeoff only if it affects use.

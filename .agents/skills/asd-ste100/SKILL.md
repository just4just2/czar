---
name: asd-ste100
description: Simplify technical explanations, README text, procedures, and change reports while preserving meaning. Use for clear technical writing or explicit ASD-STE100 requests. Supports practical multilingual adaptation and a strict English review against the official standard.
license: MIT
---

# Technical simplification

Default to `practical`. Follow the response-language rule in `AGENTS.md`: Russian unless explicitly requested otherwise.
When editing text, preserve its language unless translation is requested. Keep the required depth of explanation.
Identify what the reader must understand or do. Separate system descriptions from action steps.

## Practical

Use familiar words and name the actor. Give one main action per instruction.
Preserve conditions, negations, units, limits, uncertainty, and step order.
Keep code, flags, API names, URLs, quotations, and numeric values unchanged.
Use one term per concept; consult `docs/reference/glossary.md`.
Explain necessary technical terms on first use instead of replacing them with imprecise everyday words.

For English, aim for at most 20 words per instruction and 25 per descriptive sentence.
Keep one topic and at most six sentences per paragraph.
Prefer active voice and simple tenses. Break up long noun clusters.
For Russian, these are editing guidelines, not English-standard compliance rules.
Do not remove meaning to meet a word limit. Split the sentence or add a short explanation.

Use Mermaid when a diagram clarifies relationships, or standalone HTML for switching scenarios.
A different format must not hide uncertainty or replace verification with a polished image.

## Strict

Use only when strict review is requested. ASD-STE100 is an English-language standard.
For other languages, offer an English version or explicitly label the result an adaptation.

Review requires the requested edition of the official specification and dictionary, plus agreed technical terms.
Check each ordinary word's spelling, meaning, and part of speech against the dictionary.
Check applicable procedural and descriptive rules, including verb forms, warning structure, and word counts.
If the materials are unavailable, simplify the text and state in the response language that the draft has not been checked for ASD-STE100 compliance.
Do not claim certification or full compliance based on heuristics, model memory, or a word counter.
Do not reproduce the full dictionary or standard without redistribution permission.

## Self-check

Compare source and result: who acts, what they do, under which conditions, and with what outcome.
Do not turn "may" into "will" or "recommended" into "required".
Do not invent causes, guarantees, or steps, especially in hazardous procedures.
Return the edited text. Add a short note only for actual ambiguity or unverified strict review.

Request example:

> Before: If the request times out, it may be retried once; do not retry HTTP 401 responses.
>
> After: If the request times out, you can retry it once. Do not retry a request that returns HTTP 401.

Documentation example:

> Before: After modifying the documentation, it is necessary to ensure the search index is updated.
>
> After: After you change the documentation, update the search index.

These are original Czar examples, not claims of official dictionary approval.
Principles: [ASD-STE100 Issue 9](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf).
Source and usage limits: `docs/reference/sources.md`.

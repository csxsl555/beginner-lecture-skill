# Repository conventions

This repository contains the `beginner-lecture` skill for writing clear, complete learning materials for beginners. The teaching instructions and examples are primarily in Chinese.

## Structure

- `SKILL.md`: skill discovery metadata, teaching workflow, terminology rules, and acceptance criteria.
- `agents/openai.yaml`: display name and short description; keep normal automatic discovery enabled.
- `references/`: teaching patterns and behavioral evaluation requests loaded when needed.
- `examples/`: self-contained demonstration lessons using fictional or explicitly supplied examples.
- `tests/verify_examples.py`: portable standard-library checks for example code, arithmetic, and local links.
- `README.md`: purpose, installation, usage, examples, validation, and limitations.
- `LICENSE`: the repository's MIT license.

Document new file categories here before adding them. Use UTF-8 text, lowercase hyphenated resource names, and relative links inside the repository. Keep temporary outputs outside the repository; do not automatically delete existing files.

## Teaching invariants

- Explain each newly introduced technical term immediately at its first appearance in a learning unit, including Chinese terms, foreign-language terms, abbreviations, mathematical symbols, and code identifiers.
- Explanations must not rely on unexplained terminology. A glossary cannot replace a definition beside the first occurrence.
- Check completeness against an explicit scope or source material. Mentioning a concept does not establish that it has been explained.
- Preserve intermediate reasoning, necessary assumptions, important limitations, and the user's requested scope.
- Do not turn one example into a mandatory structure or length for every subject.

## Validation

Run from the repository root:

```sh
python tests/verify_examples.py
```

If the host provides the `skill-creator` validator, also run its `scripts/quick_validate.py` against this repository. Read `references/evaluation-cases.md` when changing teaching behavior and review a relevant generated lesson for terminology, reasoning, and scope. Report author review separately from independent or learner evaluation.

The automated checks validate examples and links; they do not prove teaching effectiveness or factual correctness across arbitrary future subjects.

## Scope of repository operations

Do not add credentials, local user paths, private source material, environment files, or unrelated personal records. Preserve existing user edits. Publishing changes, deleting files, changing credentials, adding CI configuration, or modifying global settings requires the user's authorization for that operation. Do not add automatic publishing behavior to the skill.

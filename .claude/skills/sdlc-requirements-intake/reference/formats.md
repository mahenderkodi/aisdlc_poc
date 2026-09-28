# Source formats — how to read each one

| Source | Read this | Also look at | Cite as |
|---|---|---|---|
| .txt .md .json .yaml .sql OpenAPI | the file itself | — | `S1 L7` |
| .docx | converted/<name>/<name>.md | converted PDF for diagrams, tables, footnotes | `S2 p.4` |
| .pptx | converted/<deck>/slides.md | deck.pdf for any slide marked ⚠ or low confidence | `S3 slide 7` |
| .xlsx | converted/<name>/<sheet>.csv | screenshot if colour carries meaning | `S4 sheet Rules row 12` |
| .pdf | converted text + the PDF pages | page images for tables and diagrams | `S5 p.18` |
| image | the image + <name>.caption.md | — | `S6 image` |
| schema.sql | the DDL + schema-notes.md | — | `S7 table leave_request` |

## Slide decks
If slides.md does not exist, create it first — one section per slide:
Text on slide (exact) · Speaker notes (exact) · Visual content (described from the PDF page) · Interpretation (every guess marked ⚠) · Confidence (high/medium/low).
Work in batches of about 10 slides. Coverage = one ledger row per slide.

## Spreadsheets
Each row of a rules or field-list sheet is one line for coverage. Colour or merged-cell meaning not written in the cells → OQ.

## SQL
Foreign keys give relations. Relations without an FK, status values and ownership come only from schema-notes.md; if they are missing there → OQ "suspected relation — confirm".

## Large documents (over 20 pages)
One chunk (chapter) per run, fresh session per chunk. After all chunks: a merge pass for duplicates and contradictions, then the coverage summary per chunk.
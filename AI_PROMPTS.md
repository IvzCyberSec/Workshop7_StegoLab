# AI Prompts – learn steganography with an AI tutor

Use these with ChatGPT, Claude or Gemini. They make the AI **explain** instead of doing the work for you.

**Never paste** private photos, passwords or anything personal into an AI tool.

## Reusable instruction (paste this first)

```text
Act as a patient tutor. I am a first-year cybersecurity student learning Python and digital
forensics in a workshop. I am building a steganography tool called StegoLab.

Do not write whole functions for me. For each question:
- Explain the concept in plain English first, with a small example.
- Give me hints or pseudocode, not the finished code.
- Tell me how I can test that my code works.
If I paste code, explain what it does line by line before suggesting changes.
```

## Understanding the concepts

```text
Explain what the "least significant bit" of a number is, using the number 200 as an example.
Show it in binary, then show what happens when I change the last bit.
```

```text
Explain what the bitwise operators >>, <<, & and | do in Python, with one small
example each that relates to working with single bits.
```

```text
Explain the structure of a PNG file: the signature, chunks and the IEND chunk.
Why would data written after IEND not show up in an image viewer?
```

## While coding

```text
Here is my bytes_to_bits function and the test that fails. Do not fix it for me.
Trace the letter "A" through my code step by step and tell me where my result
differs from the expected [0, 1, 0, 0, 0, 0, 0, 1].
[PASTE CODE AND ERROR]
```

```text
I get this error when running my code. Explain what the error means and give me
two things to check. Do not rewrite my code.
[PASTE ERROR]
```

## Forensics thinking

```text
My forensic tool found a metadata field containing a string ending in "==".
What encodings commonly look like this, and how could I check safely?
```

```text
Why can a statistical check on least significant bits produce false positives
on normal photos? Give one example of a clean image that might look suspicious.
```

## Before you commit (the understanding check)

```text
Ask me 5 questions to check that I really understand how my StegoLab tool hides
and detects data. Wait for my answer to each one before giving feedback.
```

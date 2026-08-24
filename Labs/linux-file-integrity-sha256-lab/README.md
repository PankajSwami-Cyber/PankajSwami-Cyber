# Linux File Integrity Verification Using SHA-256

## Overview

This lab demonstrates how to use Linux command-line tools to calculate and compare **SHA-256 hash values** for two text files.

The objective was to determine whether the two files were identical or different by comparing their cryptographic hash values.

## Objectives

* List the contents of the working directory
* View the contents of two text files
* Calculate SHA-256 hashes using `sha256sum`
* Save the generated hashes to separate files
* Compare the hash values using `cmp`
* Determine whether the two files are identical or different
* Understand how cryptographic hashing can be used for file integrity verification

## Environment

* **Operating System:** Linux
* **Shell:** Bash
* **Hash Algorithm:** SHA-256

## Commands Used

```bash
ls
cat file2.txt
cat file1.txt
sha256sum file1.txt
sha256sum file2.txt
sha256sum file1.txt >> file1hash
sha256sum file2.txt >> file2hash
cat file1hash
cat file2hash
cmp file1hash file2hash
```

## Lab Procedure

### 1. List the files

```bash
ls
```

The command displayed the files available in the working directory:

```text
file1.txt
file2.txt
```

### 2. View the file contents

```bash
cat file2.txt
cat file1.txt
```

The contents of both files were inspected before calculating their hashes.

### 3. Calculate the SHA-256 hash of `file1.txt`

```bash
sha256sum file1.txt
```

Result:

```text
131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267  file1.txt
```

### 4. Calculate the SHA-256 hash of `file2.txt`

```bash
sha256sum file2.txt
```

Result:

```text
2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b  file2.txt
```

### 5. Save the hash results

The hash values were redirected into separate files:

```bash
sha256sum file1.txt >> file1hash
sha256sum file2.txt >> file2hash
```

The `>>` operator appends the command output to the specified file.

### 6. Display the saved hash values

```bash
cat file1hash
cat file2hash
```

This confirmed that the SHA-256 values were stored correctly.

### 7. Compare the hash files

```bash
cmp file1hash file2hash
```

The comparison showed that the hash files were different.

Because the SHA-256 values generated for the original files were also different, the two files do not contain identical data.

## Results

| File        | SHA-256 Hash                                                       |
| ----------- | ------------------------------------------------------------------ |
| `file1.txt` | `131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267` |
| `file2.txt` | `2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b` |

### Hash Comparison

```text
file1.txt
131f95c51cc819465fa1797f6ccacf9d494aaaff46fa3eac73ae63ffbdfd8267

file2.txt
2558ba9a4cad1e69804ce03aa2a029526179a91a5e38cb723320e83af9ca017b
```

The SHA-256 hash values are **different**.

## Conclusion

The two files are **different**.

This lab demonstrated how SHA-256 cryptographic hashes can be used to verify file integrity. When the contents of files differ, their SHA-256 hash values will normally differ as well.

The exercise also provided hands-on practice with Linux command-line tools, output redirection, file comparison, and basic cybersecurity investigation techniques.

## Security Concepts Demonstrated

* **File Integrity** — Detecting whether data has changed
* **Cryptographic Hashing** — Generating a unique fixed-length representation of file contents
* **SHA-256** — Using a secure hashing algorithm for integrity verification
* **Linux Command Line** — Performing security-related tasks through Bash
* **File Comparison** — Comparing files and hash outputs
* **Evidence Collection** — Recording and reviewing hash values

## Evidence

A screenshot of the Linux terminal session is included in the `screenshot.png`.

```text
screenshot.png
```

## Key Takeaway

Cryptographic hashing is an important cybersecurity technique for verifying data integrity. A change to a file's contents results in a different hash value, making hash comparison useful for detecting unauthorized or unexpected modifications.

## Skills

`Linux` `Bash` `SHA-256` `Cryptographic Hashing` `File Integrity` `Command Line` `Cybersecurity Fundamentals` `File Comparison`

GitHub - https://github.com/PankajSwami-Cyber/PankajSwami-Cyber

Linkedin - www.linkedin.com/in/pankajswamicyber


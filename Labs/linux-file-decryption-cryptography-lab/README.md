# Linux File Decryption & Cryptography Lab

## Overview

This project documents a cybersecurity lab focused on Linux command-line skills, cryptography, classical cipher decoding, and file decryption.

In this lab, I worked through a scenario where files in a Linux home directory had been encrypted. I used Linux commands to investigate the directory, locate hidden files, decode a Caesar cipher, and decrypt an encrypted file using OpenSSL.

The lab reinforced the importance of encryption for protecting data and helped me practice Linux and cryptography skills relevant to a security analyst.

## Objectives

The main objectives of this lab were to:

* List and explore directory contents using Linux commands
* Read the contents of files
* Identify hidden files
* Decode a Caesar cipher using Linux command-line tools
* Use OpenSSL to decrypt an encrypted file
* Restore the encrypted file to its original state
* Reveal the hidden message contained in the recovered file

## Tools & Technologies

* Linux
* Bash / Linux command line
* `ls`
* `cat`
* `cd`
* `tr`
* OpenSSL
* AES-256-CBC
* PBKDF2
* Caesar cipher

## Lab Scenario

In this scenario, files in my Linux home directory had been encrypted.

My task was to investigate the available files, uncover clues that provided the instructions for decryption, decode the classical cipher, and ultimately recover the encrypted data.

The lab consisted of three main stages:

1. Explore the home directory and read the available instructions.
2. Locate a hidden file and decode the Caesar cipher it contained.
3. Use the recovered instructions to decrypt the encrypted data file and reveal the hidden message.

## Methodology

### 1. Explore the Home Directory

I started by listing the contents of the home directory:

```bash
ls
```

I then read the contents of the README file:

```bash
cat README.txt
```

This provided the initial instructions for the lab.

---

### 2. Locate the Hidden File

I navigated to the `caesar` directory:

```bash
cd caesar
```

I used the `-a` option with `ls` to display hidden files:

```bash
ls -a
```

This revealed the hidden file:

```text
.leftShift3
```

I read the contents of the hidden file:

```bash
cat .leftShift3
```

The contents were encoded using a Caesar cipher.

---

### 3. Decode the Caesar Cipher

I used the Linux `tr` command to reverse the three-character Caesar shift:

```bash
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"
```

This converted the encoded text back into plaintext and revealed the instructions needed for the next stage of the lab.

### How the command works

The `tr` command translates characters from one character set to another.

In this case:

```text
"d-za-cD-ZA-C"
```

represents the shifted alphabet, while:

```text
"a-zA-Z"
```

represents the normal alphabet.

This allowed me to reverse the Caesar cipher and recover the readable instructions.

---

### 4. Return to the Home Directory

After decoding the instructions, I returned to the home directory:

```bash
cd ~
```

---

### 5. Decrypt the Encrypted File

I used OpenSSL to decrypt the encrypted data file:

```bash
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k '<LAB_PASSWORD>'
```

For this public portfolio repository, the lab password is intentionally replaced with:

```text
<LAB_PASSWORD>
```

### OpenSSL options used

| Option              | Purpose                                       |
| ------------------- | --------------------------------------------- |
| `aes-256-cbc`       | Uses AES-256 encryption with CBC mode         |
| `-pbkdf2`           | Uses PBKDF2 for password-based key derivation |
| `-a`                | Handles Base64 encoding/decoding              |
| `-d`                | Specifies decryption mode                     |
| `-in Q1.encrypted`  | Specifies the encrypted input file            |
| `-out Q1.recovered` | Specifies the recovered output file           |
| `-k`                | Provides the password used for decryption     |

---

### 6. Verify the Recovered File

After decrypting the file, I listed the directory contents:

```bash
ls
```

I then displayed the recovered file:

```bash
cat Q1.recovered
```

This allowed me to verify that the encrypted data had been successfully recovered and reveal the hidden message.

## Commands Used

```bash
# Explore the home directory
ls
cat README.txt

# Navigate to the Caesar cipher directory
cd caesar
ls -a
cat .leftShift3

# Decode the Caesar cipher
cat .leftShift3 | tr "d-za-cD-ZA-C" "a-zA-Z"

# Return to the home directory
cd ~

# Decrypt the encrypted file
openssl aes-256-cbc -pbkdf2 -a -d -in Q1.encrypted -out Q1.recovered -k '<LAB_PASSWORD>'

# Verify the recovered file
ls
cat Q1.recovered
```

## Key Learning Outcomes

Through this lab, I practiced:

* Linux directory navigation
* File and directory inspection
* Reading files from the command line
* Identifying hidden Linux files
* Understanding and reversing a Caesar cipher
* Using the `tr` command for character translation
* Using OpenSSL from the Linux command line
* Decrypting data using AES-256-CBC
* Understanding the role of PBKDF2 in password-based key derivation
* Recovering encrypted data and verifying the recovered file

## Security Relevance

Encryption is an important security control used to protect information.

As a security analyst, understanding encryption and decryption is important when working with protected data and evaluating security controls.

This lab demonstrated how Linux command-line tools can be combined with cryptographic techniques to investigate files, uncover hidden instructions, decode information, and recover encrypted data in an authorized environment.

## Evidence

Screenshots documenting the lab steps are available in the `screenshots.pdf` .

Suggested evidence includes:

* Home directory contents
* README instructions
* Hidden `.leftShift3` file
* Caesar cipher decoding
* OpenSSL decryption
* Recovered file and hidden message

## Repository Structure

```text
linux-file-decryption-cryptography-lab/
│
├── README.md
│
├── commands.txt
│
└── screenshots.pdf

```

## Security & Privacy Note

This repository is intended for educational and portfolio purposes.

No passwords, credentials, API keys, tokens, or other sensitive information should be published in the repository. The lab password is represented as `<LAB_PASSWORD>` in the documentation.


## Disclaimer

This project was completed as part of an authorized cybersecurity training lab for educational purposes. The techniques demonstrated were performed within the provided lab environment.

## Skills Demonstrated

`Linux` `Bash` `Cryptography` `Encryption` `Decryption` `OpenSSL` `AES-256-CBC` `PBKDF2` `Caesar Cipher` `Command Line` `Cybersecurity` `Information Security`

GitHub - https://github.com/PankajSwami-Cyber

Linkedin - www.linkedin.com/in/pankajswamicyber


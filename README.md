# Parzaan-Cybersecurity_Task_1

# GDG Recruitments 2026: Cybersecurity Task 1 Writeup

## Introduction
This document outlines my investigative process for Task 1 and Task 1B. As a beginner in cybersecurity, my goal was to apply a structured methodology to each challenge. While I was unable to retrieve the final flags within the time limit, the following sections document the tools I explored, the logic I applied, and the technical roadblocks I encountered during my attempts.

---

## Task 1A: The 3-Level CTF
**Objective:** Formulate a strategy to recover three hidden fragments for the flag format: `Gdg{part1_part2_part3}`.

### Level 1: Hidden Files & Directory Traversal
* **The Strategy:** My first instinct was to check for "hidden" files that don't appear in standard directory listings, as these are often used to store hints or flag fragments in CTF environments.
* **The Investigation:** 1. I navigated to the `gdg_part1` directory and executed `ls -la` to view all contents, including those prefixed with a dot (`.`).
    2. I located a `.hint` file and attempted to decode its contents (which appeared to be Base64).
* **The Roadblock:** While I identified the likely hidden files, I struggled to bypass the final permission layer or encoding required to read the actual fragment text before the time expired.

### Level 2: Steganography (Image Analysis)
* **The Strategy:** Given the image `heheheha.png`, I looked for data hidden within the file's pixels or metadata.
* **The Investigation:**
    1. I used `exiftool` to scan for hidden comments, unusual timestamps, or suspicious software tags in the metadata.
    2. I researched **LSB (Least Significant Bit)** encoding, where fragments are hidden in the binary "noise" of the image colors. 
    
    3. I attempted to use `zsteg` to isolate different bit planes (Red, Green, Blue) to find a text string.
* **The Result:** I found suspicious patterns in the Red channel, but I was unable to successfully extract a readable string during the challenge window.

### Level 3: Automation vs. The "QR Bomb"
* **The Strategy:** Faced with 3,000 QR codes, I realized manual analysis was a "rabbit hole" designed to waste time. 
* **The Investigation:**
    1. I designed a Python logic to automate the search. The plan was to use `PIL` for image handling and `pyzbar` for decoding.
    2. **The Logic:** Iterate through all 3,000 files and `print()` only the content that matched the "Gdg" prefix.
* **The Roadblock:** I ran into a "to hell with dependencies" part where the `pyzbar` library could not link to the necessary `libzbar` system drivers on my local machine. I spent most of the remaining time troubleshooting the environment rather than running the final scan.

---

## Task 1B: apple_pi3 (Binary Analysis)
**Objective:** Audit a Linux binary to see if sensitive data can be recovered from an obfuscated state.

### 1. Static Analysis Attempts
* I used the `strings` command to peer into the binary. I noticed references to `strcmp` and `printf`, which suggested the program performs a comparison between user input and a "secret" string stored internally.


### 2. Dynamic Analysis & Tracing
* **The Approach:** I attempted to use `ltrace ./apple_pie` to catch the binary de-obfuscating its secret in memory. 
* **The Theory:** If the program de-obfuscates the flag at runtime, `ltrace` should capture the plain-text flag as an argument to the `strcmp` function right before checking my input.


### 3. Debugging (GDB)
* I tried setting a breakpoint at the `main` function using **GDB**. My goal was to step through the assembly code and inspect the registers (`RDI`/`RSI`) where the comparison happens.
* **The Result:** Due to my limited experience with assembly and the binary's basic obfuscation, I was unable to correctly identify the specific memory address holding the flag before the session ended.

---

## Technical Hurdles & Failure Analysis
* **Technological Roadblocks:** The biggest hurdle was environment configuration (specifically for the QR-scanner and GDB). This taught me that having a "ready-to-go" toolkit is just as important as knowing the theory.
* **Logic vs. Execution:** My logic for identifying the vulnerabilities (LSB in stego, `strcmp` in binaries) was sound, but my I couldn't execute it as fast as I am super new to this.
* **Final Reflection:** Although I did not capture the flags, this task provided an immense learning curve regarding how developers attempt to hide data and how a security researcher systematically peels back those layers.


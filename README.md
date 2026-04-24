# Learning Diary System (Phase 1: Stabilization)

### What is this?
This is my personal tool to track my progress as an IT student. I built it to automate my documentation and show my learning curve on GitHub.

---

### Current Status: Cleaning the Logic
I spent today refactoring the core logic. I realized that the system was too sensitive to how I typed my categories (e.g., "python" vs "Python").

**What I fixed today:**
* **Case-Insensitivity:** The system now treats "test", "Test", and "TEST" as the exact same category.
* **Standardized Output:** No matter how I type it, the output always looks clean (First letter capitalized, the rest lowercase).
* **Sorting & Grouping:** Entries are now correctly grouped together, even if I made a typo with capitalization.

---

### The Next Steps (Planning Phase)
I’m currently planning the jump to **Concept 2 & 3**.

* **The Goal:** Moving deep-dive content to Google Docs and using the Diary as a high-speed index with a Tag-based search.
* **Status:** I’ve spent the day researching "Learning Domains" in IT and preparing the Google Docs structure. Implementation starts next week.

---

### My Philosophy
> "I hate chaos. Before I build new features, I make sure the current logic is solid."

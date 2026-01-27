---
name: task_manager
description: Logic for parsing, picking, and updating tasks in TASKMASTER.md
---

# Task Manager Skill

This skill provides the standard procedure for interacting with the `TASKMASTER.md` file.

## 1. Get Next Task
To find the next task to work on:
1.  Read `TASKMASTER.md`.
2.  Look for the first occurrence of an uncompleted task marker: `- [ ]` or `- [/]` (in progress).
3.  **Priority**:
    - "In Progress" section/items first.
    - "Next Steps" / "Backlog" section next.
4.  **Output**: Extract the task description.

## 2. Contextualize
Before starting the task:
1.  Identify key files mentioned in the task description.
2.  Read those files to understand the current state.
3.  If the task is vague (e.g., "Implement feature X"), check `implementation_plan.md` if it exists, or create a plan first.

## 3. Mark Complete
Upon successful verification of the task:
1.  Use `multi_replace_file_content` to change `-[ ]` or `-[/]` to `-[x]`.
2.  Update the Global Context or Status section if relevant.

## 4. Safety Rules
- **Never** mark a task as done without verification (build, test, or visual check).
- **Never** skip tasks unless explicitly instructed by the user.
- If a task is blocked, mark it with a warning icon (e.g., `-[!]`) and notify the user.

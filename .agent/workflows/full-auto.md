---
description: Autonomously executes the next pending task from TASKMASTER.md
---

# Workflow: Full-Auto

This workflow allows you to pick up the next task from `TASKMASTER.md` and execute it autonomously.

## 1. Load Skills
- View `.agent/skills/task_manager/SKILL.md` to understand how to parse the task board.

## 2. Identify Task
- Read `TASKMASTER.md`.
- Identify the highest priority uncompleted task (Use `task_manager` logic).
- **Notify User**: "Starting Full-Auto on task: [Task Name]"

## 3. Planning & Context
- **Analyze**: What does this task require?
- **Plan**: If complex, create/update `implementation_plan.md`. If simple, plan internally.
- **Dependencies**: Check if previous tasks (e.g., installs) are actually done.

## 4. Execution
- Perform the necessary tool calls (Code edits, commands, file creation).
- **Iterate**: If errors occur, fix them. You have permission to retry up to 3 times before stopping for help.

## 5. Verification
- Run relevant tests (`smoke-test.sh`, unit tests, or build checks).
- **Critique**: Did I actually solve the user's request?

## 6. Completion
- Mark the task as `[x]` in `TASKMASTER.md`.
- **Commit**: `git commit -am "feat: [Task Name] (auto)"`
- **Output**: "Task [Task Name] complete. Ready for next?"

// turbo
## 7. Auto-Continue (Optional)
- If the user has enabled "Turbo Mode" (explicitly stated), loop back to Step 2 immediately.
- Otherwise, **Stop** and wait for user confirmation.

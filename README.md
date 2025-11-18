Core_Tool_Arch Simple Demo

A minimal metadata-driven workflow demo showing how business tasks execute through interchangeable tool layers.

Run python plan_interpreter.py

To switch toolsets, open plan_interpreter.py and change this line:

execute_plan("plan.json", world="en")


📌 Overview

This project is a tiny, self-contained example of a metadata-driven workflow architecture.
It demonstrates how a declarative plan (JSON) can orchestrate business tasks, which in turn rely on a pluggable set of “tools.”

The entire system is intentionally small and readable so that the core architecture stands out clearly:

plan.json defines what to run

plan_interpreter.py defines how to run it

business_methods.py defines business intent

tools_en.py / tools_af.py define execution worlds

Switching between English and Afrikaans toolsets shows how the same workflow can run identically in different execution contexts.

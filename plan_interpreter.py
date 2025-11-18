# plan_interpreter.py

import json
import business_methods

def load_tools(world):
    if world == "en":
        import tools_eng as tools
    elif world == "af":
        import tools_afr as tools
    return tools

def execute_plan(plan_path, world="en"):
    tools = load_tools(world)

    with open(plan_path, "r") as f:
        plan = json.load(f)

    for step in plan["steps"]:
        action = step["action"]
        fn = getattr(business_methods, action)
        print(f"\n>>> Executing: {action}")
        fn(tools)

if __name__ == "__main__":
    # Change world between "en" and "af"
    execute_plan("plan.json", world="en")

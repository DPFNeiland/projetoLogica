from services.problem_service import load_problem

data = load_problem(2)

print(data["problem"]["statement"])

for hint in data["hints"]:
    input(">> ")
    print(hint["content"])
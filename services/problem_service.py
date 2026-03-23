from database.queries import get_problem, get_hints

def load_problem(problem_id):
    problem = get_problem(problem_id)
    hints = get_hints(problem_id)

    return {
        "problem": problem,
        "hints": hints
    }   
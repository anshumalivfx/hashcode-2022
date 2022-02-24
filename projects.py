projects = {}

number_of_projects = int(input())

for i in range(number_of_projects):
    project_name, completion_time_required, score, best_before, number_contributors = input().split()
    completion_time_required = int(completion_time_required)
    score = int(score)
    best_before = int(best_before)
    number_contributors = int(number_contributors)
    
    
    skill_temp = []
    
    for j in range(number_contributors):
        temp_skills = {}
        skill_required, level = input().split()
        level = int(level)
        temp_skills["skills"] = skill_required
        temp_skills["level"] = level
        skill_temp.append(temp_skills)
    
        
    projects[project_name] = {
        "completion_time_required": completion_time_required,
        "score": score,
        "best_before": best_before,
        "number_contributors": number_contributors,
        "skill_required": skill_temp
    }

def assign_team(score):
    
    if score >= 90:
        return "Elite Team"

    elif score >= 70:
        return "Advanced Team"

    else:
        return "Starter Team"
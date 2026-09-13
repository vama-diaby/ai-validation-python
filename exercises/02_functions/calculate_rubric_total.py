def calculate_rubric_total(
    accuracy_score,
    relevance_score,
    completeness_score,
    clarity_score,
    instruction_following_score,
):
    return (
        accuracy_score
        + relevance_score
        + completeness_score
        + clarity_score
        + instruction_following_score
    )

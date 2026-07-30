from task.folder.solution.solution import rank_candidates

def test_ranking():
    result = rank_candidates()
    
    # simple check (adjust if needed)
    assert isinstance(result, dict)

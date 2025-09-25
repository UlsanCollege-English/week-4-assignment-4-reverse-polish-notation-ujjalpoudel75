def test_examples():
    from src.rpn import eval_rpn
    assert eval_rpn(["2","1","+","3","*"]) == 9
    assert eval_rpn(["4","13","5","/","+"]) == 6
    assert eval_rpn(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22

def test_negatives_and_div():
    from src.rpn import eval_rpn
    assert eval_rpn(["-7","3","/"]) == -2  # -7/3 = -2.333 -> -2
    assert eval_rpn(["7","-3","/"]) == -2


# --- Edge Cases ---
def test_edge_single_number_only():
    from src.rpn import eval_rpn
    assert eval_rpn(["42"]) == 42

def test_edge_large_negative_and_truncation_mix():
    from src.rpn import eval_rpn
    # (-7 3 /) -> -2, then * 5 -> -10, then + 1 -> -9
    assert eval_rpn(["-7","3","/","5","*","1","+"]) == -9

# --- Longer Scenario ---
def test_long_expression_mixed_ops():
    from src.rpn import eval_rpn
    tokens = ["15","7","1","1","+","-","/","3","*","2","1","1","+","+","-"]
    # This is a classic long RPN example: result should be 5
    assert eval_rpn(tokens) == 5

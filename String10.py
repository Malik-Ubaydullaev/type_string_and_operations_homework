def main(x,y):
    """
    Given three integers, x, y, return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    result = (x+y)*2
    answer = "(" + str(x) + "+" + str(y) + ")*2=" + str(result)
    return answer
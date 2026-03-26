from postfix_evaluator import PostfixEvaluator

postfix = ["5 3 +",
           "8 2 - 3 +",
           "5 3 8 * +",
           "6 2 / 3 +",
           "5 8 + 3 -",
           "5 3 + 8 *",
           "8 2 3 * + 6 -",
           "5 3 8 * + 2 /",
           "8 2 + 3 6 * -",
           "5 3 + 8 2 / -"]

expected = [8, 9, 29, 6.0, 10, 64, 8, 14.5, -8, 4.0]

for i in range(len(postfix)):
    evaluator = PostfixEvaluator(postfix[i])
    result = evaluator.evaluate()
    print(f"{postfix[i]} = {result} (expected: {expected[i]})")
#passes test
"""[5 3 +] = 8
[8 2 - 3 +] = 9
[5 3 8 * +] = 29
[6 2 / 3 +] = 6.0
[5 8 + 3 -] = 10
[5 3 + 8 *] = 64
[8 2 3 * + 6 -] = 8
[5 3 8 * + 2 /] = 14.5
[8 2 + 3 6 * -] = -8
[5 3 + 8 2 / -] = 4.0"""
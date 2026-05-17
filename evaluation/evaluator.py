import json

from app.service import VisionService


def run():

    with open("evaluation/test_cases.json") as f:
        cases = json.load(f)

    for case in cases:

        result = VisionService.process(
            case["image"],
            case["question"]
        )

        answer = result["answer"].lower()

        passed = any(
            k in answer
            for k in case["expected_keywords"]
        )

        print(case["id"], "PASS" if passed else "FAIL")

import json

from app.service import VisionService


def run():

    with open("evaluation/test_cases.json") as f:
        cases = json.load(f)

    results = []

    print("\n=== Evaluation ===\n")

    for case in cases:

        result = VisionService.process(
            case["image"],
            case["question"]
        )

        answer = result["answer"].lower()

        passed = any(
            k.lower() in answer
            for k in case["expected_keywords"]
        )

        case_result = {
            "id": case["id"],
            "passed": passed,
            "answer": answer
        }

        results.append(case_result)

        print(case["id"], "PASS" if passed else "FAIL")

    return results


if __name__ == "__main__":
    run()

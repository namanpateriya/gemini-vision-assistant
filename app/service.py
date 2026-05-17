from app.vision.processor import VisionProcessor


class VisionService:

    @staticmethod
    def process(
        image_path,
        question
    ):

        answer = VisionProcessor.analyze_image(
            image_path,
            question
        )

        return {
            "status": "success",
            "answer": answer
        }

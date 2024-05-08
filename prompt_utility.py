class PromptUtility:
    @staticmethod
    def get_yes_no_answer(question: str) -> bool:
        while True:
            answer = input(question)
            if answer is None or len(answer) == 0:
                print("please respond with y, n, Yes, yes, No or no")
            else:
                answer = answer.lower()[:1]
                match answer:
                    case 'y':
                        return True

                    case 'n':
                        return False

                    case _:
                        print("please respond with y, n, Yes, yes, No or no")


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

    @staticmethod
    def get_quantity(question: str, min_value: int = 0, max_value: int = 10) -> int:
        """Prompt for a number between min_value and max_value"""
        question = f'{question} (between {min_value} and {max_value})?>'
        count: int = min_value - 1
        while count < min_value or count > max_value:
            try:
                count = int(input(question))
                if count < min_value or count > max_value:
                    print(f'Please enter a number between {min_value} and {max_value}.')
                else:
                    return count
            except ValueError:
                print(f'Please enter a value between {min_value} and {max_value}')

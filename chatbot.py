import json;
from difflib import get_close_matches;
from typing import List

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file);
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_knowledge_match(user_question: str, questions: List[str]) -> str :
    matches: List = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str :
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        

def chat_bot(question_val):
    knowledge_base: dict = load_knowledge_base('knowledge_base.json')

    while True:
        # user_input: question_val;

        # if user_input.lower() == 'quit':
        #     break

        best_match: str = find_knowledge_match(question_val, [q["question"] for q in knowledge_base["questions"]])

        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            return f'Bot: {answer}';
        else:
            print('Bot: I don\'t know the answer. Can you teach me?')
            new_answer: str = input('Type the answer or "" to skip: ')

            if new_answer.lower() != '':
                knowledge_base["questions"].append({"question": question_val, "answer": new_answer})
                save_knowledge_base('knowledge_base.json', knowledge_base)
                return 'Bot: Thank you! I learned a new response!';

if __name__ == '__main__':
    chat_bot("hi")
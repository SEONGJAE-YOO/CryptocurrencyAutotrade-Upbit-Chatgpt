from autotrade import get_instructions
import csv 
import re
  
def count_tokens_in_markdown_file(markdown_text):
    # 공백을 기준으로 텍스트를 토큰으로 분할하고 그 갯수를 반환합니다.
    code_blocks_removed = remove_code_blocks(markdown_text)
    # 토큰 수 계산
    token_count = count_tokens(code_blocks_removed)
    
    return token_count

def remove_code_blocks(markdown_text):
    import re
    # 정규식을 사용하여 코드 블록 제거
    pattern = r'```[\s\S]*?```'
    code_blocks_removed = re.sub(pattern, '', markdown_text)
    return code_blocks_removed

def count_tokens(text):
    # 공백을 기준으로 텍스트를 토큰으로 분할하고 그 갯수를 반환합니다.
    tokens = text.split()
    return len(tokens)


def count_tokens_in_csv(file_path):
    total_tokens = 0
    
    with open(file_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        # 각 행에 대해
        for row in reader:
            # 각 셀의 내용을 하나의 텍스트로 합침
            row_text = ' '.join(row)
            # 정규식을 사용하여 텍스트를 토큰으로 분할
            tokens = re.findall(r'\b\w+\b', row_text)
            #print(tokens)
            total_tokens += len(tokens)
    
    return total_tokens


if __name__ == "__main__":
    instructions_path = "instructions.md"
    instructions = get_instructions(instructions_path)
    
    if not instructions:
        print("No instructions found.")
    
    count_result = count_tokens_in_markdown_file(instructions)
    print(f"Count tokens in instructions.md file: {count_result}")
    
    # 엑셀 파일 경로
    excel_file_path = "daily_hourly.csv"
    # 토큰 수 계산
    token_count = count_tokens_in_csv(excel_file_path)
    print("Total number of tokens in the csv file:", token_count)





"""
** chatgpt api를 사용하여 엑셀데이터를 넣을때도 토큰수가 증가하니? **


네, ChatGPT API를 사용하여 텍스트를 분석하거나 생성할 때에도 텍스트의 양에 따라 토큰 수가 증가할 수 있습니다. ChatGPT API는 텍스트 입력의 최대 길이를 설정하고 있으며, 이를 초과하는 경우에는 에러가 발생할 수 있습니다. 일반적으로 텍스트의 양이 증가하면 토큰 수도 증가하므로, 텍스트 입력의 크기에 주의해야 합니다.

따라서 ChatGPT API를 사용하여 비트코인 데이터들을 보낼때도 토큰 수를 고려해야 합니다. 만약 엑셀의 길이이 많은 경우에는 적절히 분할하거나 요약하여 API에 전달하는 것이 좋습니다.

"""
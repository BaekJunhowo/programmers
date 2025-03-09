import os
import re
import glob


def extract_numbered_patterns_without_bold(folder_path='.'):
    # 현재 폴더에서 모든 .md 파일 찾기
    md_files = glob.glob(os.path.join(folder_path, '*.md'))

    # 추출된 텍스트를 저장할 리스트
    extracted_texts = []

    # 각 md 파일 처리
    for md_file in md_files:
        file_patterns = []
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # 숫자. 뒤에 공백이 오는 패턴 및 그 뒤의 문자열
            pattern = r'(\d+\.\s+.+?)(?=\n\d+\.\s+|\n\n|\Z)'
            matches = re.findall(pattern, content, re.DOTALL)

            if matches:
                for match in matches:
                    # ** 기호 제거
                    clean_match = re.sub(r'\*\*', '', match)
                    file_patterns.append(clean_match)

            # 파일에서 패턴을 찾았다면 파일 정보와 함께 추가
            if file_patterns:
                extracted_texts.append(f"파일: {md_file}")
                extracted_texts.append("=" * 50)
                for clean_text in file_patterns:
                    extracted_texts.append(clean_text.strip())
                # extracted_texts.append("=" * 50 + "\n")
                extracted_texts.append("\n")
        except Exception as e:
            print(f"파일 {md_file} 처리 중 오류 발생: {e}")

    # 추출된 텍스트가 있다면 파일로 저장
    if extracted_texts:
        try:
            with open('extracted_content.txt', 'w', encoding='utf-8') as f:
                f.write('\n'.join(extracted_texts))
            return True
        except Exception as e:
            print(f"파일 저장 중 오류 발생: {e}")
            return False

    return False


# 함수 실행
if __name__ == "__main__":
    result = extract_numbered_patterns_without_bold()
    if result:
        print("번호가 매겨진 패턴 추출이 완료되었습니다. 'txt' 파일을 확인하세요.")
    else:
        print("해당 패턴이 발견되지 않았습니다.")
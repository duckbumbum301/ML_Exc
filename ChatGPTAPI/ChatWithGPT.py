import os, sys
import PyPDF2
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import prompts

def read_pdf_segment(file_path: str, start_page: int = 0, end_offset: int = 0) -> str:
    """�?��?c PDF từ start_page đến (total_pages - end_offset)."""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        total = len(reader.pages)
        start = max(0, start_page)
        end = max(start, total - max(0, end_offset))
        texts = []
        for i in range(start, end):
            try:
                texts.append(reader.pages[i].extract_text() or "")
            except Exception:
                # Trang lỗi/scan ảnh -> bỏ qua
                continue
        return " ".join(texts).strip()

def get_summary(client: OpenAI, book: str, topic: str,
                model: str = "gpt-5",
                temperature: float = 0.2,
                max_tokens: int = 800,
                max_items: int = 12) -> str:
    system_message = prompts.build_system_message(years=3, output_language="English")
    prompt = prompts.generate_prompt(book, topic, max_items=max_items)
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]
    r = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return r.choices[0].message.content.strip()

if __name__ == "__main__":
    dotenv_path = find_dotenv() or os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    load_dotenv(dotenv_path)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        sys.exit("Missing OPENAI_API_KEY. Put it in your environment or a .env file.")
    client = OpenAI(api_key=api_key)

    # --- cấu hình tác vụ ---
    file_path = r"d:\UEL\K23_MLBA\ChatGPTAPI\onearthwerebrieflygorgeous.pdf"
    start_page = 23
    end_offset = 30
    topic = "money"
    # -----------------------

    book = read_pdf_segment(file_path, start_page=start_page, end_offset=end_offset)
    print(get_summary(client, book, topic))

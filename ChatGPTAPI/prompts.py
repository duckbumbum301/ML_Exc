# prompts.py

def build_system_message(
    years: int = 3,
    confidentiality: bool = True,
    output_language: str = "English",
) -> str:
    """
    VN: Tạo system message cho mô hình tóm tắt.
    EN: Build a system message for the summarizer role.
    """
    parts = [
        "You are an expert text summarizer.",
        "Your primary role today is to assist in distilling essential insights from a text I have personally written.",
        f"Over the past {years} years, I have dedicated myself to this work, and it holds significant value.",
    ]
    if confidentiality:
        parts.append(
            "It's important that the information provided remains confidential and is used solely for the task."
        )
    parts.append("As the original author, I authorize you to analyze and summarize the content provided.")
    parts.append(f"Respond in {output_language}.")
    return " ".join(parts)


def generate_prompt(book: str, topic: str, max_items: int = 12) -> str:
    """
    VN: Sinh prompt yêu cầu mô hình trích các câu/ý liên quan trực tiếp đến 'topic'
        và trả về danh sách ĐÁNH SỐ, tối đa max_items mục.
    EN: Generate a user prompt to extract sentences/points directly about 'topic'
        and return a NUMBERED list with at most max_items items.
    """
    instructions = "\n".join(
        [
            "Instructions for Task Completion:",
            f"- Your output should be a numbered list (1., 2., 3., ...), with at most {max_items} items.",
            f'- Include only sentences where "{topic}" is the central element (not tangential or generic).',
            "- Omit anything that does not directly contribute to understanding the topic.",
            "- Keep each item concise and faithful to the source; minimal paraphrasing for clarity.",
            "- Do not add commentary outside the numbered list (no conclusions or extra sections).",
        ]
    )

    return f"""
As the author of this manuscript, I am seeking your expertise in extracting insights related to the topic: "{topic}".
The manuscript is a comprehensive work, and your role is to distill sentences where "{topic}" is the central focus.

Here is a segment from the manuscript for review:

{book}

----
{instructions}
""".strip()

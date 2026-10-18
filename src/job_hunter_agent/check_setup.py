"""Step 1 check: are the API keys loaded and does Claude answer?"""

import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic


def main() -> None:
    load_dotenv()

    for key in ("ANTHROPIC_API_KEY", "LANGSMITH_API_KEY"):
        status = "OK" if os.getenv(key) else "MISSING"
        print(f"{key}: {status}")

    llm = ChatAnthropic(model="claude-haiku-5-5", max_tokens=50)
    reply = llm.invoke("Say 'setup works' in 3 words.")
    print("Claude says:", reply.content)
    print("Tokens used:", reply.usage_metadata)


if __name__ == "__main__":
    main()

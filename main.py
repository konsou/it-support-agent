import argparse

import settings
from chat_session import chat_session


def main():
    parser = argparse.ArgumentParser(description="AI Helper Command Line Interface")
    parser.add_argument(
        "-w", "--work-dir", type=str, help="Working directory for the assistant"
    )

    args = parser.parse_args()

    if args.work_dir:
        settings.AGENT_WORK_DIR = args.work_dir
        print(f"Using work dir: {args.work_dir}")
    chat_session()


if __name__ == "__main__":
    main()
